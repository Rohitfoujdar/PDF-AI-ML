import streamlit as st
import pandas as pd
import numpy as np

#Title
st.title("Rohit foujdar")

#Simple text
st.write("I am a software developer")

#Create a dataframe 
df = pd.DataFrame({
    "first column":[1, 2, 3, 4],
    "second column":[133, 2333, 333, 444]
})

#display dataframe
st.write("Here is Dataframe")
st.write(df)

#Create a line chart
st.write("This is line chart")
chart_data = pd.DataFrame(
    np.random.randn(20,3) , columns = ["a","b","c"]
)

st.line_chart(chart_data)
