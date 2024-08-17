**Steps to Build and Deploy the Sentiment Analysis Model**

Environment Setup
.Create Project Directory
.Set Up Virtual Environment
.Install Required Packages

Data Preparation
  Download and Load IMDB Dataset: Use Kaggle CLI to download, then extract the dataset into a data/ directory.
Data Preprocessing:
 .Perform label encoding or one-hot encoding for sentiment labels.
 .Split the dataset into training and testing sets.
 .Tokenize the text data and pad sequences for model input.
Model Building and Training:
 LSTM Model: Build and train an LSTM model for sentiment analysis.
 Logistic Regression Model: Optionally, build and train a logistic regression model (script: train_logistic_regression.py).
Model Deployment with Flask
 Run Flask Application
 





