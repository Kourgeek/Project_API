import fastapi
from pydantic import BaseModel
from model import np,reg

class Students(BaseModel):
    Age: float
    Gender: float
    Ethnicity: float
    Absences: float


app = fastapi.FastAPI()

@app.get("/")
def check_api():
    return "WORK"

@app.post("/score")
def get_GPA_score(inputs: Students):

    features =  [
        inputs.Age,
        inputs.Gender,
        inputs.Ethnicity,
        inputs.Absences
    ]

    prediction = reg.predict(np.array([features]))

    return prediction.tolist()[0]
