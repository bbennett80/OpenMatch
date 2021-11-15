from transformers import AutoTokenizer, AutoModel

#import streamlit as st

#@st.cache
def load_model():
    tokenizer = AutoTokenizer.from_pretrained("bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12")
    model = AutoModel.from_pretrained("bionlp/bluebert_pubmed_uncased_L-12_H-768_A-12")
    return tokenizer, model

