import numpy as np
import pandas as pd
import sys
from sklearn.linear_model import LinearRegression

path = "/workspaces/Projects/data/data.csv"

sys.path.append(path)

data = pd.read_csv(path)
data = data[["Age","Gender","Ethnicity","Absences","GradeClass"]]

# train | target
X = data[["Age","Gender","Ethnicity","Absences"]]
y =  data ["GradeClass"]

reg = LinearRegression().fit(X,y)



