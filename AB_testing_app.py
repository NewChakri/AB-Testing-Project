import streamlit as st
import pandas as pd
from AB_Testing import AB_Test

# Set app-wide theme to align button text to the left
st.set_page_config(page_title="A/B Testing Application")

# Title of the app
st.title("A/B Testing Analysis")

# File uploader to upload CSV
uploaded_file = st.file_uploader("Please upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.write("### Data Preview:")
    st.write(df.head())

    # Sidebar inputs to select columns
    group = st.sidebar.selectbox("Select the column representing groups (e.g., A/B)", df.columns)
    target = st.sidebar.selectbox("Select the column representing the target metric", df.columns)

    # Run A/B test when the button is clicked
    if st.sidebar.button("Execute A/B Test", key="execute_ab_test", help="Run the A/B test and display the results"):
        result = AB_Test(dataframe=df, group=group, target=target)

        # Display the test result in a clear format
        st.subheader("A/B Testing Analysis Results")

        # Use success or warning message based on the result
        if result['AB Hypothesis'].values[0] == "Statistically Significant":
            st.success("The test indicates a statistically significant difference between the A and B groups.")
        else:
            st.warning("The test does not indicate a statistically significant difference between the A and B groups.")
            
        # Display the full result in a table
        st.table(result)
else:
    st.write("Please upload a CSV file to proceed.")
