
import requests

import streamlit as st

st.header("**OpenMatch**")

# Patient search
st.sidebar.write("Copy and paste report text into boxes on the right -->")
pathology = st.text_area("Pathology report", key="Pathology")
note = st.text_area("Oncology note", key="Note")
imaging = st.text_area("Imaging", key="Imaging")
genetics = st.text_area("Genetics", key="Genetics")

patient_button = st.button("Submit")
if patient_button:
    st.write("**Pathology report:**", pathology)
    st.write("**Oncology note:**", note)
    st.write("**Imaging report:**", imaging)
    st.write("**Genetics report:**", genetics)
