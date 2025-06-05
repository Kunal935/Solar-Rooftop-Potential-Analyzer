import streamlit as st
from PIL import Image
import numpy as np
from utils.solar_analysis import analyze_image_and_estimate

st.set_page_config(page_title="Solar Rooftop Analysis Tool", layout="centered")

st.title("🔆 AI-Powered Solar Rooftop Assessment Tool")
st.markdown("""
Upload a rooftop satellite image to get a quick solar installation recommendation including:
- Estimated usable area
- Number of panels
- Cost and ROI analysis
""")

uploaded_file = st.file_uploader("Upload Rooftop Image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

    if st.button("Analyze Rooftop"):
        with st.spinner("Analyzing image and calculating potential..."):
            result = analyze_image_and_estimate(image)

        st.success("Analysis Complete!")
        st.markdown(f"### Usable Area: `{result['usable_area']} m²`")
        st.markdown(f"### Panels Fit: `{result['panel_count']}`")
        st.markdown(f"### Estimated Installation Cost: `₹{result['estimated_cost']}`")
        st.markdown(f"### Expected Monthly Savings: `₹{result['monthly_savings']}`")
        st.markdown(f"### ROI / Payback Period: `{result['payback_period']} years`")
        st.markdown("---")
        st.info("This is an estimate based on image area. Exact values depend on roof tilt, sun exposure, etc.")
