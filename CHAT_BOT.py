import streamlit as st #for ui
import os
from dotenv import load_dotenv #to get env variables loaded into the application
load_dotenv() #loading of all the env variable

import google.generativeai as genai

#genai config of api
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# initialise the model
model = genai.GenerativeModel('gemini-pro')

# define a function to generate response from llm
def get_gemini_response(ques):
    resp = model.generate_content(ques)
    return resp.text

# setting up streamlit app
st.set_page_config(
    page_title="Gemini pro Q/A project",
    layout="wide",
    initial_sidebar_state="expanded",
)

# setting up header
st.header("Gemini Q/A app")
# st.title

# input
question = st.text_input("Ask a question: ")

#submit button
if st.button("Submit"):
    response = get_gemini_response(question)
    st.write("User:", question)
    st.write("Bot:", response)