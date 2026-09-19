"""
Crop recommendation knowledge base.

One entry per crop. Used by the recommender page to filter/rank crops
against user input: growing setup, soil type, region climate, and
available area — then generate a care plan (watering, irrigation,
spacing, timeline) for each recommended crop.

Field notes:
- growing_methods: list of "vertical", "container", "open_field".
  A crop can support more than one.
- soil_types: list from SOIL_TYPES below.
- climate_zones: list from CLIMATE_ZONES below.
- min_area_sqft: minimum growing area in square feet, for a single
  plant/unit at recommended spacing — used for both container and
  open-field sizing (open-field crops will have larger figures).
- rainfall_mm_range: only meaningful for open_field growing; ignored
  for container/vertical setups where watering is manual/irrigated.
- water_frequency: plain description, independent of irrigation_type.
- irrigation_type: list of suitable irrigation methods for this crop.
- sunlight_hours: minimum daily direct/bright light needed.
- growth_duration_days: sowing/transplant to first harvest.
- spacing_cm: plant-to-plant spacing at maturity.
- soil_ph_range: tuple (min, max).
"""

SOIL_TYPES = [
    "sandy", "loamy", "clay", "silty", "red_soil", "black_soil", "peaty",
]

CLIMATE_ZONES = [
    "tropical", "subtropical", "temperate", "arid",
]

IRRIGATION_TYPES = [
    "drip", "wick", "hydroponic_nft", "sprinkler", "flood", "hand_watering",
]


