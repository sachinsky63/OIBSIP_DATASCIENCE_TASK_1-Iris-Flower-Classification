
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


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import traceback

app = FastAPI(title="Car Price Prediction API")

# Load the trained machine learning pipeline
model = joblib.load("car_price_model.pkl")


# Input data
class CarDetails(BaseModel):
    brand: str
    car_age: int = Field(..., ge=0, le=100)
    km_driven: int = Field(..., ge=0)
    fuel: str
    seller_type: str
    transmission: str
    owner: str


# Home route
@app.get("/")
def home():
    return {"message": "Car Price Prediction API is running!"}


# Predict car price
@app.post("/predict")
def predict_price(car: CarDetails):
    try:
        # Convert input into a DataFrame
        input_data = pd.DataFrame([car.model_dump()])

        # Predict price using the trained model
        prediction = model.predict(input_data)[0]

        return {
            "predicted_selling_price": round(float(prediction), 2),
            "currency": "INR"
        }

    except Exception as e:
        # Print the actual error in the terminal
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

