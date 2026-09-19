import os

import streamlit as st

from style import get_css, get_topbar_html, get_farm_rack_html, PALETTE
from translations import t


PHOTO_PATH = os.path.join("assets", "vertical_farm.jpg")


def render_tool_card(title_key, desc_key, page_path):
    st.markdown(
        f'<div class="tool-card">'
        f'<div class="tool-card-title">{t(title_key)}</div>'
        f'<div class="tool-card-desc">{t(desc_key)}</div>'
        f'</div>',
        unsafe_allow_html=True
    )
    st.page_link(page_path, label=t("home_card_open"), icon=None, use_container_width=True)


def main():
    st.set_page_config(
        page_title="Field Notes — Vertical Farming Assistant",
        page_icon="🌿",
        layout="centered"
    )

    st.markdown(get_css(), unsafe_allow_html=True)
    st.markdown(get_topbar_html(wordmark=t("brand_wordmark")), unsafe_allow_html=True)

    muted = PALETTE["text_muted"]
    leaf = PALETTE["leaf"]

    # ---------- hero ----------
    st.markdown(f'<div class="kicker" style="text-align:center;">{t("home_kicker")}</div>', unsafe_allow_html=True)
    st.markdown(
        f'<h1 style="font-size:2.5rem; line-height:1.1; text-align:center; margin-bottom:0.5rem;">'
        f'{t("home_title_line1")}<br><span style="font-style:italic; color:{leaf};">{t("home_title_line2")}</span></h1>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<p style="font-size:1rem; color:{muted}; text-align:center; '
        f'max-width:30rem; margin:0 auto 1.6rem auto;">{t("home_subtitle")}</p>',
        unsafe_allow_html=True
    )

    # ---------- animated vertical farm rack (signature visual) ----------
    st.markdown(get_farm_rack_html(), unsafe_allow_html=True)

    # ---------- real photo slot ----------
    # Looks for a user-supplied photo at assets/vertical_farm.jpg so
    # the page can show a genuine picture of a vertical farm without
    # hotlinking someone else's photo from the internet. Falls back
    # to a quiet instructional note if it isn't there yet.
    st.write("")
    if os.path.exists(PHOTO_PATH):
        st.image(PHOTO_PATH, use_container_width=True)
    else:
        st.markdown(
            f'<p style="text-align:center; font-size:0.75rem; color:{muted}; '
            f'font-family:\'IBM Plex Mono\',monospace;">{t("home_photo_caption")}</p>',
            unsafe_allow_html=True
        )

    st.markdown('<hr class="hairline">', unsafe_allow_html=True)

    # ---------- two tool cards ----------
    col1, col2 = st.columns(2)
    with col1:
        render_tool_card("home_card_recommender_title", "home_card_recommender_desc", "pages/1_Crop_Recommender.py")
    with col2:
        render_tool_card("home_card_analyser_title", "home_card_analyser_desc", "pages/2_Analyser.py")


if __name__ == "__main__":
    main()