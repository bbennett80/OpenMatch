
import requests
# from nlp import nlp

import streamlit as st

st.header("**OpenMatch**")
st.subheader('Choose the documents available for upload.')

st.sidebar.write("Copy and paste report text into boxes on the right -->")
documents = st.sidebar.multiselect('Available documents:', 
                        ['Pathology', 'Progress note', 'Imaging', 'Genetics'])



patient_button = st.button("Submit")
for doc in documents:
    doc_text = st.text_area(doc, key=doc)
    
    if patient_button:
        st.write(doc_text)



