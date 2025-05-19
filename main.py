import os
import cryptocode
import streamlit as st


password = st.secrets["DECRYPT_CODE"]

with open('crypted_code.txt', 'r', encoding='utf-8') as f:
    encoded = f.read()

decoded = cryptocode.decrypt(encoded, password)
eval(compile(decoded,'<string>','exec'))
