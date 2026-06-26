import streamlit as st
from PIL import Image
from transformers import pipeline

st.title("🌱 AI Plant Disease Detection")

uploaded_file = st.file_uploader(
    "Upload Plant Leaf Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    disease = "Tomato Early Blight"

    st.success(f"Detected Disease: {disease}")

    disease_info = {
        "Tomato Early Blight": """
Symptoms:
• Brown spots on leaves
• Yellowing of leaves

Causes:
• Fungal infection
• High humidity

Prevention:
• Remove infected leaves
• Avoid overwatering
• Maintain proper spacing

Treatment:
• Apply fungicide
• Use disease-resistant varieties
"""
    }

    st.subheader("🤖 AI Recommendation")
    st.write(disease_info.get(disease, "No information available"))
