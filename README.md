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
