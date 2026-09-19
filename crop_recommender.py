"""
Matching logic for the crop recommender.

Strict-match policy: a crop is only recommended if it satisfies every
criterion the user gave (growing method, soil type, climate zone, and
available area). No partial/closest-match fallback — if nothing
qualifies, the caller shows an empty-result message instead of
guessing.
"""

from crop_data import CROPS


def recommend_crops(growing_method, soil_type, climate_zone, area_sqft):
    """
    Returns a list of (crop_name, crop_dict) tuples for every crop that
    fully matches all four criteria, sorted by growth_duration_days
    (fastest to harvest first, since that's generally most actionable
    for a new grower).
    """
    matches = []

    for name, crop in CROPS.items():
        if growing_method not in crop["growing_methods"]:
            continue
        if soil_type not in crop["soil_types"]:
            continue
        if climate_zone not in crop["climate_zones"]:
            continue
        if area_sqft < crop["min_area_sqft"]:
            continue
        matches.append((name, crop))

    matches.sort(key=lambda pair: pair[1]["growth_duration_days"])
    return matches