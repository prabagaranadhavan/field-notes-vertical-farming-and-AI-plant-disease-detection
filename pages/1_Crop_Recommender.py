import os

import streamlit as st

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from style import get_css, get_topbar_html, PALETTE
from translations import (
    t,
    translate_crop_name,
    translate_option,
)
from crop_data import SOIL_TYPES, CLIMATE_ZONES
from crop_recommender import recommend_crops
from climate_lookup import resolve_climate_zone
from geo_detect import render_locate_button, read_geo_query_params
from care_timeline import get_timeline
from crop_species_link import get_detector_species


GROWING_METHODS = ["vertical", "container", "open_field"]


def render_crop_card(name, crop):
    leaf = PALETTE["leaf"]
    amber = PALETTE["amber"]
    muted = PALETTE["text_muted"]

    irrigation_labels = ", ".join(translate_option(i) for i in crop["irrigation_type"])

    rows = (
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{leaf};">{t("reco_care_water")}</div>'
        f'<div class="care-text">{crop["water_frequency"]}</div>'
        f'</div>'
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{amber};">{t("reco_care_irrigation")}</div>'
        f'<div class="care-text">{irrigation_labels}</div>'
        f'</div>'
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{leaf};">{t("reco_care_sunlight")}</div>'
        f'<div class="care-text">{t("reco_sunlight_hours", hours=crop["sunlight_hours"])}</div>'
        f'</div>'
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{amber};">{t("reco_care_spacing")}</div>'
        f'<div class="care-text">{crop["spacing_cm"]}</div>'
        f'</div>'
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{leaf};">{t("reco_care_duration")}</div>'
        f'<div class="care-text">{t("reco_duration_days", days=crop["growth_duration_days"])}</div>'
        f'</div>'
        f'<div class="care-row">'
        f'<div class="care-heading" style="color:{amber};">{t("reco_care_ph")}</div>'
        f'<div class="care-text">{crop["soil_ph_range"][0]}–{crop["soil_ph_range"][1]}</div>'
        f'</div>'
    )

    card_html = (
        f'<div class="specimen-card">'
        f'<div class="specimen-label">{t("reco_results_kicker")}</div>'
        f'<div class="specimen-name">{translate_crop_name(name)}</div>'
        f'{rows}'
        f'</div>'
    )
    st.markdown(card_html, unsafe_allow_html=True)


def render_care_timeline(name, crop):
    leaf = PALETTE["leaf"]
    amber = PALETTE["amber"]

    stages = get_timeline(name, crop["growth_duration_days"])

    with st.expander(t("timeline_expander_label")):
        for i, stage in enumerate(stages):
            heading_color = leaf if i % 2 == 0 else amber
            actions_html = "".join(
                f'<div class="care-text" style="margin-bottom:0.3rem;">• {t(action_key)}</div>'
                for action_key in stage["action_keys"]
            )
            stage_html = (
                f'<div class="care-row">'
                f'<div class="care-heading" style="color:{heading_color};">'
                f'{t(stage["title_key"])} &nbsp;·&nbsp; '
                f'{t("timeline_day_range", start=stage["day_start"], end=stage["day_end"])}'
                f'</div>'
                f'{actions_html}'
                f'</div>'
            )
            st.markdown(stage_html, unsafe_allow_html=True)


def render_disease_link(name):
    """
    Shows a "check this crop for disease" button when the disease
    detector has coverage for this crop's species; otherwise a quiet
    note that detection isn't available yet. Clicking the button
    stores the crop in session_state (carried across pages within the
    same session) and jumps straight to the Analyser.
    """
    species = get_detector_species(name)
    muted = PALETTE["text_muted"]

    if species:
        if st.button(
            t("reco_check_disease_button"),
            key=f"check_disease_{name}",
            use_container_width=True,
        ):
            st.session_state["analyser_context_crop"] = name
            st.switch_page("pages/2_Analyser.py")
    else:
        st.markdown(
            f'<p style="color:{muted}; font-size:0.78rem; margin-top:0.3rem;">'
            f'{t("reco_disease_not_available")}</p>',
            unsafe_allow_html=True,
        )


