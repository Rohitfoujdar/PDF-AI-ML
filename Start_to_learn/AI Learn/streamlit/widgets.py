import streamlit as st
import pandas as pd 

st.write("Here is input")

name = st.text_input("Enter you name:")

age = st.slider("Select yor age :" , 0 ,20 ,100)

st.write(f"Your age is , {age}")

if name:
    st.write(f"Hello , {name}")

option = ["Java script" , "Python" , "C++" , "Java"]
choice = st.selectbox("Choose your favorite language:" , option)
st.write(f"Your selected language {choice}")

data = {
    "Name":["Rohit", "Mayank" , "Rahul" , "Jyoti"],
    "Age":["20" , "19" ,"23" , "20"],
    "City":["Noida" , "Jaipur" , "Delhi" , "Noida"]
}

df = pd.DataFrame(data)

st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file" , type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)