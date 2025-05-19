import cryptocode
import streamlit as st


password = st.secrets["DECRYPT_CODE"]

with open('code.py', 'r', encoding='utf-8') as f:
    encoded_ = cryptocode.encrypt(f.read(), password)

with open("crypted_code.txt", "w") as file:
    file.write(encoded_)