CROPS = {

    "Spinach": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "black_soil"],
        "climate_zones": ["temperate", "subtropical", "tropical"],
        "temp_range_c": (10, 27),
        "rainfall_mm_range": (400, 800),
        "min_area_sqft": 0.25,
        "water_frequency": "Every 1–2 days, keep soil consistently moist.",
        "irrigation_type": ["drip", "wick", "hydroponic_nft", "hand_watering"],
        "sunlight_hours": 4,
        "growth_duration_days": 40,
        "spacing_cm": "10x10",
        "soil_ph_range": (6.0, 7.5),
    },

    "Lettuce": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "silty"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (7, 24),
        "rainfall_mm_range": (350, 700),
        "min_area_sqft": 0.5,
        "water_frequency": "Daily light watering, keep roots consistently moist.",
        "irrigation_type": ["drip", "wick", "hydroponic_nft", "hand_watering"],
        "sunlight_hours": 5,
        "growth_duration_days": 45,
        "spacing_cm": "20x20",
        "soil_ph_range": (6.0, 7.0),
    },

    "Kale": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "black_soil", "clay"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (7, 26),
        "rainfall_mm_range": (400, 800),
        "min_area_sqft": 1,
        "water_frequency": "Every 2 days, deeper watering than leafy salad greens.",
        "irrigation_type": ["drip", "hydroponic_nft", "hand_watering"],
        "sunlight_hours": 6,
        "growth_duration_days": 55,
        "spacing_cm": "30x30",
        "soil_ph_range": (6.0, 7.5),
    },

    "Basil": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy"],
        "climate_zones": ["tropical", "subtropical"],
        "temp_range_c": (18, 32),
        "rainfall_mm_range": (500, 1000),
        "min_area_sqft": 0.3,
        "water_frequency": "Every 2 days, avoid waterlogging.",
        "irrigation_type": ["drip", "wick", "hydroponic_nft", "hand_watering"],
        "sunlight_hours": 6,
        "growth_duration_days": 60,
        "spacing_cm": "20x20",
        "soil_ph_range": (6.0, 7.0),
    },

    "Mint": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "clay", "silty"],
        "climate_zones": ["tropical", "subtropical", "temperate"],
        "temp_range_c": (15, 30),
        "rainfall_mm_range": (600, 1200),
        "min_area_sqft": 0.3,
        "water_frequency": "Every 1–2 days, prefers consistently damp soil.",
        "irrigation_type": ["drip", "wick", "hand_watering"],
        "sunlight_hours": 4,
        "growth_duration_days": 60,
        "spacing_cm": "25x25",
        "soil_ph_range": (6.0, 7.5),
    },

    "Coriander": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "black_soil"],
        "climate_zones": ["subtropical", "arid"],
        "temp_range_c": (15, 28),
        "rainfall_mm_range": (300, 700),
        "min_area_sqft": 0.2,
        "water_frequency": "Every 2–3 days, light watering.",
        "irrigation_type": ["drip", "wick", "hand_watering"],
        "sunlight_hours": 5,
        "growth_duration_days": 40,
        "spacing_cm": "15x15",
        "soil_ph_range": (6.2, 7.5),
    },

    "Strawberry": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["sandy", "loamy"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (10, 26),
        "rainfall_mm_range": (500, 900),
        "min_area_sqft": 1,
        "water_frequency": "Every 2 days, avoid wetting leaves/fruit directly.",
        "irrigation_type": ["drip", "hydroponic_nft"],
        "sunlight_hours": 6,
        "growth_duration_days": 90,
        "spacing_cm": "30x30",
        "soil_ph_range": (5.5, 6.8),
    },

    "Tomato_Dwarf": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "black_soil"],
        "climate_zones": ["tropical", "subtropical"],
        "temp_range_c": (18, 29),
        "rainfall_mm_range": (600, 1200),
        "min_area_sqft": 2,
        "water_frequency": "Every 2–3 days, deep watering at the base.",
        "irrigation_type": ["drip", "hydroponic_nft"],
        "sunlight_hours": 6,
        "growth_duration_days": 75,
        "spacing_cm": "40x40",
        "soil_ph_range": (6.0, 6.8),
    },

    "Chili_Pepper": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "red_soil"],
        "climate_zones": ["tropical", "subtropical"],
        "temp_range_c": (20, 32),
        "rainfall_mm_range": (600, 1200),
        "min_area_sqft": 1.5,
        "water_frequency": "Every 2–3 days, allow topsoil to dry slightly between.",
        "irrigation_type": ["drip", "hydroponic_nft"],
        "sunlight_hours": 6,
        "growth_duration_days": 80,
        "spacing_cm": "35x35",
        "soil_ph_range": (5.5, 6.8),
    },

    "Cucumber": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "silty"],
        "climate_zones": ["tropical", "subtropical"],
        "temp_range_c": (18, 30),
        "rainfall_mm_range": (600, 1200),
        "min_area_sqft": 3,
        "water_frequency": "Daily, consistent moisture — sensitive to dry spells.",
        "irrigation_type": ["drip", "hydroponic_nft"],
        "sunlight_hours": 6,
        "growth_duration_days": 60,
        "spacing_cm": "45x45",
        "soil_ph_range": (6.0, 7.0),
    },

    "Green_Beans": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "black_soil"],
        "climate_zones": ["tropical", "subtropical", "temperate"],
        "temp_range_c": (16, 29),
        "rainfall_mm_range": (500, 1000),
        "min_area_sqft": 2,
        "water_frequency": "Every 2 days, more frequently during flowering/podding.",
        "irrigation_type": ["drip", "sprinkler"],
        "sunlight_hours": 6,
        "growth_duration_days": 55,
        "spacing_cm": "30x30",
        "soil_ph_range": (6.0, 7.0),
    },

    "Radish": {
        "growing_methods": ["container", "open_field"],
        "soil_types": ["sandy", "loamy", "silty"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (10, 25),
        "rainfall_mm_range": (350, 700),
        "min_area_sqft": 0.3,
        "water_frequency": "Every 1–2 days, light and even watering.",
        "irrigation_type": ["drip", "hand_watering"],
        "sunlight_hours": 5,
        "growth_duration_days": 30,
        "spacing_cm": "10x10",
        "soil_ph_range": (6.0, 7.0),
    },

    "Okra": {
        "growing_methods": ["container", "open_field"],
        "soil_types": ["sandy", "loamy", "red_soil", "black_soil"],
        "climate_zones": ["tropical", "arid"],
        "temp_range_c": (22, 35),
        "rainfall_mm_range": (600, 1100),
        "min_area_sqft": 2,
        "water_frequency": "Every 2–3 days, drought-tolerant once established.",
        "irrigation_type": ["drip", "sprinkler", "flood"],
        "sunlight_hours": 6,
        "growth_duration_days": 65,
        "spacing_cm": "40x40",
        "soil_ph_range": (6.0, 7.5),
    },

    "Potato": {
        "growing_methods": ["container", "open_field"],
        "soil_types": ["sandy", "loamy", "black_soil"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (15, 24),
        "rainfall_mm_range": (500, 900),
        "min_area_sqft": 3,
        "water_frequency": "Every 3–4 days, reduce watering as tubers mature.",
        "irrigation_type": ["drip", "sprinkler", "flood"],
        "sunlight_hours": 6,
        "growth_duration_days": 100,
        "spacing_cm": "30x60",
        "soil_ph_range": (5.0, 6.5),
    },

    "Wheat": {
        "growing_methods": ["open_field"],
        "soil_types": ["loamy", "clay", "black_soil"],
        "climate_zones": ["temperate", "subtropical"],
        "temp_range_c": (10, 25),
        "rainfall_mm_range": (350, 700),
        "min_area_sqft": 500,
        "water_frequency": "4–6 irrigations across the growing season, timed to growth stages.",
        "irrigation_type": ["flood", "sprinkler"],
        "sunlight_hours": 6,
        "growth_duration_days": 120,
        "spacing_cm": "row spacing 20",
        "soil_ph_range": (6.0, 7.5),
    },

    "Rice_Paddy": {
        "growing_methods": ["open_field"],
        "soil_types": ["clay", "silty", "black_soil"],
        "climate_zones": ["tropical", "subtropical"],
        "temp_range_c": (20, 35),
        "rainfall_mm_range": (1000, 2000),
        "min_area_sqft": 1000,
        "water_frequency": "Standing water maintained through most of the growth cycle.",
        "irrigation_type": ["flood"],
        "sunlight_hours": 6,
        "growth_duration_days": 130,
        "spacing_cm": "20x20",
        "soil_ph_range": (5.5, 7.0),
    },

    "Sugarcane": {
        "growing_methods": ["open_field"],
        "soil_types": ["loamy", "black_soil", "clay"],
        "climate_zones": ["tropical"],
        "temp_range_c": (21, 35),
        "rainfall_mm_range": (1100, 2000),
        "min_area_sqft": 800,
        "water_frequency": "Weekly, heavy water requirement through vegetative growth.",
        "irrigation_type": ["flood", "drip"],
        "sunlight_hours": 7,
        "growth_duration_days": 300,
        "spacing_cm": "row spacing 90",
        "soil_ph_range": (6.0, 7.5),
    },

    "Groundnut": {
        "growing_methods": ["open_field"],
        "soil_types": ["sandy", "red_soil"],
        "climate_zones": ["tropical", "arid"],
        "temp_range_c": (20, 30),
        "rainfall_mm_range": (500, 1000),
        "min_area_sqft": 400,
        "water_frequency": "Every 7–10 days, critical during flowering and pegging.",
        "irrigation_type": ["sprinkler", "drip"],
        "sunlight_hours": 6,
        "growth_duration_days": 120,
        "spacing_cm": "30x10",
        "soil_ph_range": (6.0, 7.0),
    },

    "Aloe_Vera": {
        "growing_methods": ["container", "open_field"],
        "soil_types": ["sandy", "red_soil"],
        "climate_zones": ["arid", "tropical"],
        "temp_range_c": (18, 35),
        "rainfall_mm_range": (200, 500),
        "min_area_sqft": 1,
        "water_frequency": "Every 7–10 days, allow soil to fully dry between waterings.",
        "irrigation_type": ["drip", "hand_watering"],
        "sunlight_hours": 6,
        "growth_duration_days": 180,
        "spacing_cm": "40x40",
        "soil_ph_range": (6.0, 7.5),
    },

    "Fenugreek": {
        "growing_methods": ["vertical", "container", "open_field"],
        "soil_types": ["loamy", "sandy", "black_soil"],
        "climate_zones": ["subtropical", "arid"],
        "temp_range_c": (15, 27),
        "rainfall_mm_range": (350, 700),
        "min_area_sqft": 0.2,
        "water_frequency": "Every 2 days, light watering.",
        "irrigation_type": ["drip", "wick", "hand_watering"],
        "sunlight_hours": 5,
        "growth_duration_days": 30,
        "spacing_cm": "10x10",
        "soil_ph_range": (6.0, 7.5),
    },
}


def get_crop(name):
    return CROPS.get(name)


def all_crop_names():
    return list(CROPS.keys())