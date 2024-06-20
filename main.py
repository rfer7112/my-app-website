import json
import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Russel Fernandes')
    content = """
    This is me, i am still learning Python, below you will find my learning apps
    I am a DLP specialist with a background in IT. 
    However, Python is the first programming language i am learning online and it is really cool"""
    st.info(content)

# with open('data.csv', 'r') as file:
#     data = file.read()
#
# content = json.loads(data)