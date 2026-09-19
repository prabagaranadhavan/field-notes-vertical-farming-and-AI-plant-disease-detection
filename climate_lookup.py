"""
Resolves a climate zone (one of crop_data.CLIMATE_ZONES) from a
location, so the Crop Recommender can pre-fill the climate dropdown
instead of making the user guess.

Two-tier approach:
1. India state/UT lookup — reasonably accurate for the app's primary
   audience, based on general Köppen classification for each region.
2. Global latitude-band fallback for anywhere else — a coarse
   approximation only (real climate depends on more than latitude,
   e.g. deserts and highlands exist across many latitudes). This is
   why the recommender always keeps the dropdown editable — auto-
   detection is a starting point, not a final answer.
"""

INDIA_STATE_CLIMATE = {
    "Tamil Nadu": "tropical",
    "Kerala": "tropical",
    "Karnataka": "tropical",
    "Andhra Pradesh": "tropical",
    "Telangana": "subtropical",
    "Goa": "tropical",
    "Puducherry": "tropical",
    "Andaman and Nicobar Islands": "tropical",
    "Lakshadweep": "tropical",

    "Maharashtra": "subtropical",
    "Gujarat": "arid",
    "Rajasthan": "arid",
    "Madhya Pradesh": "subtropical",
    "Chhattisgarh": "subtropical",
    "Odisha": "tropical",
    "West Bengal": "subtropical",
    "Jharkhand": "subtropical",
    "Bihar": "subtropical",
    "Uttar Pradesh": "subtropical",

    "Punjab": "subtropical",
    "Haryana": "subtropical",
    "Delhi": "subtropical",
    "Chandigarh": "subtropical",

    "Himachal Pradesh": "temperate",
    "Uttarakhand": "temperate",
    "Jammu and Kashmir": "temperate",
    "Ladakh": "arid",
    "Sikkim": "temperate",

    "Assam": "subtropical",
    "Meghalaya": "subtropical",
    "Manipur": "subtropical",
    "Mizoram": "subtropical",
    "Nagaland": "subtropical",
    "Tripura": "subtropical",
    "Arunachal Pradesh": "temperate",
}


def _normalize(name):
    return (name or "").strip().lower()


_INDIA_LOOKUP_NORMALIZED = {_normalize(k): v for k, v in INDIA_STATE_CLIMATE.items()}


def climate_from_india_state(state_name):
    """Return a climate zone for an Indian state/UT name, or None if
    not recognised (case-insensitive, whitespace-tolerant)."""
    return _INDIA_LOOKUP_NORMALIZED.get(_normalize(state_name))


def climate_from_latitude(lat):
    """Coarse global fallback based on latitude bands only. Used when
    the location isn't in India or the state name isn't recognised."""
    abs_lat = abs(lat)
    if abs_lat <= 23.5:
        return "tropical"
    if abs_lat <= 35:
        return "subtropical"
    if abs_lat <= 55:
        return "temperate"
    return "temperate"


def resolve_climate_zone(country=None, state=None, lat=None, lon=None):
    """
    Best-effort climate zone resolution. Returns (zone, source) where
    source is 'india_state', 'latitude', or None if nothing could be
    determined (caller should fall back to asking the user).
    """
    if country and _normalize(country) in ("india", "in", "bharat"):
        zone = climate_from_india_state(state)
        if zone:
            return zone, "india_state"

    if lat is not None:
        try:
            return climate_from_latitude(float(lat)), "latitude"
        except (TypeError, ValueError):
            pass

    return None, None