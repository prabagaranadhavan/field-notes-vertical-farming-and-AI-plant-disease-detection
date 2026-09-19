import os
import json

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from style import get_css, get_topbar_html, PALETTE
from treatment_guide import is_healthy_class
from translations import t, translate_class_name, translate_treatment, translate_crop_name
from crop_species_link import get_detector_species, prediction_matches_species


MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "plant_disease_model.keras")
CLASS_PATH = os.path.join(MODEL_DIR, "class_names.json")
IMAGE_SIZE = (224, 224)


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_resource
def load_class_names():
    with open(CLASS_PATH, "r") as file:
        return json.load(file)


def prepare_image(pil_image):
    """
    Composite transparent PNGs onto white before resizing — leaving
    transparency in place turns it black on RGB conversion, which looks
    nothing like the photographed leaves the model trained on.
    Otherwise, hand the model raw 0-255 pixels: preprocessing is baked
    into the model graph itself (mobilenet_v2.preprocess_input).
    """
    if pil_image.mode in ("RGBA", "LA") or (
        pil_image.mode == "P" and "transparency" in pil_image.info
    ):
        pil_image = pil_image.convert("RGBA")
        white_bg = Image.new("RGBA", pil_image.size, (255, 255, 255, 255))
        pil_image = Image.alpha_composite(white_bg, pil_image).convert("RGB")
    else:
        pil_image = pil_image.convert("RGB")

    img = pil_image.resize(IMAGE_SIZE)
    img_array = tf.keras.utils.img_to_array(img)
    return np.expand_dims(img_array, axis=0)


def predict(model, class_names, pil_image, top_k=3):
    img_array = prepare_image(pil_image)
    predictions = model.predict(img_array, verbose=0)[0]

    if len(predictions) != len(class_names):
        st.error(
            t("analyser_model_mismatch", pred=len(predictions), names=len(class_names))
        )
        return []

    top_indices = predictions.argsort()[::-1][:top_k]
    return [(class_names[i], float(predictions[i]) * 100) for i in top_indices]


def gauge_color(confidence):
    if confidence >= 60:
        return PALETTE["leaf"]
    if confidence >= 30:
        return PALETTE["amber"]
    return PALETTE["rust"]


def render_specimen_card(results):
    top_name, top_confidence = results[0]
    pretty_name = translate_class_name(top_name)
    dial_color = gauge_color(top_confidence)

    # Radial dial built with a conic-gradient — fill sweeps clockwise
    # from 12 o'clock to the confidence percentage, dim track for the rest.
    # NOTE: no leading indentation on these lines — Markdown treats 4+
    # leading spaces as a code block, which prints raw HTML as text
    # instead of rendering it.
    dial_html = (
        f'<div class="dial-wrap">'
        f'<div class="dial" style="background: conic-gradient({dial_color} '
        f'{top_confidence * 3.6:.1f}deg, var(--line-dark) 0deg);">'
        f'<div class="dial-inner">{top_confidence:.0f}%</div>'
        f'</div>'
        f'<div class="dial-meta">'
        f'<div class="specimen-label">{t("analyser_best_match")}</div>'
        f'<div class="specimen-name" style="margin:0;">{pretty_name}</div>'
        f'</div>'
        f'</div>'
    )

    ticks_html = ""
    for name, confidence in results[1:]:
        color = gauge_color(confidence)
        ticks_html += (
            f'<div class="tick-row">'
            f'<div class="tick-dot" style="background:{color};"></div>'
            f'<div class="tick-name">{translate_class_name(name)}</div>'
            f'<div class="tick-value">{confidence:.1f}%</div>'
            f'</div>'
        )

    card_html = (
        f'<div class="specimen-card">'
        f'<div class="specimen-label">{t("analyser_specimen_readout")}</div>'
        f'{dial_html}'
        f'{ticks_html}'
        f'</div>'
    )

    st.markdown(card_html, unsafe_allow_html=True)


