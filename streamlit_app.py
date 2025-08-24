# streamlit_app.py
# Generative AI Streamlit App for Google Cloud Gemini

import os

import streamlit as st
from google import genai

st.set_page_config(page_title="Generative AI Demo", layout="wide")

st.title("Generative AI with Google Cloud Gemini")

# User inputs
PROJECT_ID = st.text_input(
    "Google Cloud Project ID",
    value=os.environ.get("GOOGLE_CLOUD_PROJECT", "")
)

LOCATION = st.text_input(
    "Google Cloud Region",
    value=os.environ.get("GOOGLE_CLOUD_REGION", "global")
)

MODEL_ID = st.text_input("Model ID", value="gemini-2.0-flash")

prompt = st.text_area("Enter your prompt for the AI model:")

if st.button("Generate"):
    if not PROJECT_ID:
        st.error("Please enter a valid PROJECT_ID")
    elif not prompt.strip():
        st.error("Please enter a prompt")
    else:
        try:
            # Initialize client
            client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

            # Generate response
            response = client.generate_text(model=MODEL_ID, prompt=prompt)
            st.subheader("AI Response:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown("Powered by [Google Cloud Generative AI](https://cloud.google.com/vertex-ai)")
