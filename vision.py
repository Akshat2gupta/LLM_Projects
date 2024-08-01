from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-pro-vision")
def get_gemini_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    else:
         response=model.generate_content(image)
    return response.text


# Title of the Streamlit app
st.set_page_config(page_title="Akshat Image Reader")
st.header("Akshat Image Reader")
input=st.text_input("Input Prompt: ",key="input")


# Upload image file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

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

submit=st.button("the image means")
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The ans is")
    st.write(response)