*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Your Project Title Here

*TODO:* Write a short introduction to your project.
The project is not an original idea. It is coming from a kaggle compeition https://www.kaggle.com/mlg-ulb/creditcardfraud. <br>
The problem in hand is one of the most common machine learning problem to solve in the financial world: Is a transaction fraudulent or not? <br>

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
*TODO*: Explain about the data you are using and where you got it from.

As mentioned before the dataset is from a kaggle published problem to solve. <br>
I tried to load the dataset in my google drive and then access it from the notebook but I had issues with that so <br>
as can be seen in the screeshot below I have added the dataset manually in the azure ML studio. <br>

The dataset contains only numerical input variables which are the result of a PCA transformation. <br>
Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. <br>

### Task
*TODO*: Explain the task you are going to be solving with this dataset and the features you will be using for it.

As said before the task is to identify fraudulent trasnactions. Since the datase thas already been preprocessed we will be using all the columns.<br>
Although in the extra suggestions we could definitely apply feature selection as a step. <br>

### Access
*TODO*: Explain how you are accessing the data in your workspace.

## Automated ML
*TODO*: Give an overview of the `automl` settings and configuration you used for this experiment

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.

Feature engineering.
Feature importance.
Feature selection.
Feature corelation analysis.

