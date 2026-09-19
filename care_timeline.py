"""
Stage-by-stage care/maintenance timeline for crops.

Rather than hand-writing a unique timeline for every crop, each crop
is tagged with a category (CROP_CATEGORY), and each category has a
STAGE_TEMPLATE: an ordered list of growth stages defined as percentage
ranges of the crop's own growth_duration_days (from crop_data.py),
plus a set of action bullets for that stage.

get_timeline() turns a crop's percentage-based template into actual
day numbers for that specific crop, so a 30-day radish and a 300-day
sugarcane both get a timeline scaled to their own duration, without
needing 20 separate hand-authored schedules.

All display text is translated via translations.t() using the
*_key values below — see the "Care Timeline" section in
translations.py for the English/Tamil strings.
"""

CROP_CATEGORY = {
    "Spinach": "leafy_green",
    "Lettuce": "leafy_green",
    "Kale": "leafy_green",
    "Fenugreek": "leafy_green",

    "Basil": "herb",
    "Mint": "herb",
    "Coriander": "herb",

    "Tomato_Dwarf": "fruiting_vegetable",
    "Chili_Pepper": "fruiting_vegetable",
    "Cucumber": "fruiting_vegetable",
    "Green_Beans": "fruiting_vegetable",
    "Okra": "fruiting_vegetable",

    "Radish": "root_vegetable",
    "Potato": "root_vegetable",

    "Wheat": "field_crop",
    "Rice_Paddy": "field_crop",
    "Sugarcane": "field_crop",
    "Groundnut": "field_crop",

    "Strawberry": "perennial",
    "Aloe_Vera": "perennial",
}


# Shared action keys reused across multiple categories/stages, to
# avoid repeating identical bullets under different keys.
_PEST_MONITOR = "timeline_action_pest_monitor"
_MULCH = "timeline_action_mulch"
_CHECK_DRAINAGE = "timeline_action_check_drainage"
_REMOVE_WEEDS = "timeline_action_remove_weeds"


