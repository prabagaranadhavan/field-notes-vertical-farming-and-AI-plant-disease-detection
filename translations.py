"""
Language layer for Field Notes.

Two languages: English (en) and Tamil (ta). Selection is stored in
st.session_state["lang"] so it persists across page navigation
(Streamlit multi-page apps share one session_state across pages).

Usage in any page:

    from translations import t, render_language_switcher

    render_language_switcher()   # call once, near the topbar
    st.markdown(t("home_title")) # pull a translated string

For dynamic content keyed by model class name (species / disease
names, treatment guide text), use `translate_class_name()` and
`translate_treatment()` below instead of raw dict lookups.
"""

import streamlit as st


DEFAULT_LANG = "en"


# ---------------------------------------------------------------------
# UI strings
# ---------------------------------------------------------------------

STRINGS = {

    "lang_name_en": {"en": "English", "ta": "English"},
    "lang_name_ta": {"en": "Tamil", "ta": "தமிழ்"},

    "brand_wordmark": {
        "en": "Field Notes",
        "ta": "கள குறிப்புகள்",
    },

    "nav_home": {"en": "Home", "ta": "முகப்பு"},
    "nav_species": {"en": "Species Index", "ta": "இன அட்டவணை"},
    "nav_analyser": {"en": "Analyser", "ta": "பகுப்பாய்வி"},

    # ---------------- Home page ----------------
    "home_kicker": {
        "en": "Field Notes · Leaf Diagnostics",
        "ta": "கள குறிப்புகள் · இலை நோயறிதல்",
    },
    "home_title_line1": {"en": "Read a leaf", "ta": "ஒரு இலையை"},
    "home_title_line2": {
        "en": "like a field guide.",
        "ta": "கள வழிகாட்டி போல் படியுங்கள்.",
    },
    "home_subtitle": {
        "en": (
            "Photograph a leaf and get an instant read on species and disease "
            "signatures — trained the way a plant pathologist builds intuition."
        ),
        "ta": (
            "ஒரு இலையைப் புகைப்படம் எடுத்து, அதன் இனம் மற்றும் நோய் அறிகுறிகளை "
            "உடனடியாக அறியுங்கள் — ஒரு தாவர நோயியல் நிபுணரின் அனுபவ முறையில் "
            "பயிற்சி பெற்றது."
        ),
    },
    "home_start_now": {"en": "Start now  →", "ta": "இப்போது தொடங்கு  →"},
    "home_browse_species": {
        "en": "browse the species index",
        "ta": "இன அட்டவணையை பார்வையிடவும்",
    },
    "home_diagram_chlorosis": {"en": "CHLOROSIS", "ta": "இலைப்பசுமையின்மை"},
    "home_diagram_necrotic": {"en": "NECROTIC MARGIN", "ta": "விளிம்பு சிதைவு"},
    "home_diagram_leafbase": {"en": "LEAF BASE", "ta": "இலை அடிப்பகுதி"},

    # ---------------- Analyser page ----------------
    "analyser_kicker": {
        "en": "Field Notes · Specimen Intake",
        "ta": "கள குறிப்புகள் · மாதிரி பதிவு",
    },
    "analyser_title": {"en": "The analyser", "ta": "பகுப்பாய்வி"},
    "analyser_subtitle": {
        "en": (
            "Upload a leaf photo — a real one, plain background, natural light "
            "works best. Clipart or transparent cut-outs are handled, but a "
            "genuine photograph gives the most reliable read."
        ),
        "ta": (
            "ஒரு இலைப் புகைப்படத்தை பதிவேற்றவும் — உண்மையான புகைப்படம், எளிய "
            "பின்னணி, இயற்கை வெளிச்சம் சிறந்த முடிவைத் தரும். கிளிப்ஆர்ட் அல்லது "
            "வெளிப்படையான படங்களும் ஏற்கப்படும், ஆனால் உண்மையான புகைப்படமே "
            "மிகச் சரியான முடிவைத் தரும்."
        ),
    },
    "analyser_no_model": {
        "en": "No trained model found. Run train_model.py first.",
        "ta": "பயிற்சி பெற்ற மாடல் கிடைக்கவில்லை. முதலில் train_model.py-ஐ இயக்கவும்.",
    },
    "analyser_uploader_label": {
        "en": "Upload a leaf image",
        "ta": "ஒரு இலைப் படத்தை பதிவேற்றவும்",
    },
    "analyser_spinner": {
        "en": "Cross-referencing specimen…",
        "ta": "மாதிரியை ஒப்பிட்டு சரிபார்க்கிறது…",
    },
    "analyser_best_match": {"en": "Best match", "ta": "சிறந்த பொருத்தம்"},
    "analyser_specimen_readout": {
        "en": "Specimen readout",
        "ta": "மாதிரி முடிவு",
    },
    "analyser_recommended_care": {
        "en": "Recommended care",
        "ta": "பரிந்துரைக்கப்பட்ட பராமரிப்பு",
    },
    "analyser_model_mismatch": {
        "en": (
            "Model output size ({pred}) doesn't match the number of saved "
            "class names ({names})."
        ),
        "ta": (
            "மாடலின் வெளியீட்டு அளவு ({pred}) சேமிக்கப்பட்ட வகைப் பெயர்களின் "
            "எண்ணிக்கையுடன் ({names}) பொருந்தவில்லை."
        ),
    },

    # ---------------- Care card headings ----------------
    "care_maintenance": {"en": "Maintenance", "ta": "பராமரிப்பு"},
    "care_chemical": {"en": "Chemical control", "ta": "வேதியியல் கட்டுப்பாடு"},
    "care_organic": {"en": "Organic control", "ta": "இயற்கை கட்டுப்பாடு"},
    "care_cultural": {"en": "Cultural practices", "ta": "பயிர் பராமரிப்பு முறைகள்"},
    "care_disclaimer": {
        "en": (
            "General guidance only — always follow the product label and "
            "check with a local agricultural extension office for anything "
            "specific to your region or crop."
        ),
        "ta": (
            "இது பொதுவான வழிகாட்டுதல் மட்டுமே — எப்போதும் தயாரிப்பு லேபிளைப் "
            "பின்பற்றவும், உங்கள் பகுதி அல்லது பயிருக்கு ஏற்ப உள்ளூர் வேளாண் "
            "விரிவாக்க அலுவலகத்தை அணுகவும்."
        ),
    },

    # ---------------- Species Index page ----------------
    "species_kicker": {
        "en": "Field Notes · Reference Catalog",
        "ta": "கள குறிப்புகள் · குறிப்பு பட்டியல்",
    },
    "species_title": {"en": "Species index", "ta": "இன அட்டவணை"},
    "species_subtitle": {
        "en": (
            "One reference specimen from each class the analyser was trained "
            "on — a quick way to see the visual range it learns to tell apart."
        ),
        "ta": (
            "பகுப்பாய்வி பயிற்சி பெற்ற ஒவ்வொரு வகையிலிருந்தும் ஒரு குறிப்பு "
            "மாதிரி — அது வேறுபடுத்த கற்றுக்கொண்ட காட்சி வரம்பை விரைவாகப் "
            "பார்க்க ஒரு வழி."
        ),
    },
    "species_no_data": {
        "en": "No training data found at",
        "ta": "பயிற்சி தரவு இங்கு கிடைக்கவில்லை:",
    },
    "species_unreadable": {"en": "unreadable", "ta": "படிக்க முடியவில்லை"},
    "species_no_image": {"en": "no image", "ta": "படம் இல்லை"},

    # ---------------- Crop Recommender page ----------------
    "nav_recommender": {"en": "Crop Recommender", "ta": "பயிர் பரிந்துரை"},
    "reco_kicker": {
        "en": "Field Notes · Planting Plan",
        "ta": "கள குறிப்புகள் · நடவு திட்டம்",
    },
    "reco_title": {"en": "Crop recommender", "ta": "பயிர் பரிந்துரையாளர்"},
    "reco_subtitle": {
        "en": (
            "Tell us about your space and soil, and we'll suggest crops "
            "that are a strict fit — along with a care plan for each."
        ),
        "ta": (
            "உங்கள் இடம் மற்றும் மண் பற்றி எங்களிடம் கூறுங்கள் — அதற்கு "
            "பொருத்தமான பயிர்களை பரிந்துரைப்போம், ஒவ்வொன்றுக்கும் ஒரு "
            "பராமரிப்பு திட்டத்துடன்."
        ),
    },
    "reco_form_setup": {"en": "Growing setup", "ta": "வளர்ப்பு முறை"},
    "reco_form_soil": {"en": "Soil type", "ta": "மண் வகை"},
    "reco_form_climate": {"en": "Climate zone", "ta": "காலநிலை மண்டலம்"},
    "reco_locate_button": {"en": "📍 Detect my location", "ta": "📍 என் இருப்பிடத்தைக் கண்டறி"},
    "reco_locate_detecting": {"en": "Detecting…", "ta": "கண்டறிகிறது…"},
    "reco_locate_denied": {
        "en": "Couldn't detect location — please select climate manually.",
        "ta": "இருப்பிடத்தைக் கண்டறிய முடியவில்லை — காலநிலையை கைமுறையாக தேர்ந்தெடுக்கவும்.",
    },
    "reco_locate_detected": {
        "en": "Detected: {place} — climate set to {zone}",
        "ta": "கண்டறியப்பட்டது: {place} — காலநிலை {zone} ஆக அமைக்கப்பட்டது",
    },
    "reco_locate_detected_no_zone": {
        "en": "Detected: {place} — couldn't determine a climate zone, please select manually.",
        "ta": "கண்டறியப்பட்டது: {place} — காலநிலை மண்டலத்தை தீர்மானிக்க முடியவில்லை, கைமுறையாக தேர்ந்தெடுக்கவும்.",
    },
    "reco_form_area": {"en": "Available area (sq ft)", "ta": "கிடைக்கும் பரப்பளவு (சதுர அடி)"},
    "reco_submit": {"en": "Find suitable crops", "ta": "பொருத்தமான பயிர்களைக் கண்டறி"},

    "setup_vertical": {"en": "Vertical", "ta": "செங்குத்து"},
    "setup_container": {"en": "Container", "ta": "தொட்டி"},
    "setup_open_field": {"en": "Open field", "ta": "திறந்த வயல்"},

    "soil_sandy": {"en": "Sandy", "ta": "மணல் மண்"},
    "soil_loamy": {"en": "Loamy", "ta": "வண்டல் மண்"},
    "soil_clay": {"en": "Clay", "ta": "களிமண்"},
    "soil_silty": {"en": "Silty", "ta": "வண்டல் படிவு மண்"},
    "soil_red_soil": {"en": "Red soil", "ta": "செம்மண்"},
    "soil_black_soil": {"en": "Black soil", "ta": "கரிசல் மண்"},
    "soil_peaty": {"en": "Peaty", "ta": "பீட் மண்"},

    "climate_tropical": {"en": "Tropical", "ta": "வெப்பமண்டலம்"},
    "climate_subtropical": {"en": "Subtropical", "ta": "துணை வெப்பமண்டலம்"},
    "climate_temperate": {"en": "Temperate", "ta": "மிதவெப்பமண்டலம்"},
    "climate_arid": {"en": "Arid", "ta": "வறண்ட பகுதி"},

    "irrigation_drip": {"en": "Drip irrigation", "ta": "சொட்டு நீர்ப்பாசனம்"},
    "irrigation_wick": {"en": "Wick irrigation", "ta": "திரி நீர்ப்பாசனம்"},
    "irrigation_hydroponic_nft": {"en": "Hydroponic (NFT)", "ta": "நீரியல் (NFT)"},
    "irrigation_sprinkler": {"en": "Sprinkler irrigation", "ta": "தெளிப்பு நீர்ப்பாசனம்"},
    "irrigation_flood": {"en": "Flood irrigation", "ta": "வெள்ள நீர்ப்பாசனம்"},
    "irrigation_hand_watering": {"en": "Hand watering", "ta": "கை மூலம் நீர் ஊற்றுதல்"},

    "reco_results_kicker": {"en": "Suitable crops", "ta": "பொருத்தமான பயிர்கள்"},
    "reco_no_results_title": {
        "en": "No crop fully matches these conditions.",
        "ta": "இந்த நிலைமைகளுக்கு முழுமையாகப் பொருந்தும் பயிர் எதுவும் இல்லை.",
    },
    "reco_no_results_body": {
        "en": (
            "Try a different soil type, climate zone, growing setup, or a "
            "larger area — the list only shows crops that satisfy every "
            "condition you selected."
        ),
        "ta": (
            "வேறு மண் வகை, காலநிலை மண்டலம், வளர்ப்பு முறை, அல்லது அதிக "
            "பரப்பளவை முயற்சிக்கவும் — நீங்கள் தேர்ந்தெடுத்த அனைத்து "
            "நிபந்தனைகளையும் பூர்த்தி செய்யும் பயிர்கள் மட்டுமே இந்த "
            "பட்டியலில் காட்டப்படும்."
        ),
    },
    "reco_care_water": {"en": "Watering", "ta": "நீர்ப்பாசனம்"},
    "reco_care_irrigation": {"en": "Suggested irrigation", "ta": "பரிந்துரைக்கப்பட்ட நீர்ப்பாசனம்"},
    "reco_care_sunlight": {"en": "Sunlight", "ta": "சூரிய ஒளி"},
    "reco_care_spacing": {"en": "Spacing", "ta": "இடைவெளி"},
    "reco_care_duration": {"en": "Time to harvest", "ta": "அறுவடைக்கான காலம்"},
    "reco_care_ph": {"en": "Soil pH range", "ta": "மண் pH வரம்பு"},

    "reco_check_disease_button": {
        "en": "🔬 Check this crop for disease",
        "ta": "🔬 இந்த பயிரில் நோயை சரிபார்க்கவும்",
    },
    "reco_disease_not_available": {
        "en": "Disease detection isn't available yet for this crop.",
        "ta": "இந்த பயிருக்கு நோய் கண்டறிதல் இன்னும் கிடைக்கவில்லை.",
    },
    "analyser_context_banner": {
        "en": "Checking on: {crop} (from your crop recommendations)",
        "ta": "சரிபார்க்கப்படுவது: {crop} (உங்கள் பயிர் பரிந்துரையிலிருந்து)",
    },
    "analyser_context_clear": {"en": "✕ Clear", "ta": "✕ அழி"},
    "analyser_species_mismatch": {
        "en": (
            "This result doesn't match {crop} — double-check the photo, "
            "or the species may be different."
        ),
        "ta": (
            "இந்த முடிவு {crop}-உடன் பொருந்தவில்லை — புகைப்படத்தை மீண்டும் "
            "சரிபார்க்கவும், அல்லது இனம் வேறுபட்டதாக இருக்கலாம்."
        ),
    },
    "reco_sunlight_hours": {"en": "{hours}+ hours daily", "ta": "தினமும் {hours}+ மணி நேரம்"},
    "reco_duration_days": {"en": "{days} days", "ta": "{days} நாட்கள்"},

    # ---------------- Care Timeline ----------------
    "timeline_expander_label": {"en": "View care timeline", "ta": "பராமரிப்பு காலவரிசையைப் பார்க்க"},
    "timeline_day_range": {"en": "Days {start}–{end}", "ta": "நாட்கள் {start}–{end}"},

    "timeline_stage_germination": {"en": "Germination & Establishment", "ta": "முளைப்பு & நிலைநிறுத்தல்"},
    "timeline_stage_vegetative": {"en": "Vegetative Growth", "ta": "தழை வளர்ச்சி"},
    "timeline_stage_pre_harvest": {"en": "Pre-Harvest", "ta": "அறுவடைக்கு முந்தைய நிலை"},
    "timeline_stage_harvest_regrowth": {"en": "Harvest & Regrowth", "ta": "அறுவடை & மீள் வளர்ச்சி"},
    "timeline_stage_flowering_watch": {"en": "Flowering Watch", "ta": "பூக்கும் கண்காணிப்பு"},
    "timeline_stage_continuous_harvest": {"en": "Continuous Harvest", "ta": "தொடர் அறுவடை"},
    "timeline_stage_transplant": {"en": "Germination & Transplant", "ta": "முளைப்பு & நடவு மாற்றம்"},
    "timeline_stage_flowering": {"en": "Flowering", "ta": "பூக்கும் நிலை"},
    "timeline_stage_fruit_development": {"en": "Fruit Development", "ta": "காய் வளர்ச்சி"},
    "timeline_stage_harvest": {"en": "Harvest", "ta": "அறுவடை"},
    "timeline_stage_bulking": {"en": "Bulking / Tuber Formation", "ta": "கிழங்கு உருவாக்கம்"},
    "timeline_stage_sowing": {"en": "Sowing & Establishment", "ta": "விதைப்பு & நிலைநிறுத்தல்"},
    "timeline_stage_tillering": {"en": "Vegetative / Tillering", "ta": "தழை வளர்ச்சி / கிளைத்தல்"},
    "timeline_stage_reproductive": {"en": "Flowering / Reproductive", "ta": "பூக்கும் / இனப்பெருக்க நிலை"},
    "timeline_stage_yield_fill": {"en": "Grain / Yield Fill", "ta": "தானிய / மகசூல் நிரப்பு நிலை"},
    "timeline_stage_establishment": {"en": "Establishment", "ta": "நிலைநிறுத்தல்"},
    "timeline_stage_fruiting_onset": {"en": "Flowering & Fruiting Onset", "ta": "பூக்கும் & காய்க்கும் தொடக்கம்"},
    "timeline_stage_ongoing_harvest": {"en": "Ongoing Harvest & Maintenance", "ta": "தொடர் அறுவடை & பராமரிப்பு"},

    "timeline_action_pest_monitor": {
        "en": "Monitor leaves and stems weekly for early pest or disease signs — use the Disease Detector if anything looks off.",
        "ta": "இலைகள் மற்றும் தண்டுகளை வாரந்தோறும் பூச்சி அல்லது நோய் அறிகுறிகளுக்காக கண்காணிக்கவும் — ஏதேனும் சந்தேகமாக இருந்தால் நோய் கண்டறிதலைப் பயன்படுத்தவும்.",
    },
    "timeline_action_mulch": {
        "en": "Apply a light mulch layer to retain soil moisture and reduce weed growth.",
        "ta": "மண் ஈரப்பதத்தை தக்கவைக்கவும் களை வளர்ச்சியை குறைக்கவும் ஒரு மெல்லிய மல்ச் அடுக்கை இடவும்.",
    },
    "timeline_action_check_drainage": {
        "en": "Check that water drains well and the growing area isn't waterlogged.",
        "ta": "நீர் நன்றாக வடிகிறதா என்றும் வளர்ப்பு பகுதி தண்ணீர் தேங்காமல் இருக்கிறதா என்றும் சரிபார்க்கவும்.",
    },
    "timeline_action_remove_weeds": {
        "en": "Remove weeds around the base to reduce competition for nutrients and water.",
        "ta": "ஊட்டச்சத்து மற்றும் நீருக்கான போட்டியை குறைக்க அடிப்பகுதியைச் சுற்றியுள்ள களைகளை அகற்றவும்.",
    },

    "timeline_action_leafy_moist_soil": {
        "en": "Keep soil consistently moist to support even germination.",
        "ta": "சீரான முளைப்பிற்கு மண்ணை தொடர்ந்து ஈரமாக வைத்திருக்கவும்.",
    },
    "timeline_action_leafy_partial_shade": {
        "en": "Provide partial shade if temperatures are high during this stage.",
        "ta": "இந்த நிலையில் வெப்பநிலை அதிகமாக இருந்தால் பகுதி நிழல் அளிக்கவும்.",
    },
    "timeline_action_leafy_fertilize": {
        "en": "Apply a balanced, nitrogen-rich fertilizer once true leaves appear.",
        "ta": "உண்மையான இலைகள் தோன்றியவுடன் சமநிலையான, நைட்ரஜன் நிறைந்த உரத்தை இடவும்.",
    },
    "timeline_action_leafy_reduce_nitrogen": {
        "en": "Reduce nitrogen fertilizer as harvest approaches to avoid excess bitterness.",
        "ta": "அதிக கசப்பைத் தவிர்க்க அறுவடை நெருங்கும்போது நைட்ரஜன் உரத்தைக் குறைக்கவும்.",
    },
    "timeline_action_leafy_thin": {
        "en": "Thin crowded plants to improve airflow and leaf size.",
        "ta": "காற்றோட்டத்தையும் இலை அளவையும் மேம்படுத்த நெரிசலான செடிகளை நேர்த்தி செய்யவும்.",
    },
    "timeline_action_leafy_harvest_outer": {
        "en": "Harvest outer leaves first to allow continued regrowth from the center.",
        "ta": "மையத்திலிருந்து தொடர்ந்து வளர அனுமதிக்க முதலில் வெளிப்புற இலைகளை அறுவடை செய்யவும்.",
    },
    "timeline_action_leafy_refresh_soil": {
        "en": "After a full harvest, refresh the soil with compost before replanting.",
        "ta": "முழு அறுவடைக்குப் பிறகு, மீண்டும் நடுவதற்கு முன் மண்ணை உரத்துடன் புதுப்பிக்கவும்.",
    },

    "timeline_action_herb_light_moisture": {
        "en": "Keep soil lightly moist; avoid waterlogging, which herbs are sensitive to.",
        "ta": "மண்ணை லேசாக ஈரமாக வைத்திருக்கவும்; மூலிகைகள் உணர்திறன் கொண்டவை என்பதால் தண்ணீர் தேங்குவதைத் தவிர்க்கவும்.",
    },
    "timeline_action_herb_pinch": {
        "en": "Pinch growing tips regularly to encourage bushier growth.",
        "ta": "செழிப்பான வளர்ச்சியை ஊக்குவிக்க வளரும் நுனிகளை தொடர்ந்து கிள்ளவும்.",
    },
    "timeline_action_herb_remove_buds": {
        "en": "Remove flower buds promptly — flowering reduces leaf flavor and slows new growth.",
        "ta": "பூ மொட்டுகளை உடனடியாக அகற்றவும் — பூத்தல் இலை சுவையைக் குறைத்து புதிய வளர்ச்சியை மெதுவாக்கும்.",
    },
    "timeline_action_herb_harvest_third": {
        "en": "Harvest a third of the plant at a time, never more, to keep it productive.",
        "ta": "செடியை உற்பத்தித்திறனுடன் வைத்திருக்க ஒரு முறை மூன்றில் ஒரு பங்கிற்கு மேல் அறுவடை செய்ய வேண்டாம்.",
    },
    "timeline_action_herb_feed_light": {
        "en": "Feed lightly every few weeks to sustain continuous cutting.",
        "ta": "தொடர்ந்து வெட்டுவதை நிலைநிறுத்த சில வாரங்களுக்கு ஒருமுறை லேசாக உரமிடவும்.",
    },

    "timeline_action_fruit_harden_off": {
        "en": "Harden off seedlings gradually before transplanting outdoors or into final containers.",
        "ta": "வெளியே அல்லது இறுதி தொட்டியில் நடவு செய்வதற்கு முன் நாற்றுகளை படிப்படியாக பழக்கப்படுத்தவும்.",
    },
    "timeline_action_fruit_stake_early": {
        "en": "Stake or cage the plant early, before it becomes top-heavy.",
        "ta": "செடி மேல்பாரமாகும் முன்பே கட்டு அல்லது கூண்டு வைக்கவும்.",
    },
    "timeline_action_fruit_consistent_water": {
        "en": "Ensure consistent watering — irregular watering at this stage causes flower drop.",
        "ta": "சீரான நீர்ப்பாசனத்தை உறுதி செய்யவும் — இந்த நிலையில் ஒழுங்கற்ற நீர்ப்பாசனம் பூக்கள் உதிர காரணமாகும்.",
    },
    "timeline_action_fruit_pollinate": {
        "en": "Gently shake or tap flowering stems midday to help pollination indoors.",
        "ta": "உள்ளே மகரந்தச் சேர்க்கைக்கு உதவ மதிய நேரத்தில் பூக்கும் தண்டுகளை மெதுவாக அசைக்கவும்.",
    },
    "timeline_action_fruit_potassium": {
        "en": "Apply a potassium-rich fertilizer to support fruit development.",
        "ta": "காய் வளர்ச்சிக்கு ஆதரவாக பொட்டாசியம் நிறைந்த உரத்தை இடவும்.",
    },
    "timeline_action_fruit_harvest_regularly": {
        "en": "Harvest regularly — leaving ripe fruit on the plant slows new fruit set.",
        "ta": "தொடர்ந்து அறுவடை செய்யவும் — பழுத்த காயை செடியில் விட்டால் புதிய காய்ப்பு மெதுவாகும்.",
    },
    "timeline_action_fruit_support_branches": {
        "en": "Support heavy branches to prevent breakage under fruit weight.",
        "ta": "காயின் எடையால் முறியாமல் இருக்க கனமான கிளைகளை தாங்கவும்.",
    },

    "timeline_action_root_loose_soil": {
        "en": "Keep soil loose and stone-free for straight root development.",
        "ta": "நேரான வேர் வளர்ச்சிக்கு மண்ணை தளர்வாகவும் கல் இல்லாமலும் வைத்திருக்கவும்.",
    },
    "timeline_action_root_gentle_water": {
        "en": "Water gently to avoid disturbing seeds/seedlings.",
        "ta": "விதைகள்/நாற்றுகளை பாதிக்காமல் இருக்க மெதுவாக நீர் ஊற்றவும்.",
    },
    "timeline_action_root_thin": {
        "en": "Thin seedlings to the recommended spacing to give roots room to bulk up.",
        "ta": "வேர்கள் வளர இடம் கொடுக்க நாற்றுகளை பரிந்துரைக்கப்பட்ட இடைவெளிக்கு நேர்த்தி செய்யவும்.",
    },
    "timeline_action_root_hill_soil": {
        "en": "Hill soil around the base to protect developing tubers from sunlight.",
        "ta": "வளரும் கிழங்குகளை சூரிய ஒளியிலிருந்து பாதுகாக்க அடிப்பகுதியைச் சுற்றி மண் மேடு அமைக்கவும்.",
    },
    "timeline_action_root_even_water": {
        "en": "Maintain even watering — inconsistent watering causes cracking or misshapen roots.",
        "ta": "சீரான நீர்ப்பாசனத்தை பராமரிக்கவும் — ஒழுங்கற்ற நீர்ப்பாசனம் வேர்கள் வெடிக்க அல்லது சிதைவடைய காரணமாகும்.",
    },
    "timeline_action_root_harvest_promptly": {
        "en": "Harvest promptly once mature — leaving roots in the ground too long affects texture.",
        "ta": "முதிர்ந்தவுடன் உடனடியாக அறுவடை செய்யவும் — வேர்களை தரையில் அதிக நேரம் விட்டால் தரம் பாதிக்கப்படும்.",
    },
    "timeline_action_root_loosen_soil": {
        "en": "Loosen soil carefully before pulling to avoid damaging the roots.",
        "ta": "வேர்களை சேதப்படுத்தாமல் இருக்க பிடுங்குவதற்கு முன் மண்ணை கவனமாக தளர்த்தவும்.",
    },

    "timeline_action_field_seed_contact": {
        "en": "Ensure good seed-to-soil contact and even sowing depth across the field.",
        "ta": "வயல் முழுவதும் நல்ல விதை-மண் தொடர்பையும் சீரான விதைப்பு ஆழத்தையும் உறுதி செய்யவும்.",
    },
    "timeline_action_field_topdress": {
        "en": "Apply the first top-dressing of fertilizer once seedlings are established.",
        "ta": "நாற்றுகள் நிலைநிறுத்தப்பட்டவுடன் முதல் மேல்-உரமிடலை செய்யவும்.",
    },
    "timeline_action_field_water_stress": {
        "en": "This stage is most sensitive to water stress — irrigate reliably through flowering.",
        "ta": "இந்த நிலை நீர் பற்றாக்குறைக்கு மிகவும் உணர்திறன் கொண்டது — பூக்கும் காலம் முழுவதும் நம்பகமாக நீர்ப்பாசனம் செய்யவும்.",
    },
    "timeline_action_field_potassium": {
        "en": "Reduce nitrogen application; focus on potassium to support grain/yield fill.",
        "ta": "நைட்ரஜன் பயன்பாட்டைக் குறைக்கவும்; தானிய/மகசூல் நிரப்புதலுக்கு பொட்டாசியத்தில் கவனம் செலுத்தவும்.",
    },
    "timeline_action_field_lodging": {
        "en": "Watch for lodging (plants falling over) in windy or heavy-rain conditions.",
        "ta": "காற்று அல்லது கனமழை நிலைமைகளில் செடிகள் விழுவதை (லாட்ஜிங்) கவனிக்கவும்.",
    },
    "timeline_action_field_harvest_timing": {
        "en": "Time harvest to grain/crop moisture recommendations to avoid losses.",
        "ta": "இழப்புகளைத் தவிர்க்க தானிய/பயிர் ஈரப்பத பரிந்துரைகளுக்கு ஏற்ப அறுவடை நேரத்தை நிர்ணயிக்கவும்.",
    },
    "timeline_action_field_clear_residue": {
        "en": "Clear field residue after harvest to reduce pest and disease carryover.",
        "ta": "பூச்சி மற்றும் நோய் தொடர்வதை குறைக்க அறுவடைக்குப் பிறகு வயல் எச்சங்களை அகற்றவும்.",
    },

    "timeline_action_perennial_deep_water": {
        "en": "Water deeply but infrequently to encourage strong root establishment.",
        "ta": "வலுவான வேர் நிலைநிறுத்தலை ஊக்குவிக்க ஆழமாக ஆனால் அரிதாக நீர் ஊற்றவும்.",
    },
    "timeline_action_perennial_remove_runners": {
        "en": "Remove runners/side-shoots not needed for propagation to focus energy on the main plant.",
        "ta": "முக்கிய செடியில் ஆற்றலை குவிக்க பெருக்கத்திற்கு தேவையில்லாத ரன்னர்கள்/பக்கக் கிளைகளை அகற்றவும்.",
    },
    "timeline_action_perennial_support_stems": {
        "en": "Support fruiting stems off the soil to prevent rot.",
        "ta": "அழுகலைத் தடுக்க காய்க்கும் தண்டுகளை மண்ணிலிருந்து தூக்கி ஆதரவு அளிக்கவும்.",
    },
    "timeline_action_perennial_harvest_peak": {
        "en": "Harvest regularly at peak ripeness.",
        "ta": "உச்ச பழுத்த நிலையில் தொடர்ந்து அறுவடை செய்யவும்.",
    },
    "timeline_action_perennial_renovate": {
        "en": "After the main harvest, renovate the bed — remove old growth to encourage the next cycle.",
        "ta": "முக்கிய அறுவடைக்குப் பிறகு, தோட்டத்தை புதுப்பிக்கவும் — அடுத்த சுழற்சியை ஊக்குவிக்க பழைய வளர்ச்சியை அகற்றவும்.",
    },
}


