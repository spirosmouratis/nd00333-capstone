# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import json
import logging
import os
import pickle
import numpy as np
import pandas as pd
import joblib

import azureml.automl.core
from azureml.automl.core.shared import logging_utilities, log_server
from azureml.telemetry import INSTRUMENTATION_KEY

from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
from inference_schema.parameter_types.pandas_parameter_type import PandasParameterType


input_sample = pd.DataFrame({ "Time": pd.Series([0.0], dtype="float64"), "V1": pd.Series([0.0], dtype="float64"),"V2": pd.Series([0.0], dtype="float64"),"V3": pd.Series([0.0], dtype="float64"),"V4": pd.Series([0.0], dtype="float64"),"V5": pd.Series([0.0], dtype="float64"),"V6": pd.Series([0.0], dtype="float64"),"V7": pd.Series([0.0], dtype="float64"),"V8": pd.Series([0.0], dtype="float64"),"V9": pd.Series([0.0], dtype="float64"),"V10": pd.Series([0.0], dtype="float64"),"V11": pd.Series([0.0], dtype="float64"),"V12": pd.Series([0.0], dtype="float64"),"V13": pd.Series([0.0], dtype="float64"),"V14": pd.Series([0.0], dtype="float64"),"V15": pd.Series([0.0], dtype="float64"),"V16": pd.Series([0.0], dtype="float64"),"V17": pd.Series([0.0], dtype="float64"),"V18": pd.Series([0.0], dtype="float64"),"V19": pd.Series([0.0], dtype="float64"),"V20": pd.Series([0.0], dtype="float64"),"V21": pd.Series([0.0], dtype="float64"),"V22": pd.Series([0.0], dtype="float64"),"V23": pd.Series([0.0], dtype="float64"),"V24": pd.Series([0.0], dtype="float64"),"V25": pd.Series([0.0], dtype="float64"),"V26": pd.Series([0.0], dtype="float64"),"V27": pd.Series([0.0], dtype="float64"),"V28": pd.Series([0.0], dtype="float64"),"Amount": pd.Series([0.0], dtype="float64")})
output_sample = np.array([0])
try:
    log_server.enable_telemetry(INSTRUMENTATION_KEY)
    log_server.set_verbosity('INFO')
    logger = logging.getLogger('azureml.automl.core.scoring_script')
except:
    pass


def init():
    global model
    # This name is model.id of model that we want to deploy deserialize the model file back
    # into a sklearn model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    path = os.path.normpath(model_path)
    path_split = path.split(os.sep)
    log_server.update_custom_dimensions({'model_name': path_split[-3], 'model_version': path_split[-2]})
    try:
        logger.info("Loading model from path.")
        model = joblib.load(model_path)
        logger.info("Loading successful.")
    except Exception as e:
        logging_utilities.log_traceback(e, logger)
        raise


@input_schema('data', PandasParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(data):
    try:
        result = model.predict(data)
        return json.dumps({"result": result.tolist()})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})