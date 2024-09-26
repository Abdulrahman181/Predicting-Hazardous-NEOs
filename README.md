## Hazardous Near Earth Objects (NEOs) Forecasting Project

# 🎯 Project Overview
  - This project aims to develop a machine learning model to predict whether near-Earth objects (NEOs) are dangerous or not.
  -  We use a real dataset from NASA that includes information on objects observed between 1910 and 2024.

# 📁 Project description
  - This project analyzes data on 338,199 space objects observed near Earth.
  - Our goal is to build a model that can accurately predict whether an object is classified as “dangerous” by NASA.
  -  This mission is vital to planetary defense efforts.

# 🛠️ Project Requirements
  - Python 3.x
  - Libraries:
    - pandas
    - numpy
    - scikit-learn
    - matplotlib
    - seaborn
    - matplotlib.pyplot

# 🧰 Project Steps
  - Data Importing and Cleaning
  - Imported the dataset and handled missing values to ensure the data is clean and ready for analysis.
  - Exploratory Data Analysis (EDA)
  - Explored the dataset using visualization libraries like Matplotlib and Seaborn.
  - Generated informative graphs to identify patterns, trends, and potential correlations.
  - Data Preprocessing
  - Selected important features for model training.
  - Encoded categorical variables and normalized numerical features.
  - Addressed class imbalance using techniques such as:
  - SMOTE (Synthetic Minority Over-sampling Technique) for oversampling.
  - Class Weight Adjustment.
  - Used Balanced Accuracy as a performance metric.
  - Model Training and Evaluation

# 💡Results and Analysis
  - Trained multiple machine learning models including:
    - Random Forest
    - Logistic Regression
    - Decision Tree 
  
   - Evaluated model performance using:
    - Precision, Recall, F1-Score
    - AUC-ROC Curve
    - Balanced Accuracy
    - Selected the best-performing model based on these metrics.

   - Best Model: Random Forest
    - Balanced Accuracy
    - Precision
    - Recall
    - F1-Score
    - AUC-ROC
     
## - Based on the model's predictions, we can enhance hazardous object detection and improve classification accuracy.

## 🔍 Key Findings and Insights
   - The dataset was highly imbalanced, with far fewer hazardous objects compared to non-hazardous ones.
   - The Random Forest model provided the best performance, handling the class imbalance effectively.
   - Balanced accuracy was a key metric in evaluating the performance of the model due to the imbalance in the target variabl

# 🔗 References
  - Dataset description and structure as per the project documentation.

# 📁 Repository Structure

├── data                       

├── notebooks   

└── README.md

# 🚀 Conclusion
  -This project demonstrated the use of machine learning models to predict hazardous NEOs.
  -By addressing data imbalance and using appropriate evaluation metrics, the project successfully identified the best model for the task.

# 💻 Contact
   - Abdul Rahman Ahmed 
   - abdulrahmannassar202@gmail.com

# 📌 Project link:
   - https://github.com/Abdulrahman181/Predicting-Hazardous-NEOs
