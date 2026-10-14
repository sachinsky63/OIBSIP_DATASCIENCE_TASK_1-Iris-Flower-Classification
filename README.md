<<<<<<< HEAD
# 🌸 Iris Flower Classification using Machine Learning

## 📌 Project Overview

This project predicts the species of an Iris flower using Machine Learning classification algorithms. It uses the Iris dataset and compares multiple models to classify flowers into three species: Setosa, Versicolor, and Virginica.

The project includes Exploratory Data Analysis (EDA), data visualization, model training, evaluation, a FastAPI backend, and a Streamlit frontend.

## 🎯 Objective

To build a Machine Learning application that predicts Iris flower species based on four input measurements:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- FastAPI
- Streamlit
- Pydantic
- Pickle
- Git and GitHub

## 📊 Dataset

The project uses the built-in Iris dataset provided by Scikit-learn.

The dataset contains 150 samples, four numerical features, and three target classes:

1. Iris Setosa
2. Iris Versicolor
3. Iris Virginica

## 🔍 Exploratory Data Analysis (EDA)

The following steps were performed:

- Checked dataset shape and data types.
- Identified missing values.
- Generated descriptive statistics.
- Created pair plots to visualize relationships between features.
- Used box plots to compare measurements across species.
- Examined the feature distributions and class separation.

## 🤖 Machine Learning Models

Three classification algorithms were trained and evaluated:

1. Logistic Regression
2. K-Nearest Neighbors (KNN)
3. Decision Tree Classifier

### Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

The models were compared using their weighted F1 scores.

The trained Logistic Regression model was initially saved as `iris_model.pkl`. The saved model is loaded by the FastAPI backend for making predictions.

## 🚀 Application Features

- Predicts Iris flower species from user-provided measurements.
- Provides a REST API using FastAPI.
- Validates input values using Pydantic.
- Offers an interactive web interface using Streamlit.
- Displays the predicted flower species.
- Uses a saved model without retraining for every prediction.
=======
# 🚗 Car Price Prediction Using Machine Learning

## 📌 Project Overview
This project predicts the estimated selling price of a used car based on its features using Machine Learning. It uses data preprocessing, exploratory data analysis (EDA), feature engineering, and regression models to estimate car prices.

## 🎯 Objectives
- Analyze used car data and identify important factors affecting prices.
- Clean and preprocess the dataset.
- Build and evaluate Machine Learning regression models.
- Provide an interface for entering car details and estimating the selling price.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Jupyter Notebook
- Streamlit
- FastAPI (if included in the final project)

## 📊 Dataset
The dataset contains information about used cars, including:

- `name` — Car name
- `year` — Manufacturing year
- `selling_price` — Selling price
- `km_driven` — Kilometers driven
- `fuel` — Fuel type
- `seller_type` — Type of seller
- `transmission` — Manual or automatic
- `owner` — Previous ownership information

## ⚙️ Project Workflow
1. Load and inspect the dataset.
2. Clean data and check for duplicate records.
3. Perform Exploratory Data Analysis (EDA).
4. Create features such as car age and brand.
5. Encode categorical variables and preprocess numerical features.
6. Train regression models, including Linear Regression and Random Forest Regressor.
7. Evaluate model performance using MAE, RMSE, and R² score.
8. Develop a user interface to estimate used car prices.
>>>>>>> 2c549a1c7eac7a87d6a495ccec6ee0e9d79caaf3

## 📁 Project Structure

```text
SachinKumarYadav_Task_1/
│
├── app.py                 # FastAPI backend
├── frontend.py            # Streamlit frontend
├── iris_model.pkl         # Saved ML model
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── Iris_Classification.ipynb  # EDA and model training notebook
```

*Note: Update the notebook filename if your actual file has a different name.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Task_1_Iris_classification
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Install Dependencies
=======
Task_3_Car_price_prediction/
├── app.py
├── car_price_model.pkl
├── cars dataset.csv
├── car_price_prediction.ipynb
├── requirements.txt
└── README.md
```

*Update the filenames above to match the actual files in your repository.*

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Task_3_Car_price_prediction
```

### 2. Install dependencies


```bash
python -m pip install -r requirements.txt
```
If necessary, install the dependencies individually:

```bash
python -m pip install fastapi uvicorn streamlit requests pandas matplotlib seaborn scikit-learn
```

### 3. Start the FastAPI Backend

```bash
python -m uvicorn app:app --reload
```

The backend will run at:

`http://127.0.0.1:8000`

### 4. Test the API

Open the interactive API documentation:

`http://127.0.0.1:8000/docs`

Use the `POST /predict` endpoint to submit flower measurements.

Example request:

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Example response:

```json
{
  "prediction": "Setosa"
}
```

### 5. Start the Streamlit Frontend

Open a second terminal and run:

```bash
python -m streamlit run frontend.py
```

The frontend will usually be available at:

`http://localhost:8501`

Keep the FastAPI backend running while using the Streamlit application.

## 📈 Results

The project compares Logistic Regression, KNN, and Decision Tree using multiple classification metrics. The trained model is saved as a pickle file and used for real-time predictions through the API.

Actual performance metrics can be added here after running the notebook.

## 🔮 Future Improvements

- Add cross-validation for more reliable model evaluation.
- Improve the interface with interactive charts.
- Deploy the FastAPI backend and Streamlit frontend online.
- Add model performance visualizations.
- Introduce automated testing for the prediction API.

## 👨‍💻 Author

**Sachin Kumar Yadav**

- GitHub: [sachinsky63](https://github.com/sachinsky63)
- LinkedIn: [Sachin Kumar Yadav](https://www.linkedin.com/in/sachin-kumar-yadav-sky/)

## 📜 Acknowledgements

This project was developed as part of the **Oasis Infobyte Data Science Internship**, Task 1: Iris Flower Classification.

## 📄 License

This project is intended for educational and learning purposes.
=======
### 3. Run the Streamlit application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

## 📈 Model Evaluation
The models are evaluated using:

- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **RMSE (Root Mean Squared Error):** Measures prediction error while penalizing larger errors.
- **R² Score:** Measures how well the model explains variation in car prices.

Add your actual evaluation scores after running the notebook.

## 🔮 Future Improvements
- Improve prediction accuracy through hyperparameter tuning.
- Add more vehicle features and recent market data.
- Improve the user interface and input validation.
- Deploy the application online.

## 👨‍💻 Internship Project
This project is part of the **Oasis Infobyte Data Science Internship — Task 3: Car Price Prediction**.

## ⚠️ Disclaimer
Predicted prices are estimates based on the training dataset and may differ from actual market prices.
>>>>>>> 2c549a1c7eac7a87d6a495ccec6ee0e9d79caaf3
