from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import pathlib
import textwrap
import os
from PIL import Image
import google.generativeai as genai 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-pro-vision')
def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None :
        bytes_data=uploaded_file.getvalue()

        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data" : bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Title of the Streamlit app
st.set_page_config(page_title="Akshat Multi Lang Invoice Reader")
st.header("Akshat Multi Lang Invoice Reader")
input=st.text_input("Input Prompt: ",key="input")


# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])
image=""
# Check if a file has been uploaded
if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    
    # You can add more functionality here, such as processing the image with a machine learning model
    # For example, sending the image to an LLM (Large Language Model) if needed
else:
    st.write("Please upload an image file.")  

submit=st.button("Ask for Answer")
input_prompt= """
You are an expert in understanding invoices. We will upload a image as an invoice and you will have to answer any 
questions based on the upload image invoice.
"""
      
if submit:
    image_data=input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)
