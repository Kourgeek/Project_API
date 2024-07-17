import fastapi
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#import data

data = pd.read_csv("data.csv")
data = data[["Age","Gender","Ethnicity","Absences","GradeClass"]]

# train | target
X = data[["Age","Gender","Ethnicity","Absences"]]
y =  data ["GradeClass"]

# train model
reg = LinearRegression().fit(X,y)

#X = [18, 1,1,10]

app = fastapi.FastAPI()

@app.get("/")
def check_api():
    return "WORK"

@app.post("/score")
def get_GPA_score(X: list):
    return float(reg.predict(np.array([X])))
