import os
import openai
import streamlit as st
from dotenv import load_dotenv

 # Load environment variables from .env file
load_dotenv()

 # Set your OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

 

st.set_page_config(

    page_title="Generate Blogs",

    page_icon="🤖",

    layout="centered",

    initial_sidebar_state="collapsed"

)

 

st.header("Generate Blogs 🤖")

 

def get_GPT_response(prompt_text, max_tokens):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Specify the desired engine/model here
        prompt=prompt_text,
        max_tokens=max_tokens
    )
    return response.choices[0].text.strip()

 

input_text = st.text_input("Enter the Blog Topic")

 

col1, col2 = st.columns([5, 5])

 

with col1:

    no_words = st.text_input('No of Words')

with col2:

    blog_style = st.selectbox('Writing the blog for',

                              ('Researchers', 'Data Scientist', 'Common People'), index=0)

 

submit = st.button("Generate")

 

if submit:

    prompt_template = f"Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."

    generated_blog = get_GPT_response(prompt_template, int(no_words))

    st.write(generated_blog)

 