# ---------------------------------------------------------------------
# Species / class-name translations
#
# Keyed by the exact class names in model/class_names.json (same keys
# treatment_guide.py uses). Only the plant/disease name needs
# translating for display — chemical/active-ingredient names are kept
# in English/Latin script in the Tamil treatment text too, since
# that's how they appear on product labels and in extension material.
# ---------------------------------------------------------------------

CLASS_NAMES_TA = {
    "Apple_Black_Rot": "ஆப்பிள் கரும் அழுகல்",
    "Apple_Cedar_Apple_Rust": "ஆப்பிள் சிடார்-ஆப்பிள் துரு நோய்",
    "Apple_Healthy": "ஆப்பிள் ஆரோக்கியமானது",
    "Apple_Scab": "ஆப்பிள் சொறி நோய்",
    "Cherry_Healthy": "செர்ரி ஆரோக்கியமானது",
    "Cherry_Powdery_Mildew": "செர்ரி பொடி பூஞ்சை நோய்",
    "Corn_Common_Rust": "சோளம் பொதுவான துரு நோய்",
    "Corn_Healthy": "சோளம் ஆரோக்கியமானது",
    "Corn_Northern_Leaf_Blight": "சோளம் வட இலை கருகல்",
    "Grape_Black_Rot": "திராட்சை கரும் அழுகல்",
    "Grape_Healthy": "திராட்சை ஆரோக்கியமானது",
    "Peach_Bacterial_Spot": "பீச் பாக்டீரியா புள்ளி நோய்",
    "Peach_Healthy": "பீச் ஆரோக்கியமானது",
    "Pepper_Bacterial_Spot": "மிளகாய் பாக்டீரியா புள்ளி நோய்",
    "Pepper_Healthy": "மிளகாய் ஆரோக்கியமானது",
    "Potato_Early_Blight": "உருளைக்கிழங்கு முன்கூட்டிய கருகல்",
    "Potato_Healthy": "உருளைக்கிழங்கு ஆரோக்கியமானது",
    "Potato_Late_Blight": "உருளைக்கிழங்கு பிந்திய கருகல்",
    "Strawberry_Healthy": "ஸ்ட்ராபெரி ஆரோக்கியமானது",
    "Strawberry_Leaf_Scorch": "ஸ்ட்ராபெரி இலை தீக்காயம்",
    "Tomato_Bacterial_Spot": "தக்காளி பாக்டீரியா புள்ளி நோய்",
    "Tomato_Early_Blight": "தக்காளி முன்கூட்டிய கருகல்",
    "Tomato_Healthy": "தக்காளி ஆரோக்கியமானது",
    "Tomato_Late_Blight": "தக்காளி பிந்திய கருகல்",
    "Tomato_Leaf_Mold": "தக்காளி இலை பூஞ்சை",
    "Tomato_Yellow_Leaf_Curl_Virus": "தக்காளி மஞ்சள் இலை சுருள் வைரஸ்",
}


