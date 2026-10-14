from fastapi import FastAPI
from pydantic import BaseModel, Field
import pickle

# import the ml model
with open("iris_model.pkl", "rb") as f:
      model = pickle.load(f)

app  = FastAPI(title = "Iris Classification API")

# pydantic model to validate incomong data
# Input data Schema
class IrisInput(BaseModel):
    sepal_length: float = Field(..., gt=0, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, description= "Petal length in cm")
    petal_width: float = Field(..., gt=0, description= "Petal width in cm")


# home route
@app.get("/")
def home():
     return {"message": "Iris classification API is running"}


# Prediction route
@app.post("/predict")
def predict(data: IrisInput):
    input_data = [[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]]

    prediction = model.predict(input_data)[0]
    species = ["Setosa", "Versicolor", "Virginica"]

    predicted_species = species[prediction]

    return {"prediction": predicted_species}