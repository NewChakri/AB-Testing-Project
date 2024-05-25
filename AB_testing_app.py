import streamlit as st
import pandas as pd
from AB_Testing import AB_Test

# Set page configuration
st.set_page_config(
    page_title="A/B Testing Analysis",
    page_icon="🔍",
    layout="wide",
)

# Title of the app
st.title("A/B Testing Analysis")

# Sidebar for file upload and options
st.sidebar.header("Upload your data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())

    # Sidebar inputs to select columns
    st.sidebar.header("Select Columns for Analysis")
    group = st.sidebar.selectbox("Select Group Column", df.columns)
    target = st.sidebar.selectbox("Select Target Column", df.columns)

    # Run A/B test when the button is clicked
    if st.sidebar.button("Execute A/B Test", key="execute_ab_test", help="Run the A/B test and display the results"):
        result = AB_Test(dataframe=df, group=group, target=target)

        # Display the test result in a clear format
        st.subheader("A/B Testing Results")

        # Use success or warning message based on the result
        if result['AB Hypothesis'].values[0] == "Statistically Significant":
            st.success("The test indicates a statistically significant difference between the A and B groups.")
        else:
            st.warning("The test does not indicate a statistically significant difference between the A and B groups.")

        # Display the full result in a styled table
        st.table(styled_result)
else:
    st.write("Please upload a CSV file to proceed with the A/B test analysis.")