TREATMENTS_TA = {
    "Apple_Black_Rot": {
        "chemical": "Captan அல்லது myclobutanil பூஞ்சைக்கொல்லி, மொட்டு விரியும் காலத்திலிருந்து கோடை வரை லேபிள் அறிவுறுத்தல்படி தெளிக்கவும்.",
        "organic": "காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லி தெளிப்பு; பாதிக்கப்பட்ட பழங்களையும் புண்களையும் கையால் அகற்றவும்.",
        "care": "இறந்த அல்லது நோய்வாய்ப்பட்ட கிளைகளை கத்தரிக்கவும், விழுந்த பழங்கள் மற்றும் இலைகளை அகற்றவும், தழையினூடே காற்றோட்டத்தை மேம்படுத்தவும்.",
    },
    "Apple_Cedar_Apple_Rust": {
        "chemical": "Myclobutanil அல்லது propiconazole பூஞ்சைக்கொல்லி, இளஞ்சிவப்பு மொட்டு நிலையிலிருந்து தொடங்கவும்.",
        "organic": "சல்பர் அடிப்படையிலான பூஞ்சைக்கொல்லி தெளிப்பு; அருகிலுள்ள ஜூனிபர் அல்லது சிடார் மரங்களை முடிந்தால் அகற்றவும்.",
        "care": "ஒவ்வொரு இலையுதிர் காலத்திலும் விழுந்த இலைகளை அகற்றி அழிக்கவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும்.",
    },
    "Apple_Healthy": {
        "care": "காற்றோட்டத்திற்காக ஆண்டுதோறும் கத்தரிக்கவும், சமநிலையான உரம் இடவும், மேலிருந்து அல்லாமல் அடிப்பகுதியில் நீர் ஊற்றவும், பூச்சி அல்லது நோய் அறிகுறிகளை தொடர்ந்து சரிபார்க்கவும்.",
    },
    "Apple_Scab": {
        "chemical": "Captan, mancozeb, அல்லது myclobutanil பூஞ்சைக்கொல்லி பச்சை நுனி முதல் இதழ் உதிரும் வரை.",
        "organic": "சல்பர் அல்லது காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லி; எதிர்கால நடவுகளுக்கு சொறி-எதிர்ப்பு இனங்களை பரிசீலிக்கவும்.",
        "care": "இலையுதிர் காலத்தில் விழுந்த இலைகளை அகற்றவும், தழையை திறக்க கத்தரிக்கவும்.",
    },
    "Cherry_Healthy": {
        "care": "திறந்த தழைக்காக கத்தரிக்கவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும், ஈரப்பதமான காலங்களில் பொடி பூஞ்சை அறிகுறிகளை கண்காணிக்கவும்.",
    },
    "Cherry_Powdery_Mildew": {
        "chemical": "சல்பர் அல்லது myclobutanil பூஞ்சைக்கொல்லி, வளர்ச்சி காலம் முழுவதும் லேபிள்படி மீண்டும் தெளிக்கவும்.",
        "organic": "வேப்பெண்ணெய் அல்லது பொட்டாசியம் பைகார்பனேட் தெளிப்பு; நீர்த்த பால் தெளிப்பு ஒரு பொதுவான வீட்டு வைத்தியம்.",
        "care": "காற்றோட்டத்திற்காக கத்தரிக்கவும், அதிக நைட்ரஜன் உரத்தை தவிர்க்கவும், மேலிருந்து அல்லாமல் மண் மட்டத்தில் நீர் ஊற்றவும்.",
    },
    "Corn_Common_Rust": {
        "chemical": "நோய்த்தொற்று கடுமையாக அல்லது வேகமாக பரவினால் azoxystrobin அல்லது propiconazole பூஞ்சைக்கொல்லி.",
        "organic": "குறைந்த அளவில் பொதுவாக தேவையில்லை; அடுத்த பருவத்திற்கு துரு-எதிர்ப்பு கலப்பினங்களுக்கு முன்னுரிமை கொடுக்கவும்.",
        "care": "பயிர் சுழற்சி செய்யவும், தானாக முளைத்த சோள செடிகளை அகற்றவும், அதிக அடர்த்தியான நடவை தவிர்க்கவும்.",
    },
    "Corn_Healthy": {
        "care": "ஒவ்வொரு பருவத்திலும் பயிர் சுழற்சி செய்யவும், காற்றோட்டத்திற்கு சம இடைவெளி பராமரிக்கவும், ஈரப்பதமான வானிலையில் தொடர்ந்து கண்காணிக்கவும்.",
    },
    "Corn_Northern_Leaf_Blight": {
        "chemical": "புண்கள் தோன்றிய உடனேயே azoxystrobin அல்லது propiconazole பூஞ்சைக்கொல்லி தெளிக்கவும்.",
        "organic": "பயிர் சுழற்சியும் எதிர்ப்பு கலப்பினங்களுமே இங்கு முக்கிய வேதியியல் அல்லாத வழிகள்.",
        "care": "அறுவடைக்குப் பிறகு பயிர் எச்சங்களை மண்ணில் கலக்கவும், குறைந்தது ஒரு பருவத்திற்காவது சோளத்திலிருந்து விலகி சுழற்சி செய்யவும்.",
    },
    "Grape_Black_Rot": {
        "chemical": "Mancozeb அல்லது myclobutanil பூஞ்சைக்கொல்லி முளை வளர்ச்சி தொடங்கியது முதல் veraison வரை.",
        "organic": "காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லி; பாதிக்கப்பட்ட காய்களை அகற்றி அழிக்கவும்.",
        "care": "திறந்த தழைக்காக கத்தரிக்கவும், பாதிக்கப்பட்ட கொடிகளையும் காய்களையும் உடனடியாக அகற்றவும்.",
    },
    "Grape_Healthy": {
        "care": "காற்றோட்டத்திற்காக ஆண்டுதோறும் கத்தரிக்கவும், விழுந்த பழங்கள் மற்றும் இலைகளை அகற்றவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும்.",
    },
    "Peach_Bacterial_Spot": {
        "chemical": "காப்பர் அடிப்படையிலான பாக்டீரியா-கொல்லி, உறக்க காலத்திலும் ஆரம்ப வளர்ச்சியிலும் தெளிக்கவும் (இது பாக்டீரியா நோய் என்பதால் பூஞ்சைக்கொல்லிகள் உதவாது).",
        "organic": "காப்பர் தெளிப்பே இங்கும் இயற்கை-அங்கீகரிக்கப்பட்ட வழி.",
        "care": "மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும், காற்றோட்டத்திற்காக கத்தரிக்கவும், அதிக நைட்ரஜன் உரத்தை தவிர்க்கவும்.",
    },
    "Peach_Healthy": {
        "care": "திறந்த மையத்திற்காக கத்தரிக்கவும், அடிப்பகுதியில் நீர் ஊற்றவும், ஈரமான வானிலையில் ஆரம்ப இலை-புள்ளிகளை கவனிக்கவும்.",
    },
    "Pepper_Bacterial_Spot": {
        "chemical": "காப்பர் அடிப்படையிலான பாக்டீரியா-கொல்லி, எதிர்ப்புத்திறன் அதிகரிப்பதை தடுக்க mancozeb உடன் கலந்து தெளிக்கப்படும்.",
        "organic": "காப்பர் தெளிப்பு, எதிர்ப்பு இனங்கள், மற்றும் பயிர் சுழற்சி.",
        "care": "மேலிருந்து நீர்ப்பாசனத்திற்கு பதிலாக சொட்டு நீர்ப்பாசனம் பயன்படுத்தவும், ஈரமான வயல்களில் வேலை செய்வதை தவிர்க்கவும், பாதிக்கப்பட்ட எச்சங்களை அகற்றவும்.",
    },
    "Pepper_Healthy": {
        "care": "அடிப்பகுதியில் நீர் ஊற்றவும், காற்றோட்டத்திற்கு இடைவெளி விடவும், ஒவ்வொரு பருவத்திலும் நடவு இடத்தை சுழற்சி செய்யவும்.",
    },
    "Potato_Early_Blight": {
        "chemical": "புண்கள் தோன்றிய உடனேயே chlorothalonil அல்லது azoxystrobin பூஞ்சைக்கொல்லி.",
        "organic": "காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லி அல்லது வேப்பெண்ணெய்; உருளைக்கிழங்கு/தக்காளியிலிருந்து விலகி பயிர் சுழற்சி செய்யவும்.",
        "care": "செடிகளுக்கு போதிய இடைவெளி விடவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும், பாதிக்கப்பட்ட இலைகளை அகற்றவும்.",
    },
    "Potato_Healthy": {
        "care": "தண்டுகளைச் சுற்றி மண் மேடு அமைக்கவும், அடிப்பகுதியில் தொடர்ந்து நீர் ஊற்றவும், ஒவ்வொரு பருவத்திலும் பயிர் சுழற்சி செய்யவும்.",
    },
    "Potato_Late_Blight": {
        "chemical": "Chlorothalonil, mancozeb, அல்லது metalaxyl அடிப்படையிலான பூஞ்சைக்கொல்லி — உடனடியாக தெளித்து லேபிள்படி மீண்டும் செய்யவும், குறிப்பாக ஈரமான வானிலையில். இந்த நோய் வேகமாக பரவக்கூடியது.",
        "organic": "காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லியை முன்னெச்சரிக்கையாக பயன்படுத்தவும்; பாதிக்கப்பட்ட செடிகளை உடனடியாக அகற்றி அழிக்கவும்.",
        "care": "மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும், நல்ல வடிகால் மற்றும் காற்றோட்டத்தை உறுதி செய்யவும், பாதிக்கப்பட்ட பொருட்களை ஒருபோதும் உரமாக்க வேண்டாம்.",
    },
    "Strawberry_Healthy": {
        "care": "அறுவடைக்குப் பிறகு தோட்டங்களை புதுப்பிக்கவும், பழைய இலைகளை அகற்றவும், காற்றோட்டத்திற்கு செடிகளுக்கு இடைவெளி விடவும்.",
    },
    "Strawberry_Leaf_Scorch": {
        "chemical": "Captan அல்லது myclobutanil பூஞ்சைக்கொல்லி.",
        "organic": "பாதிக்கப்பட்ட இலைகளை அகற்றி அழிக்கவும்; செடிகளைச் சுற்றி காற்றோட்டத்தை மேம்படுத்தவும்.",
        "care": "அறுவடைக்குப் பிறகு தோட்டங்களை புதுப்பிக்கவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும்.",
    },
    "Tomato_Bacterial_Spot": {
        "chemical": "காப்பர் அடிப்படையிலான பாக்டீரியா-கொல்லி, எதிர்ப்புத்திறன் மேலாண்மைக்காக mancozeb உடன் அடிக்கடி கலக்கப்படும்.",
        "organic": "காப்பர் தெளிப்பு, எதிர்ப்பு இனங்கள், மற்றும் பயிர் சுழற்சி.",
        "care": "மேலிருந்து நீர் ஊற்றுவதை தவிர்க்கவும், ஈரமாக இருக்கும்போது செடிகளை தொடாதீர்கள், செடிகளுக்கு இடையே கருவிகளை கிருமி நீக்கம் செய்யவும்.",
    },
    "Tomato_Early_Blight": {
        "chemical": "முதல் அறிகுறிகள் தோன்றியவுடன் chlorothalonil அல்லது azoxystrobin பூஞ்சைக்கொல்லி, லேபிள்படி ஒவ்வொரு 7–10 நாட்களுக்கும் மீண்டும் தெளிக்கவும்.",
        "organic": "காப்பர் பூஞ்சைக்கொல்லி அல்லது வேப்பெண்ணெய்; மண் தெறிப்பதை குறைக்க அடிப்பகுதியில் மல்ச் இடவும்.",
        "care": "பாதிக்கப்பட்ட கீழ் இலைகளை அகற்றவும், காற்றோட்டத்திற்காக செடிகளை கட்டவும், ஒவ்வொரு பருவத்திலும் பயிர் சுழற்சி செய்யவும்.",
    },
    "Tomato_Healthy": {
        "care": "காற்றோட்டத்திற்காக கட்டு அல்லது கூண்டு பயன்படுத்தவும், காலையில் அடிப்பகுதியில் நீர் ஊற்றவும், மண் தெறிப்பதை குறைக்க மல்ச் இடவும்.",
    },
    "Tomato_Late_Blight": {
        "chemical": "Chlorothalonil, mancozeb, அல்லது mefenoxam கொண்ட பூஞ்சைக்கொல்லி — குளிர்ந்த, ஈரமான வானிலையில் உடனடியாகவும் அடிக்கடியும் தெளிக்கவும்.",
        "organic": "காப்பர் அடிப்படையிலான பூஞ்சைக்கொல்லியை முன்னெச்சரிக்கையாக பயன்படுத்தவும்; பரவலை கட்டுப்படுத்த பாதிக்கப்பட்ட செடிகளை விரைவாக அகற்றி அழிக்கவும்.",
        "care": "மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும், செடிகளுக்கு இடையிலான இடைவெளியை அதிகரிக்கவும், பாதிக்கப்பட்ட எச்சங்களை ஒருபோதும் உரமாக்க வேண்டாம்.",
    },
    "Tomato_Leaf_Mold": {
        "chemical": "Chlorothalonil அல்லது mancozeb பூஞ்சைக்கொல்லி.",
        "organic": "காற்றோட்டத்தை மேம்படுத்தவும் (பசுமை இல்லங்களில் பொதுவானது) ஈரப்பதத்தை குறைக்கவும்; காப்பர் தெளிப்பை மறு வழியாக பயன்படுத்தவும்.",
        "care": "கீழ் இலைகளை கத்தரிக்கவும், இடைவெளியை அதிகரிக்கவும், மேலிருந்து நீர்ப்பாசனத்தை தவிர்க்கவும்.",
    },
    "Tomato_Yellow_Leaf_Curl_Virus": {
        "chemical": "வைரஸுக்கு நேரடி வேதியியல் மருந்து இல்லை — imidacloprid போன்ற பூச்சிக்கொல்லிகள் இதை பரப்பும் வெள்ளை ஈயை குறிவைக்கின்றன.",
        "organic": "வெள்ளை ஈக்களுக்கு எதிராக வேப்பெண்ணெய் அல்லது பூச்சிக்கொல்லி சோப்பு; பிரதிபலிக்கும் மல்ச் அவற்றை விரட்ட உதவும்.",
        "care": "வெள்ளை ஈ-எதிர்ப்பு இனங்களை பயன்படுத்தவும், முடிந்தால் பூச்சி வலைகளை பயன்படுத்தவும், மீதமுள்ள பயிரை பாதுகாக்க பாதிக்கப்பட்ட செடிகளை உடனடியாக அகற்றி அழிக்கவும்.",
    },
}


