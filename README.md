# AB_Testing_Project
Web app : https://newchakri-ab-testing.streamlit.app
![image](https://github.com/NewChakri/AB_Testing_Project/assets/99199609/8a306b7c-ebba-4458-8a94-05d2cf597d32)

The AB Testing Project is a Python-based tool developed to automate the statistical analysis of two groups, enabling the determination of significant differences in metrics. The project boasts a user-friendly Streamlit interface that facilitates easy interaction and visualization of results. It implements statistical tests like the Independent Samples t Test and Mann-Whitney U Test, making it adaptable to various data distributions and variance conditions.

# What is A/B Testing?
A/B Testing is a method used to compare two groups, like Group A and Group B, to see if there's a significant difference in a metric, such as user engagement or sales. We use statistical tests to determine this difference.

# A/B Testing Steps
Step 1: Checking for Normality

We start by checking if our data follows a normal distribution using the Shapiro-Wilk test. If our data passes this test (p-value > 0.05), we proceed to Step 2. If not, we use the Mann-Whitney U Test instead.

Step 2: Testing for Equal Variances (Only for Normal Data)

If our data follows a normal distribution, we check if the variances (spread) of the two groups are similar using Levene's test. If the p-value from Levene's test is greater than 0.05, we assume equal variances and proceed with the Independent Samples t Test. If the p-value is less than or equal to 0.05, we assume unequal variances and adjust our test accordingly.

Step 3: Performing the Tests

Independent Samples t Test: This test checks if there's a significant difference between the averages of two groups. We interpret the p-value as follows:

If p-value < 0.05: We reject the null hypothesis, indicating a significant difference between the groups.
If p-value ≥ 0.05: We fail to reject the null hypothesis, suggesting no significant difference between the groups.
Mann-Whitney U Test: This test checks if there's a significant difference in the distributions of two groups, even if the data isn't normally distributed or has different variances. Similarly, we interpret the p-value:

If p-value < 0.05: We reject the null hypothesis, indicating a significant difference.
If p-value ≥ 0.05: We fail to reject the null hypothesis, suggesting no significant difference.


## A/B Testing Application

This Streamlit app allows users to perform A/B testing on their own data. Users can upload a CSV file, select the group and target columns, and run the A/B test to see the results.

## Features

- Upload CSV files directly through the app.
- Select the columns representing the groups (A/B) and the target metric.
- Automatically performs normality tests and chooses the appropriate statistical test (Independent Samples t Test or Mann-Whitney U Test).
- Displays the results of the A/B test, including p-values and test type.

## How to Use

Upload Data: Begin by uploading your CSV file containing the necessary columns.
Select Columns: Choose the group (A/B) and target metric columns from the uploaded data.
Run A/B Test: Click the button to run the A/B test and view the results.


## Example Scenario: Website Feature Engagement

**Scenario:** A company has launched a new feature on their website and wants to determine if it significantly increases user engagement. Group A represents users who have not been exposed to the new feature, while Group B represents users who have been exposed to the new feature. The target metric is `engagement_score`, which measures user engagement on a scale from 0 to 100.

### Input Data

The input data should be in CSV format with at least two columns:
- `group`: Indicates the user group (e.g., "A" or "B").
- `engagement_score`: The engagement score of the user, ranging from 0 to 100.

