import streamlit as st
import pandas as pd
from AB_Testing import AB_Test

# Title of the app
st.title("A/B Testing App")

# File uploader to upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.write("Data Preview:")
    st.write(df.head())

    # Sidebar inputs to select columns
    group = st.sidebar.selectbox("Select Group Column", df.columns)
    target = st.sidebar.selectbox("Select Target Column", df.columns)

    # Run A/B test when the button is clicked
    if st.button("Run A/B Test"):
        result = AB_Test(dataframe=df, group=group, target=target)
        st.write(result)
else:
    st.write("Please upload a CSV file to proceed.")