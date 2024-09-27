import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

#designing the page
st.title("Convert Your Image to Text")
user_input = st.text_input("Input Prompt:")

uploaded_file = st.file_uploader("upload the image...",type = ["jpg","jpeg","png"])

# Display the image on the page
from PIL import Image
img = ""
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption="uploaded image",use_column_width=True)

# Function for evaluating the image and annotating it.

def gemini_response(user_input, img):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if user_input !="":
        response = model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text

# create submit button and map the genai function
submit = st.button("Do the magic...")

if submit:
    response = gemini_response(user_input=user_input, img=img)     
    st.subheader("The response is:")
    st.write(response)