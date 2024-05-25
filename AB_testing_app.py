import streamlit as st
import pandas as pd
from AB_Testing import AB_Test

# Set app-wide theme
st.set_page_config(page_title="A/B Testing App")

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
    if st.sidebar.button("Run A/B Test", key="run_ab_test", help="Run the A/B test and display the results"):
        result = AB_Test(dataframe=df, group=group, target=target)

        # Display the test result in a clear format
        st.subheader("A/B Test Result")

        # Use success or warning message based on the result
        if result['AB Hypothesis'].values[0] == "Statistically Significant":
            st.success("There is a significant difference between the A/B groups.")
        else:
            st.warning("There is no significant difference between the A/B groups.")

        # Display the full result in a table with centered text
        result_html = result.to_html(index=False)

        st.markdown(
            f"""
            <style>
            .dataframe {{
                text-align: center;
                width: 100%;
                margin: auto;
            }}
            .dataframe th {{
                text-align: center;
            }}
            .dataframe td {{
                text-align: center;
            }}
            </style>
            {result_html}
            """,
            unsafe_allow_html=True
        )
else:
    st.write("Please upload a CSV file to proceed.")
