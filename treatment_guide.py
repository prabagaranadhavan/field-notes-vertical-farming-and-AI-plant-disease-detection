"""
Treatment and maintenance guide, keyed by the exact class names saved
in model/class_names.json.

For diseased classes: chemical control, organic/natural control, and
cultural (non-spray) practices.
For healthy classes: general maintenance only.

This is general agricultural-extension–style guidance (active-ingredient
classes, not specific brand products). Always follow the product label
and check with a local agricultural extension office for anything
region-specific or regulated.
"""

TREATMENTS = {

    "Apple_Black_Rot": {
        "chemical": "Captan or myclobutanil fungicide, applied from bud break through summer per label interval.",
        "organic": "Copper-based fungicide spray; remove mummified fruit and cankers by hand.",
        "care": "Prune out dead or diseased wood, clear fallen fruit and leaves, and improve air circulation through the canopy."
    },
    "Apple_Cedar_Apple_Rust": {
        "chemical": "Myclobutanil or propiconazole fungicide, starting at the pink bud stage.",
        "organic": "Sulfur-based fungicide spray; remove nearby juniper or cedar hosts where possible.",
        "care": "Rake and destroy fallen leaves each autumn, and avoid overhead irrigation."
    },
    "Apple_Healthy": {
        "care": "Prune yearly for airflow, feed with a balanced fertilizer, water at the base rather than overhead, and check regularly for early pest or disease signs."
    },
    "Apple_Scab": {
        "chemical": "Captan, mancozeb, or myclobutanil fungicide from green tip through petal fall.",
        "organic": "Sulfur or copper-based fungicide; consider scab-resistant varieties for future plantings.",
        "care": "Rake and dispose of fallen leaves in autumn, and prune to open up the canopy."
    },

    "Cherry_Healthy": {
        "care": "Prune for an open canopy, avoid overhead watering, and monitor for early signs of powdery mildew during humid periods."
    },
    "Cherry_Powdery_Mildew": {
        "chemical": "Sulfur or myclobutanil fungicide, reapplied per label through the growing season.",
        "organic": "Neem oil or potassium bicarbonate spray; diluted milk spray is a common home remedy.",
        "care": "Prune for airflow, avoid excess nitrogen fertilizer, and water at soil level, not overhead."
    },

    "Corn_Common_Rust": {
        "chemical": "Azoxystrobin or propiconazole fungicide if infection is severe or spreading fast.",
        "organic": "Usually unnecessary at low levels; prioritize rust-resistant hybrids next season.",
        "care": "Rotate crops, remove volunteer corn plants, and avoid overly dense planting."
    },
    "Corn_Healthy": {
        "care": "Rotate crops each season, maintain even spacing for airflow, and scout regularly during humid weather."
    },
    "Corn_Northern_Leaf_Blight": {
        "chemical": "Azoxystrobin or propiconazole fungicide applied at first sign of lesions.",
        "organic": "Crop rotation and resistant hybrids are the main non-chemical levers here.",
        "care": "Till under crop debris after harvest and rotate away from corn for at least one season."
    },

    "Grape_Black_Rot": {
        "chemical": "Mancozeb or myclobutanil fungicide from early shoot growth through veraison.",
        "organic": "Copper-based fungicide; remove and destroy mummified berries.",
        "care": "Prune for an open canopy and remove infected canes and fruit promptly."
    },
    "Grape_Healthy": {
        "care": "Prune annually for airflow, remove fallen fruit and leaves, and avoid overhead irrigation."
    },

    "Peach_Bacterial_Spot": {
        "chemical": "Copper-based bactericide, applied during dormancy and early growth (fungicides won't help — this is bacterial).",
        "organic": "Copper spray is also the standard organic-approved option here.",
        "care": "Avoid overhead irrigation, prune for airflow, and avoid excess nitrogen fertilizer."
    },
    "Peach_Healthy": {
        "care": "Prune for an open center, water at the base, and watch for early leaf-spotting during wet weather."
    },

    "Pepper_Bacterial_Spot": {
        "chemical": "Copper-based bactericide, often tank-mixed with mancozeb to slow resistance buildup.",
        "organic": "Copper spray, resistant varieties, and crop rotation.",
        "care": "Use drip irrigation instead of overhead watering, avoid working in wet fields, and remove infected debris."
    },
    "Pepper_Healthy": {
        "care": "Water at the base, space plants for airflow, and rotate planting location each season."
    },

    "Potato_Early_Blight": {
        "chemical": "Chlorothalonil or azoxystrobin fungicide at first sign of lesions.",
        "organic": "Copper-based fungicide or neem oil; rotate crops away from potatoes/tomatoes.",
        "care": "Space plants adequately, avoid overhead watering, and remove infected foliage."
    },
    "Potato_Healthy": {
        "care": "Hill soil around stems, water consistently at the base, and rotate crops each season."
    },
    "Potato_Late_Blight": {
        "chemical": "Chlorothalonil, mancozeb, or a metalaxyl-based fungicide — apply immediately and repeat per label, especially in wet weather. This disease can spread fast.",
        "organic": "Copper-based fungicide used preventively; remove and destroy infected plants right away.",
        "care": "Avoid overhead irrigation, ensure good drainage and airflow, and never compost infected material."
    },

    "Strawberry_Healthy": {
        "care": "Renovate beds after harvest, remove old foliage, and keep plants well spaced for airflow."
    },
    "Strawberry_Leaf_Scorch": {
        "chemical": "Captan or myclobutanil fungicide.",
        "organic": "Remove and destroy infected leaves; improve airflow around plants.",
        "care": "Renovate beds after harvest and avoid overhead watering."
    },

    "Tomato_Bacterial_Spot": {
        "chemical": "Copper-based bactericide, often mixed with mancozeb for resistance management.",
        "organic": "Copper spray, resistant varieties, and crop rotation.",
        "care": "Avoid overhead watering, don't handle plants while wet, and sanitize tools between plants."
    },
    "Tomato_Early_Blight": {
        "chemical": "Chlorothalonil or azoxystrobin fungicide at first symptoms, repeated every 7–10 days per label.",
        "organic": "Copper fungicide or neem oil; mulch around the base to reduce soil splash onto leaves.",
        "care": "Remove infected lower leaves, stake plants for airflow, and rotate crops each season."
    },
    "Tomato_Healthy": {
        "care": "Stake or cage for airflow, water at the base in the morning, and mulch to reduce soil splash."
    },
    "Tomato_Late_Blight": {
        "chemical": "Chlorothalonil, mancozeb, or a mefenoxam-containing fungicide — apply immediately and frequently in cool, wet weather.",
        "organic": "Copper-based fungicide used preventively; remove and destroy infected plants quickly to limit spread.",
        "care": "Avoid overhead irrigation, increase plant spacing, and never compost infected debris."
    },
    "Tomato_Leaf_Mold": {
        "chemical": "Chlorothalonil or mancozeb fungicide.",
        "organic": "Improve ventilation (common in greenhouse settings) and reduce humidity; copper spray as a backup.",
        "care": "Prune lower leaves, increase spacing, and avoid overhead watering."
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "chemical": "No direct chemical cure for the virus itself — insecticides such as imidacloprid target the whitefly that spreads it.",
        "organic": "Neem oil or insecticidal soap against whiteflies; reflective mulch can help deter them.",
        "care": "Use whitefly-resistant varieties, insect netting where practical, and remove/destroy infected plants promptly to protect the rest of the crop."
    },
}


def get_treatment(class_name):
    """Return the treatment dict for a class, or None if not found."""
    return TREATMENTS.get(class_name)


def is_healthy_class(class_name):
    return class_name.endswith("_Healthy")