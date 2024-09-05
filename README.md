### Hazardous Near Earth Objects (NEOs) Forecasting Project

## Overview
This project aims to develop a machine learning model to predict whether near-Earth objects (NEOs) are dangerous or not. We use a real dataset from NASA that includes information on objects observed between 1910 and 2024.

## Project description
This project analyzes data on 338,199 space objects observed near Earth. Our goal is to build a model that can accurately predict whether an object is classified as “dangerous” by NASA. This mission is vital to planetary defense efforts.

## Requirements
- Python 3.x
- Libraries: pandas, numpy, scikit-learn, matplotlib, seaborn, matplotlib.pyplot

## Project Steps
Data Importing and Cleaning

Imported the dataset and handled missing values to ensure the data is clean and ready for analysis.
Exploratory Data Analysis (EDA)

Explored the dataset using visualization libraries like Matplotlib and Seaborn.
Generated informative graphs to identify patterns, trends, and potential correlations.
Data Preprocessing

Selected important features for model training.
Encoded categorical variables and normalized numerical features.
Addressed class imbalance using techniques such as:
SMOTE (Synthetic Minority Over-sampling Technique) for oversampling.
Class Weight Adjustment.
Used Balanced Accuracy as a performance metric.
Model Training and Evaluation

Trained multiple machine learning models including:

- Random Forest[Accuracy: 0.9182867872085632]
- Logistic Regression[Accuracy: 0.8706071940744246]
- Decision Tree [Accuracy: 0.8846079924304026]
  
Evaluated model performance using:
Precision, Recall, F1-Score
AUC-ROC Curve
Balanced Accuracy
Selected the best-performing model based on these metrics.

## Results
Best Model: Random Forest
Balanced Accuracy: [Accuracy: 0.6]
Precision: [Accuracy:  0.92]
Recall: [Recall: 0.88]
F1-Score: [F1-Score: 0.92]
AUC-ROC: [AUC-ROC: 0.95]

##Key Findings and Insights
The dataset was highly imbalanced, with far fewer hazardous objects compared to non-hazardous ones.
The Random Forest model provided the best performance, handling the class imbalance effectively.
Balanced accuracy was a key metric in evaluating the performance of the model due to the imbalance in the target variabl

## Conclusion
This project demonstrated the use of machine learning models to predict hazardous NEOs. By addressing data imbalance and using appropriate evaluation metrics, the project successfully identified the best model for the task.

## Contact
[Abdul Rahman Ahmed] - [abdulrahmannassar202@gmail.com]

## Project link:
https://github.com/Abdulrahman181/Predicting-Hazardous-NEOs
