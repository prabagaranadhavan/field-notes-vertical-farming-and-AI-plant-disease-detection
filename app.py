import streamlit as st

from translations import t, render_language_switcher


home_page = st.Page(
    "pages/0_Home.py",
    title=t("nav_home"),
    icon="🌿",
    default=True
)

recommender_page = st.Page(
    "pages/1_Crop_Recommender.py",
    title=t("nav_recommender"),
    icon="🌾"
)

analyser_page = st.Page(
    "pages/2_Analyser.py",
    title=t("nav_analyser"),
    icon="🔬"
)

# Order in this list is the exact order shown in the sidebar:
# Home -> Crop Recommender -> Analyser
pg = st.navigation([home_page, recommender_page, analyser_page])

with st.sidebar:
    render_language_switcher()

pg.run()