# ---------------------------------------------------------------------
# Crop Recommender translations
#
# Keyed by the exact names in crop_data.py (CROPS keys) and the option
# values used there (soil_types, climate_zones, irrigation_type,
# growing_methods).
# ---------------------------------------------------------------------

CROP_NAMES_TA = {
    "Spinach": "பசலைக்கீரை",
    "Lettuce": "லெட்யூஸ்",
    "Kale": "கேல்",
    "Basil": "துளசி",
    "Mint": "புதினா",
    "Coriander": "கொத்தமல்லி",
    "Strawberry": "ஸ்ட்ராபெரி",
    "Tomato_Dwarf": "குள்ள தக்காளி",
    "Chili_Pepper": "மிளகாய்",
    "Cucumber": "வெள்ளரிக்காய்",
    "Green_Beans": "பச்சை பீன்ஸ்",
    "Radish": "முள்ளங்கி",
    "Okra": "வெண்டைக்காய்",
    "Potato": "உருளைக்கிழங்கு",
    "Wheat": "கோதுமை",
    "Rice_Paddy": "நெல்",
    "Sugarcane": "கரும்பு",
    "Groundnut": "நிலக்கடலை",
    "Aloe_Vera": "கற்றாழை",
    "Fenugreek": "வெந்தயம்",
}