STAGE_TEMPLATES = {

    "leafy_green": [
        {
            "title_key": "timeline_stage_germination",
            "start_pct": 0, "end_pct": 15,
            "action_keys": [
                "timeline_action_leafy_moist_soil",
                "timeline_action_leafy_partial_shade",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_vegetative",
            "start_pct": 15, "end_pct": 60,
            "action_keys": [
                "timeline_action_leafy_fertilize",
                _MULCH,
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_pre_harvest",
            "start_pct": 60, "end_pct": 90,
            "action_keys": [
                "timeline_action_leafy_reduce_nitrogen",
                "timeline_action_leafy_thin",
            ],
        },
        {
            "title_key": "timeline_stage_harvest_regrowth",
            "start_pct": 90, "end_pct": 100,
            "action_keys": [
                "timeline_action_leafy_harvest_outer",
                "timeline_action_leafy_refresh_soil",
            ],
        },
    ],

    "herb": [
        {
            "title_key": "timeline_stage_germination",
            "start_pct": 0, "end_pct": 15,
            "action_keys": [
                "timeline_action_herb_light_moisture",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_vegetative",
            "start_pct": 15, "end_pct": 50,
            "action_keys": [
                "timeline_action_herb_pinch",
                _MULCH,
            ],
        },
        {
            "title_key": "timeline_stage_flowering_watch",
            "start_pct": 50, "end_pct": 80,
            "action_keys": [
                "timeline_action_herb_remove_buds",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_continuous_harvest",
            "start_pct": 80, "end_pct": 100,
            "action_keys": [
                "timeline_action_herb_harvest_third",
                "timeline_action_herb_feed_light",
            ],
        },
    ],

    "fruiting_vegetable": [
        {
            "title_key": "timeline_stage_transplant",
            "start_pct": 0, "end_pct": 10,
            "action_keys": [
                "timeline_action_fruit_harden_off",
                _CHECK_DRAINAGE,
            ],
        },
        {
            "title_key": "timeline_stage_vegetative",
            "start_pct": 10, "end_pct": 35,
            "action_keys": [
                "timeline_action_fruit_stake_early",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_flowering",
            "start_pct": 35, "end_pct": 55,
            "action_keys": [
                "timeline_action_fruit_consistent_water",
                "timeline_action_fruit_pollinate",
            ],
        },
        {
            "title_key": "timeline_stage_fruit_development",
            "start_pct": 55, "end_pct": 85,
            "action_keys": [
                "timeline_action_fruit_potassium",
                _MULCH,
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_harvest",
            "start_pct": 85, "end_pct": 100,
            "action_keys": [
                "timeline_action_fruit_harvest_regularly",
                "timeline_action_fruit_support_branches",
            ],
        },
    ],

    "root_vegetable": [
        {
            "title_key": "timeline_stage_germination",
            "start_pct": 0, "end_pct": 15,
            "action_keys": [
                "timeline_action_root_loose_soil",
                "timeline_action_root_gentle_water",
            ],
        },
        {
            "title_key": "timeline_stage_vegetative",
            "start_pct": 15, "end_pct": 50,
            "action_keys": [
                "timeline_action_root_thin",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_bulking",
            "start_pct": 50, "end_pct": 90,
            "action_keys": [
                "timeline_action_root_hill_soil",
                "timeline_action_root_even_water",
            ],
        },
        {
            "title_key": "timeline_stage_harvest",
            "start_pct": 90, "end_pct": 100,
            "action_keys": [
                "timeline_action_root_harvest_promptly",
                "timeline_action_root_loosen_soil",
            ],
        },
    ],

    "field_crop": [
        {
            "title_key": "timeline_stage_sowing",
            "start_pct": 0, "end_pct": 10,
            "action_keys": [
                "timeline_action_field_seed_contact",
                _CHECK_DRAINAGE,
            ],
        },
        {
            "title_key": "timeline_stage_tillering",
            "start_pct": 10, "end_pct": 40,
            "action_keys": [
                "timeline_action_field_topdress",
                _REMOVE_WEEDS,
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_reproductive",
            "start_pct": 40, "end_pct": 65,
            "action_keys": [
                "timeline_action_field_water_stress",
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_yield_fill",
            "start_pct": 65, "end_pct": 90,
            "action_keys": [
                "timeline_action_field_potassium",
                "timeline_action_field_lodging",
            ],
        },
        {
            "title_key": "timeline_stage_harvest",
            "start_pct": 90, "end_pct": 100,
            "action_keys": [
                "timeline_action_field_harvest_timing",
                "timeline_action_field_clear_residue",
            ],
        },
    ],

    "perennial": [
        {
            "title_key": "timeline_stage_establishment",
            "start_pct": 0, "end_pct": 15,
            "action_keys": [
                "timeline_action_perennial_deep_water",
                _CHECK_DRAINAGE,
            ],
        },
        {
            "title_key": "timeline_stage_vegetative",
            "start_pct": 15, "end_pct": 40,
            "action_keys": [
                _MULCH,
                _PEST_MONITOR,
            ],
        },
        {
            "title_key": "timeline_stage_fruiting_onset",
            "start_pct": 40, "end_pct": 70,
            "action_keys": [
                "timeline_action_perennial_remove_runners",
                "timeline_action_perennial_support_stems",
            ],
        },
        {
            "title_key": "timeline_stage_ongoing_harvest",
            "start_pct": 70, "end_pct": 100,
            "action_keys": [
                "timeline_action_perennial_harvest_peak",
                "timeline_action_perennial_renovate",
            ],
        },
    ],
}


def get_timeline(crop_name, growth_duration_days):
    """
    Returns a list of stage dicts for the given crop, scaled to its
    actual growth_duration_days:
        [{"title_key": ..., "day_start": int, "day_end": int,
          "action_keys": [...]}, ...]
    Falls back to the "leafy_green" template if the crop has no
    category mapping (shouldn't happen for crops in crop_data.py, but
    keeps this safe for future additions before they're categorised).
    """
    category = CROP_CATEGORY.get(crop_name, "leafy_green")
    template = STAGE_TEMPLATES[category]

    stages = []
    for stage in template:
        day_start = max(1, round(growth_duration_days * stage["start_pct"] / 100) + (1 if stage["start_pct"] == 0 else 0))
        day_end = max(day_start, round(growth_duration_days * stage["end_pct"] / 100))
        stages.append({
            "title_key": stage["title_key"],
            "day_start": day_start,
            "day_end": day_end,
            "action_keys": stage["action_keys"],
        })
    return stages