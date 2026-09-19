"""
Bridges the Crop Recommender (crop_data.py) to the Disease Detector
(treatment_guide.py) — the two use different crop vocabularies, since
the detector's model was only ever trained on 8 species (Apple,
Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, Tomato).

CROP_TO_DETECTOR_SPECIES maps a crop_data.py crop name to the matching
detector species prefix, or None if the detector has no classes for
that crop at all — in which case the recommender page should not
offer a "check for disease" link for it, since the model would have
nothing meaningful to say.
"""

from treatment_guide import TREATMENTS


CROP_TO_DETECTOR_SPECIES = {
    "Spinach": None,
    "Lettuce": None,
    "Kale": None,
    "Basil": None,
    "Mint": None,
    "Coriander": None,
    "Strawberry": "Strawberry",
    "Tomato_Dwarf": "Tomato",
    "Chili_Pepper": "Pepper",
    "Cucumber": None,
    "Green_Beans": None,
    "Radish": None,
    "Okra": None,
    "Potato": "Potato",
    "Wheat": None,
    "Rice_Paddy": None,
    "Sugarcane": None,
    "Groundnut": None,
    "Aloe_Vera": None,
    "Fenugreek": None,
}


def get_detector_species(crop_name):
    """Returns the detector species prefix for a crop, or None if the
    disease detector has no coverage for it."""
    return CROP_TO_DETECTOR_SPECIES.get(crop_name)


def get_classes_for_species(species):
    """All treatment_guide.py class names belonging to a species
    prefix, e.g. 'Tomato' -> ['Tomato_Bacterial_Spot', ...,
    'Tomato_Healthy']. Derived from treatment_guide.py directly so the
    two files can't drift out of sync."""
    if not species:
        return []
    return [name for name in TREATMENTS if name.split("_")[0] == species]


def prediction_matches_species(predicted_class_name, expected_species):
    """True if a model prediction's species prefix matches the crop
    the user said they were checking on. Used to flag a likely
    species mismatch without altering the underlying prediction."""
    if not expected_species or not predicted_class_name:
        return True
    return predicted_class_name.split("_")[0] == expected_species