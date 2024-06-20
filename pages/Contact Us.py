import streamlit as st
from send_email import mail


st.header("Contact Me")
email_sender = "russel.nlwork@gmail.com"

with st.form(key='email_form'):
    user_email = st.text_input("Your Email Address")
    raw_message = st.text_area("Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        mail(message)
        st.info("Your email was sent")