# Maps a raw option value from crop_data.py (growing_methods,
# soil_types, climate_zones, irrigation_type) to its STRINGS key, so
# form widgets and result cards can show translated labels while the
# underlying matching logic still works on the plain English values.
OPTION_KEY_MAP = {
    "vertical": "setup_vertical",
    "container": "setup_container",
    "open_field": "setup_open_field",
    "sandy": "soil_sandy",
    "loamy": "soil_loamy",
    "clay": "soil_clay",
    "silty": "soil_silty",
    "red_soil": "soil_red_soil",
    "black_soil": "soil_black_soil",
    "peaty": "soil_peaty",
    "tropical": "climate_tropical",
    "subtropical": "climate_subtropical",
    "temperate": "climate_temperate",
    "arid": "climate_arid",
    "drip": "irrigation_drip",
    "wick": "irrigation_wick",
    "hydroponic_nft": "irrigation_hydroponic_nft",
    "sprinkler": "irrigation_sprinkler",
    "flood": "irrigation_flood",
    "hand_watering": "irrigation_hand_watering",
}


def translate_crop_name(crop_name: str) -> str:
    """Crop display name in the current language."""
    if get_lang() == "ta":
        return CROP_NAMES_TA.get(crop_name, crop_name.replace("_", " "))
    return crop_name.replace("_", " ")


