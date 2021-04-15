
# Fraud Detection of Transactions With Azure ML

The financial industry is shifting currently towards machine learning solutions and is trying to become data driven. <br>
With that shift, previously manual tasks are being passed down to machine learning models. <br>
One of these tasks is being able to detect if a transaction is fraudulent or not so that customers are not charged for items that they did not purchase.. <br>
The names of the columns though for security reasons have been removed. <br>
Usually in business cases like these we can expect demographic data, transaction speed, amount, location, etc <br>
Here though we are not able to reverse engineer that since the data have been under PCA transformation<br>


## Dataset

### Overview

As mentioned before the dataset is from a kaggle published problem to solve. <br>
I tried to load the dataset in my google drive and then access it from the notebook but I had issues with that so <br>
as can be seen in the screeshot below I have added the dataset manually in the azure ML studio. <br>

The dataset contains only numerical input variables which are the result of a PCA transformation. <br>
Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise. <br>

![](Dataset1.png)

![](Dataset2.png)


### Task

As said before the task is to identify fraudulent trasnactions. Since the datase thas already been preprocessed we will be using all the columns.<br>
Although in the extra suggestions we could definitely apply feature selection as a step. <br>

### Access

The dataset is quire large (140Mb csv file). I tried to upload it in my google drive and feed it from a link but there issues with the format. <br>
So I did load the dataset manualy in the Azure Studio dataset section.

## Automated ML

Below you can see our primary metrics for our model. <br>

We have choose weighted ACU for our metric since we have a very imbalanced dataset.<br> 
![](AutoMLparam.png)


### Results

In the photos below you can see the RunDetails.<br>
![](AutoML_RunDetails.png)


And also here are the information about the best model and its runID. <br>

![](ModelRunID.png)
![](RunID.png)

The parameters of the best model can be seen below. <br>

![](estimators1.png)
![](estimators2.png)

## Hyperparameter Tuning

We start by setting up the train.py file where we load split in test and train data and we prepare our data b converting our categorical data to ints and then to dummy vars so we can apply our logistic regression model since log reg is not dealing directly with categorical data as a tree would do. We use stratify because we have an imbalanced datset when it comes to our target variable and we want to have a nice distribution of both classes in our train and test sets On the hyperparameter side we use max_itter as 20 or 100 which is the amount of iterations for the log reg. And C indicated the inverse of regularisation, It’s a penalty term, meant to disincentivize and regulate against Overfitting.

The random parameter sampler will choose randomly parameters from the potential parameter space and it is not exahustive like the complete grid parameter sampling. That is decreasing dramatically the time of the training while keeping the accuracy of the model high enough to solve common industry problems.

The BanditPolicy basically states to check the job every X amount iterations here in our case is 2. If the primary metric which we chose is outside of the top 10% range the jon will be terminated. This saves us from continuing to explore hyperparameters that don't show promise of helping reach our target metric.

### Results

The results we got with the hyperdrive are better but are not realistic. The model overfits and there is a very dominant class, the non fraudulent one.
It needs to be balanced.


![](Hyper_RunDetails.png)


![](HyperBestModel.png)


![](hyperbestparam.png)


## Model Deployment

In this screenshot we see the model id.

![](ModelID.png)

The endpoint alive and healthy.

![](endpoint.png)

And the result of testing two entries in the deployed model.

![](results.png)

Before the deployment of the model we can save the environment dependencies. <br>
![](env.png)
![](env2.png)

## Screen Recording

This is the link to the screencast.<br>
https://drive.google.com/file/d/1Mkth-x_EM2Bc3k7CvAfY5Qh8iXvkHt63/view?usp=sharing


## Standout Suggestions

Feature engineering.
Feature importance.
Feature selection.
Feature corelation analysis.

