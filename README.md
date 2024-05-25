# AB_Testing_Project

Developed a Python-based A/B Testing tool that automates the statistical analysis of two groups to determine significant differences in metrics. The project includes a user-friendly Streamlit interface for easy interaction and visualization of results. Implemented statistical tests such as Independent Samples t Test and Mann-Whitney U Test to accommodate different data distributions and variance conditions.

# A/B Testing Simplified
This project introduces a user-friendly function for conducting A/B Testing and interpreting the results of statistical hypothesis tests commonly used in A/B Testing.

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
