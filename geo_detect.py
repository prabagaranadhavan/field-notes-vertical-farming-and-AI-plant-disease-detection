"""
Browser-side location detection for the Crop Recommender.

Streamlit has no native geolocation API, so this renders a small HTML
button that:
  1. Asks the browser for the user's coordinates (navigator.geolocation).
  2. Reverse-geocodes those coordinates to a country/state/city using
     BigDataCloud's free, no-key, CORS-enabled reverse-geocode API —
     this call happens in the user's own browser, not on the server.
  3. Writes the result into the page's URL query string and reloads,
     so Python can read it back via st.query_params on the next run.

This is a well-known workaround for one-way browser -> Streamlit
communication without a custom bidirectional component: a sandboxed
iframe is allowed to navigate its parent frame even when it can't read
the parent's location, so `window.parent.location.href = ...` works
from within components.html.

If the user denies the location permission, or it's on a browser/
device without geolocation, the button just shows an error message
and the manual dropdown in the page still works normally.
"""

import streamlit as st
import streamlit.components.v1 as components


def render_locate_button(label, detecting_label, denied_label):
    """
    Renders the "detect my location" button. On success, the page
    reloads with ?geo_lat=&geo_lon=&geo_country=&geo_state=&geo_place=
    query params set — read these back with read_geo_query_params().
    """
    html = f"""
    <div style="font-family:'IBM Plex Mono', monospace;">
      <button id="locate-btn" style="
          background:#D98F52; color:#14231A; border:none; border-radius:2px;
          padding:0.6rem 1rem; font-size:0.82rem; letter-spacing:0.04em;
          text-transform:uppercase; cursor:pointer; width:100%;">
        {label}
      </button>
      <div id="locate-status" style="
          font-size:0.72rem; color:#8FA893; margin-top:0.4rem; min-height:1rem;"></div>
    </div>
    <script>
      const btn = document.getElementById("locate-btn");
      const status = document.getElementById("locate-status");

      btn.addEventListener("click", function() {{
        if (!navigator.geolocation) {{
          status.innerText = "{denied_label}";
          return;
        }}
        status.innerText = "{detecting_label}";
        btn.disabled = true;

        navigator.geolocation.getCurrentPosition(
          async function(position) {{
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            let country = "";
            let state = "";
            let place = "";

            try {{
              const resp = await fetch(
                "https://api.bigdatacloud.net/data/reverse-geocode-client?latitude="
                + lat + "&longitude=" + lon + "&localityLanguage=en"
              );
              const data = await resp.json();
              country = data.countryName || "";
              state = data.principalSubdivision || "";
              place = [data.city || data.locality || "", state, country]
                .filter(Boolean).join(", ");
            }} catch (e) {{
              place = lat.toFixed(2) + ", " + lon.toFixed(2);
            }}

            const params = new URLSearchParams(window.parent.location.search);
            params.set("geo_lat", lat);
            params.set("geo_lon", lon);
            params.set("geo_country", country);
            params.set("geo_state", state);
            params.set("geo_place", place);

            window.parent.location.search = params.toString();
          }},
          function(error) {{
            status.innerText = "{denied_label}";
            btn.disabled = false;
          }},
          {{ timeout: 10000 }}
        );
      }});
    </script>
    """
    components.html(html, height=70)


def read_geo_query_params():
    """
    Reads back the query params the JS component set after a
    successful detection. Returns a dict with lat, lon, country,
    state, place — any of which may be None if not present.
    """
    params = st.query_params
    lat = params.get("geo_lat")
    lon = params.get("geo_lon")
    country = params.get("geo_country")
    state = params.get("geo_state")
    place = params.get("geo_place")

    if lat is None:
        return None

    return {
        "lat": lat,
        "lon": lon,
        "country": country,
        "state": state,
        "place": place,
    }