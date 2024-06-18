import streamlit as st
import helper
import pickle

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Add custom CSS for background and button styling
st.markdown("""
    <style>
    .main {
        background-color: #FAA0A0;
    }
    .stButton button {
        background-color: #C21E56;
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #C21E56;
    }
    .stTextInput > div > div > input {
        border: 2px solid #C21E56;
        border-radius: 4px;
        padding: 10px;
        font-size: 16px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #C21E56;
    }
    </style>
    """, unsafe_allow_html=True)

# Page header
st.header("Enter Your Question To Check Whether It's Duplicate or Not")

# Input fields for the questions
q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

# Button to find if the questions are duplicates
if st.button('Find'):
    query = helper.query_point_creator(q1, q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
