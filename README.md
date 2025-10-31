Employee Churn Prediction using Machine Learning
📘 Software Engineering Project – Module I

By: Maaz Sameer Shaikh
Institute: Vishwakarma University, Pune
Faculty In-Charge: Prof. Pratibha Mahajan
Academic Year: 2023–2024 (Term II)

📊 Overview

This project aims to develop a predictive model for employee churn (attrition) — identifying employees who are likely to leave an organization. By leveraging data analytics and machine learning, the model helps HR teams take proactive actions to improve retention and employee satisfaction.

The system uses historical employee data, performs data visualization, and applies a Random Forest classifier to predict churn probabilities.

🧩 Dataset Information

The dataset contains employee details with the following features:

Feature	Description
Satisfaction Level	Employee’s job satisfaction score
Last Evaluation	Performance evaluation score
Number of Projects	Number of projects assigned
Average Monthly Hours	Average working hours per month
Time Spent in Company	Tenure (in years)
Work Accident	Whether the employee had a workplace accident
Promotion (Last 5 Years)	Whether the employee was promoted recently
Department	Employee’s department
Salary	Salary level (low, medium, high)
Target (Left)	1 = Employee left, 0 = Stayed
📈 Exploratory Data Analysis (EDA)

The data was explored using various visualizations to uncover patterns and relationships:

📊 Bar plots comparing employees who left vs stayed.

📦 Distribution of projects, company tenure, and promotions.

🔍 Count plots by department, salary, and work accidents.

🔥 Correlation heatmap to find relationships between satisfaction, projects, and churn.

🔎 Key Insights

Satisfaction Level has a strong negative correlation with churn — lower satisfaction leads to higher turnover.

Features like number of projects and average monthly hours also influence churn.

Employees with no promotions and low salary are more likely to leave.

🧠 Model Development
🧰 Methodology

Data Preprocessing:

Handled missing values, encoded categorical data, and normalized numeric values.

Feature Selection:

Identified key predictors using correlation and feature importance scores.

Model Training:

Used RandomForestClassifier for classification.

Model Evaluation:

Assessed using Accuracy, Precision, and F1 Score metrics.

Model Deployment (Future Scope):

The model can be integrated into HR dashboards or retention tools for real-time insights.

🎯 Project Objectives

Develop a predictive model for employee churn.

Identify at-risk employees to enable proactive retention.

Use analytics to guide HR decision-making.

Enhance employee satisfaction and organizational stability.

🔮 Future Scope

Improve model accuracy using advanced techniques (XGBoost, Logistic Regression).

Balance data distribution with oversampling/undersampling methods.

Deploy using Flask or Streamlit for interactive prediction.

Integrate with Power BI dashboards for real-time HR insights.

🧭 Conclusion

The developed Employee Churn Prediction Model effectively identifies employees at risk of leaving based on various behavioral and performance factors.
By leveraging these insights, organizations can design targeted retention strategies, reduce turnover, and foster a more satisfied and stable workforce.