def translate_option(value: str) -> str:
    """Translate a raw option value (soil type, climate zone,
    irrigation type, growing method) via OPTION_KEY_MAP + STRINGS.
    Falls back to a title-cased, underscore-stripped version of the
    raw value if no mapping exists."""
    key = OPTION_KEY_MAP.get(value)
    if key:
        return t(key)
    return value.replace("_", " ").title()


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

def get_lang() -> str:
    return st.session_state.get("lang", DEFAULT_LANG)


def set_lang(lang: str):
    st.session_state["lang"] = lang


def t(key: str, **kwargs) -> str:
    """Look up a UI string in the current language, with optional
    .format(**kwargs) substitution. Falls back to English, then to
    the raw key, if a translation is missing."""
    entry = STRINGS.get(key)
    if entry is None:
        return key
    lang = get_lang()
    text = entry.get(lang) or entry.get("en") or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text


def translate_class_name(class_name: str) -> str:
    """Species/disease display name in the current language."""
    if get_lang() == "ta":
        return CLASS_NAMES_TA.get(class_name, class_name.replace("_", " "))
    return class_name.replace("_", " ")


def translate_treatment(class_name: str) -> dict:
    """Treatment dict (chemical/organic/care) in the current language.
    Falls back to the English treatment_guide.py entry for any key
    missing from the Tamil set."""
    from treatment_guide import get_treatment

    en_treatment = get_treatment(class_name) or {}
    if get_lang() != "ta":
        return en_treatment

    ta_treatment = TREATMENTS_TA.get(class_name, {})
    merged = dict(en_treatment)
    merged.update(ta_treatment)
    return merged


def render_language_switcher():
    """Two small pill-style buttons (EN / தமிழ்) rendered wherever
    called — intended for the sidebar, right under the page nav."""
    current = get_lang()

    st.markdown(
        '<div style="font-family:\'IBM Plex Mono\', monospace; font-size:0.68rem; '
        'letter-spacing:0.12em; text-transform:uppercase; color:#8FA893; '
        'margin:1.2rem 0 0.5rem 0;">Language</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button(
            "EN",
            key="lang_btn_en",
            use_container_width=True,
            type="primary" if current == "en" else "secondary",
        ):
            set_lang("en")
            st.rerun()
    with col2:
        if st.button(
            "தமிழ்",
            key="lang_btn_ta",
            use_container_width=True,
            type="primary" if current == "ta" else "secondary",
        ):
            set_lang("ta")
            st.rerun()