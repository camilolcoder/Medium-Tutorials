import streamlit as st
from internal_logic import generate_image_from_text
from PIL import Image
import time
import os

# Sidebar for API key (optional)
with st.sidebar:
    anthropic_api_key = st.text_input("Maybe API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("🎨 Text to Image Generator")

prompt = st.text_input(
    "Enter a prompt to generate an image:",
    placeholder="A futuristic city with flying cars..."
)

# Button to trigger image generation
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating your image... 🚀 Please wait."):
            # Generate the image and get the saved file path
            image_path = generate_image_from_text(prompt)

        # Display the image once it's ready
        if image_path and os.path.exists(image_path):
            st.image(Image.open(image_path), caption="Generated Image", use_container_width=True)
            st.success("Image generation complete! 🎉")
        else:
            st.error("Something went wrong. Please try again.")
    else:
        st.warning("Please enter a prompt before generating an image.")
