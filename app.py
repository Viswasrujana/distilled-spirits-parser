import streamlit as st
import pytesseract
import cv2
import numpy as np
import os
import sys
from PIL import Image

# Ensure Streamlit Cloud can resolve local imports properly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.parser import generate_free_label, free_parse_text

st.set_page_config(page_title="Spirits Label Parser", page_icon="🥃", layout="centered")

st.title("🥃 Spirits Label Compliance Scanner")
st.write("A 100% free tool to mock synthetic labels and parse out core TTB information fields.")

tab1, tab2 = st.tabs(["🎯 1. Generate Free Test Label", "🔍 2. Run OCR & Parser Pipeline"])

with tab1:
    st.subheader("Generate Synthetic Label Dataset")

    sample_labels = {
        "OLD TOM DISTILLERY": {
            "brand": "OLD TOM DISTILLERY",
            "ctype": "Kentucky Straight Bourbon Whiskey",
            "alcohol": "45% Alc./Vol. (90 Proof)",
            "net": "750 mL"
        },
        "RIVERSTONE RESERVE": {
            "brand": "RIVERSTONE RESERVE",
            "ctype": "Tennessee Whiskey",
            "alcohol": "40% Alc./Vol. (80 Proof)",
            "net": "1 L"
        },
        "SILVER CREST": {
            "brand": "SILVER CREST",
            "ctype": "London Dry Gin",
            "alcohol": "47% Alc./Vol. (94 Proof)",
            "net": "750 mL"
        },
        "HARBOR OAK": {
            "brand": "HARBOR OAK",
            "ctype": "Aged Rum",
            "alcohol": "43% Alc./Vol. (86 Proof)",
            "net": "700 mL"
        },
        "MOUNTAIN PEAK DISTILLING CO.": {
            "brand": "MOUNTAIN PEAK DISTILLING CO.",
            "ctype": "Single Malt Whiskey",
            "alcohol": "50% Alc./Vol. (100 Proof)",
            "net": "375 mL"
        },
        "BLACK RIDGE BOURBON": {
            "brand": "BLACK RIDGE BOURBON",
            "ctype": "Kentucky Straight Bourbon Whiskey",
            "alcohol": "46% Alc./Vol. (92 Proof)",
            "net": "750 mL"
        }
    }

    selected_label = st.selectbox(
        "Select Sample Label",
        list(sample_labels.keys())
    )

    sample = sample_labels[selected_label]

    brand = st.text_input(
        "Brand Name Field",
        sample["brand"]
    )

    ctype = st.text_input(
        "Class/Type Field",
        sample["ctype"]
    )

    alcohol = st.text_input(
        "Alcohol Content Field",
        sample["alcohol"]
    )

    net = st.text_input(
        "Net Contents Field",
        sample["net"]
    )

    label_choice = st.selectbox(
        "Select Label Style to Generate",
        ["Front Label", "Back Label", "Neck Strip"]
    )

    type_mapping = {
        "Front Label": "FRONT",
        "Back Label": "BACK",
        "Neck Strip": "NECK"
    }

    chosen_type = type_mapping[label_choice]

    if st.button("Generate & Store Label Image"):
        img = generate_free_label(
            brand,
            ctype,
            alcohol,
            net,
            label_type=chosen_type
        )

        st.session_state["cached_label"] = img

        st.image(
            img,
            caption=f"Generated Mock {label_choice} Preview",
            width=350
        )

        st.success(
            "Mock image loaded into memory! Switch to Tab 2 to scan it."
        )

with tab2:
    st.subheader("Process & Structure Label Information")
    source_choice = st.radio("Select Image Source:", ["Use Generated Label from Tab 1", "Upload a Real Label Image File"])
    
    target_img = None
    if source_choice == "Use Generated Label from Tab 1":
        if 'cached_label' in st.session_state:
            target_img = st.session_state['cached_label']
        else:
            st.warning("Please go generate a label image in Tab 1 first.")
    else:
        uploaded_file = st.file_uploader("Upload PNG/JPG Label", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            target_img = Image.open(uploaded_file)
            
    if target_img:
        st.image(target_img, caption="Selected Target Image", width=300)
        
        if st.button("Run Text Analysis Pipeline"):
            with st.spinner("Executing CV processing and OCR extraction..."):
                cv_img = cv2.cvtColor(np.array(target_img), cv2.COLOR_RGB2BGR)
                gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
                try:
                    extracted_raw_text = pytesseract.image_to_string(gray)
                    final_json = free_parse_text(extracted_raw_text)
                    st.success("Analysis Complete!")
                    st.subheader("Extracted Output Schema")
                    st.json(final_json)
                except Exception as e:
                    st.error(f"OCR Error: Make sure Tesseract is installed on your system. Details: {e}")
