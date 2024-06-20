import json
import pandas
import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')


with col2:
    st.title('Russel Fernandes')
    about_me = """
    This is me, i am still learning Python.
    I am a DLP specialist with a background in IT. 
    However, Python is the first programming language i am learning online and it is really cool"""
    st.info(about_me)

text1 = """
Below you can find some of the apps i have built in Python. Feel free to contact me"""
st.write(text1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv('data.csv', sep=';')
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
