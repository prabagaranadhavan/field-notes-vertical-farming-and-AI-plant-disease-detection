# Field Notes — Vertical Farming Assistant

A Streamlit app for vertical/home farming: get a crop plan for your
space and soil, follow a stage-by-stage care timeline, and diagnose
plant leaf diseases from a photo using a trained MobileNetV2 model.
Available in English and Tamil.

## Features

- **Home** — introduces the assistant with an animated vertical-farm
  illustration, links into the two tools below.
- **Crop Recommender** — enter your growing setup, soil type, climate
  zone (auto-detectable via browser geolocation), and available
  space; get a strict-fit list of suitable crops, each with a
  watering/irrigation/spacing plan and a scaled care timeline. Crops
  the disease detector has coverage for get a "check this crop for
  disease" shortcut straight into the Analyser.
- **Analyser** — upload a leaf photo, get the top predicted
  species/disease with a confidence readout, plus a treatment card
  (chemical control, organic control, cultural practices) or general
  maintenance tips for healthy plants.

## Project structure

## Setup

1. Clone this repo and create a virtual environment:
2. Install dependencies:
3. Train the disease-detection model (needs a data/train/<class_name>/
   folder of labeled leaf images, not included in this repo):   This produces model/plant_disease_model.keras and
   model/class_names.json, both required for the Analyser page.

4. (Optional) Add your own vertical farm photo at
   assets/vertical_farm.jpg to show a real photo on the home page.

5. Run the app:
## Notes

- The disease model covers 26 classes across 8 species: Apple,
  Cherry, Corn, Grape, Peach, Pepper, Potato, Strawberry, Tomato.
- Treatment guidance in this repo is general agricultural-extension
  style information, not a substitute for professional advice.
  Always follow product labels and consult a local agricultural
  extension office for anything region-specific.
- model/ and data/ are git-ignored since they are large binary or
  dataset files. Regenerate them locally rather than committing them.
