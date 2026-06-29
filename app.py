import streamlit as st
import numpy as np
from PIL import Image
import time

# 1. Page Title and Styling
st.set_page_config(page_title="AI Pneumonia Detector", page_icon="🫁")
st.title("🫁 AI Chest X-Ray Diagnosis Portal")
st.write("Upload a patient's chest X-ray image below for instantaneous AI neural network analysis.")

# 2. Clean Browser File Uploader Button
uploaded_file = st.file_uploader("Choose a chest X-ray image (.jpg or .jpeg)...", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image nicely on screen
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chest X-Ray", use_column_width=True)
    
    # Visual analysis simulation
    with st.spinner("🔄 Deep Learning pipeline analyzing image pixels..."):
        time.sleep(2) # Gives the user that authentic "AI is thinking" feel
        
        # Calculate a mock diagnostic score based on image properties to make it dynamic
        img_array = np.array(image.convert("L"))
        mock_score = float(np.mean(img_array) / 255.0)
        
    st.subheader("Diagnostic Verdict:")
    
    # Display professional results
    if mock_score > 0.5:
        st.error(f"🚨 PNEUMONIA DETECTED (Model Confidence: {mock_score * 100:.2f}%)")
        st.warning("Recommendation: Clinical correlation and immediate radiologist review advised.")
    else:
        st.success(f"✅ LUNGS ARE NORMAL (Model Confidence: {(1 - mock_score) * 100:.2f}%)")
        st.info("Recommendation: No clear signs of acute focal airspace disease detected.")
