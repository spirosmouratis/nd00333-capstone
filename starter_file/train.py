import os
import argparse
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset
from azureml.core import Workspace, Dataset
from sklearn.linear_model import LogisticRegression

run = Run.get_context()

workspace = run.experiment.workspace

key="fraud-capstone"
description_text="Credit Card Fraud Detection Data"
dataset=workspace.datasets[key]
x=dataset.to_pandas_dataframe()
x=x.fillna(0)
y=x.pop("Class")

def main():
    # Add arguments to script
    parser=argparse.ArgumentParser()
    parser.add_argument('--C',type=float,default=1.0,help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter',type=int,default=100,help="Maximum number of iterations to converge")
    args=parser.parse_args()
    run.log("Regularization Strength:",np.float(args.C))
    run.log("Max iterations:",np.int(args.max_iter))
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=123,stratify=y)
    model=LogisticRegression(C=args.C,max_iter=args.max_iter).fit(x_train,y_train)
    accuracy=model.score(x_test,y_test)
    run.log("Accuracy",np.float(accuracy))
    
    
if __name__=='__main__':
    main()