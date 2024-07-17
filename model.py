import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression

data = pd.read_csv("data.csv")
data = data[["Age","Gender","Ethnicity","Absences","GradeClass"]]

# train | target
X = data[["Age","Gender","Ethnicity","Absences"]]
y =  data ["GradeClass"]

reg = LinearRegression().fit(X,y)



