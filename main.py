import fastapi
import numpy as np
import pandas as pd
#from sklearn.linear_model import LinearRegression

#define model info

model_name  =  "Simple_model"
model_path = "Simple_ML_model.ipynb"

app = fastapi.FastAPI()

@app.get("/")
def check_api():
    return "WORK"

@app.get("/score")
def get_GPA_score(X):
    return 1