def main():
    st.set_page_config(
        page_title="Crop Recommender — Field Notes",
        page_icon="🌾",
        layout="centered"
    )

    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(get_topbar_html(wordmark=t("brand_wordmark")), unsafe_allow_html=True)

    # NOTE: no render_language_switcher() call here — app.py's router
    # already renders it once, globally, on every page. Calling it
    # again here would duplicate the EN/தமிழ் pills in the sidebar.

    st.markdown(f'<div class="kicker">{t("reco_kicker")}</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="font-size:2.2rem; margin-bottom:0.2rem;">{t("reco_title")}</h1>', unsafe_allow_html=True)
    st.markdown(
        f'<p style="color:{PALETTE["text_muted"]}; max-width:32rem;">'
        f'{t("reco_subtitle")}</p>',
        unsafe_allow_html=True
    )

    st.markdown('<hr class="hairline">', unsafe_allow_html=True)

    # ---------- location detection (outside the form: it needs its
    # own button/JS interaction, independent of form submission) ----------
    detected_zone = None
    detected_place = None

    render_locate_button(
        t("reco_locate_button"),
        t("reco_locate_detecting"),
        t("reco_locate_denied"),
    )

    geo = read_geo_query_params()
    if geo:
        detected_place = geo.get("place")
        detected_zone, _source = resolve_climate_zone(
            country=geo.get("country"),
            state=geo.get("state"),
            lat=geo.get("lat"),
        )
        if detected_zone:
            st.markdown(
                f'<p style="color:{PALETTE["text_muted"]}; font-size:0.82rem;">'
                f'{t("reco_locate_detected", place=detected_place, zone=translate_option(detected_zone))}'
                f'</p>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<p style="color:{PALETTE["text_muted"]}; font-size:0.82rem;">'
                f'{t("reco_locate_detected_no_zone", place=detected_place)}'
                f'</p>',
                unsafe_allow_html=True,
            )

    climate_default_index = (
        CLIMATE_ZONES.index(detected_zone) if detected_zone in CLIMATE_ZONES else 0
    )

    with st.form("crop_recommender_form"):
        growing_method = st.selectbox(
            t("reco_form_setup"),
            options=GROWING_METHODS,
            format_func=translate_option,
        )
        soil_type = st.selectbox(
            t("reco_form_soil"),
            options=SOIL_TYPES,
            format_func=translate_option,
        )
        climate_zone = st.selectbox(
            t("reco_form_climate"),
            options=CLIMATE_ZONES,
            index=climate_default_index,
            format_func=translate_option,
        )
        area_sqft = st.number_input(
            t("reco_form_area"),
            min_value=0.0,
            value=10.0,
            step=1.0,
        )
        submitted = st.form_submit_button(t("reco_submit"), use_container_width=True)

    # FIX: results are stored in session_state instead of a local
    # variable. Streamlit reruns this whole script on every widget
    # interaction (clicking "check this crop for disease", switching
    # language, etc.), and `submitted` is only True on the exact run
    # the form was clicked. Without persisting results, any rerun
    # after submission — including the one triggered by the disease
    # -check button itself — would skip straight past this block,
    # the results would disappear, and render_disease_link()'s
    # st.button() would never even get called, so the click that
    # supposedly triggered it silently does nothing.
    if submitted:
        st.session_state["reco_results"] = recommend_crops(
            growing_method, soil_type, climate_zone, area_sqft
        )

    if "reco_results" in st.session_state:
        results = st.session_state["reco_results"]

        st.markdown('<hr class="hairline">', unsafe_allow_html=True)

        if not results:
            st.markdown(
                f'<p style="color:{PALETTE["text_on_ink"]}; '
                f'font-weight:600;">{t("reco_no_results_title")}</p>'
                f'<p style="color:{PALETTE["text_muted"]};">{t("reco_no_results_body")}</p>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="kicker" style="margin-top:0.4rem;">{t("reco_results_kicker")}</div>',
                unsafe_allow_html=True
            )
            for name, crop in results:
                render_crop_card(name, crop)
                render_care_timeline(name, crop)
                render_disease_link(name)
                st.write("")


if __name__ == "__main__":
    main()