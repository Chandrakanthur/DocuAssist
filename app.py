import streamlit as st
import base64

def set_background(image_file):
    """Sets the background of the Streamlit app."""
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded_string = base64.b64encode(img_data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded_string});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Set the background image
set_background("background.png")  # Replace with your image file

st.title("Simple File Uploader")

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    st.write("File name:", uploaded_file.name)
    st.write("File type:", uploaded_file.type)
    st.write("File size:", len(uploaded_file.getvalue()))