def render_care_card(top_class_name):
    treatment = translate_treatment(top_class_name)
    if not treatment:
        return

    healthy = is_healthy_class(top_class_name)
    leaf = PALETTE["leaf"]
    amber = PALETTE["amber"]
    rust = PALETTE["rust"]

    rows = ""

    if healthy:
        rows += (
            f'<div class="care-row">'
            f'<div class="care-heading" style="color:{leaf};">{t("care_maintenance")}</div>'
            f'<div class="care-text">{treatment["care"]}</div>'
            f'</div>'
        )
    else:
        if "chemical" in treatment:
            rows += (
                f'<div class="care-row">'
                f'<div class="care-heading" style="color:{rust};">{t("care_chemical")}</div>'
                f'<div class="care-text">{treatment["chemical"]}</div>'
                f'</div>'
            )
        if "organic" in treatment:
            rows += (
                f'<div class="care-row">'
                f'<div class="care-heading" style="color:{amber};">{t("care_organic")}</div>'
                f'<div class="care-text">{treatment["organic"]}</div>'
                f'</div>'
            )
        if "care" in treatment:
            rows += (
                f'<div class="care-row">'
                f'<div class="care-heading" style="color:{leaf};">{t("care_cultural")}</div>'
                f'<div class="care-text">{treatment["care"]}</div>'
                f'</div>'
            )

    disclaimer = f'<div class="care-disclaimer">{t("care_disclaimer")}</div>'

    card_html = f'<div class="care-card">{rows}{disclaimer}</div>'
    st.markdown(card_html, unsafe_allow_html=True)


def render_context_banner():
    """
    Shows a small banner when the user arrived here from the Crop
    Recommender's "check this crop for disease" link, with a way to
    clear it and go back to general, crop-agnostic analysis. Returns
    the expected detector species prefix (or None) for use in the
    mismatch check after prediction.
    """
    crop_name = st.session_state.get("analyser_context_crop")
    if not crop_name:
        return None

    leaf = PALETTE["leaf"]
    muted = PALETTE["text_muted"]

    col1, col2 = st.columns([5, 1])
    with col1:
        st.markdown(
            f'<p style="color:{leaf}; font-size:0.85rem; margin-bottom:0.2rem;">'
            f'{t("analyser_context_banner", crop=translate_crop_name(crop_name))}</p>',
            unsafe_allow_html=True,
        )
    with col2:
        if st.button(t("analyser_context_clear"), key="clear_context"):
            del st.session_state["analyser_context_crop"]
            st.rerun()

    return get_detector_species(crop_name)


def main():
    st.set_page_config(
        page_title="Analyser — Field Notes",
        page_icon="🔬",
        layout="centered"
    )

    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(get_topbar_html(wordmark=t("brand_wordmark")), unsafe_allow_html=True)

    st.markdown(f'<div class="kicker">{t("analyser_kicker")}</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 style="font-size:2.2rem; margin-bottom:0.2rem;">{t("analyser_title")}</h1>', unsafe_allow_html=True)
    st.markdown(
        f'<p style="color:{PALETTE["text_muted"]}; max-width:32rem;">'
        f'{t("analyser_subtitle")}</p>',
        unsafe_allow_html=True
    )

    expected_species = render_context_banner()

    if not os.path.exists(MODEL_PATH) or not os.path.exists(CLASS_PATH):
        st.error(t("analyser_no_model"))
        return

    model = load_model()
    class_names = load_class_names()

    st.markdown('<hr class="hairline">', unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        t("analyser_uploader_label"),
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        pil_image = Image.open(uploaded_file)

        col1, col2 = st.columns([1, 1.3])
        with col1:
            st.image(pil_image, use_container_width=True)

        with col2:
            with st.spinner(t("analyser_spinner")):
                results = predict(model, class_names, pil_image, top_k=3)
            if results:
                render_specimen_card(results)

        if results:
            if expected_species and not prediction_matches_species(results[0][0], expected_species):
                st.markdown(
                    f'<p style="color:{PALETTE["amber"]}; font-size:0.85rem; '
                    f'margin-top:0.6rem;">⚠ {t("analyser_species_mismatch", crop=translate_crop_name(st.session_state["analyser_context_crop"]))}</p>',
                    unsafe_allow_html=True,
                )

            st.markdown(f'<div class="kicker" style="margin-top:1.4rem;">{t("analyser_recommended_care")}</div>', unsafe_allow_html=True)
            render_care_card(results[0][0])


if __name__ == "__main__":
    main()