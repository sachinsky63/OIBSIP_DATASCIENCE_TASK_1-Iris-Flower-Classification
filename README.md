# 🌸 Iris Flower Classification

## 📌 Project Overview
This project uses Machine Learning to classify Iris flowers into three species based on their sepal and petal measurements.

The three Iris species are:
- Iris Setosa
- Iris Versicolor
- Iris Virginica

This project was developed as **Task 1 of the Oasis Infobyte Data Science Internship**.

## 🎯 Objective
To build a machine learning classification model that predicts the species of an Iris flower using four input features:
- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook
- FastAPI
- Streamlit
- Pickle

## 📂 Project Structure

```text
SachinKumarYadav_Task_1/
│
├── iris_classification.ipynb
├── iris_model.pkl
├── app.py
├── frontend.py
├── requirements.txt
└── README.md
```

## 🤖 Machine Learning Model
The Iris dataset is used to train a classification model. The trained model is saved as `iris_model.pkl` and loaded by the FastAPI application to make predictions.

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sachinsky63/OIBSIP_DATASCIENCE_TASK_1-Iris-Flower-Classification.git

Open the repository and navigate to the Iris project folder.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the FastAPI Backend

```bash
python -m uvicorn app:app --reload
```

Open the API documentation in your browser:

http://127.0.0.1:8000/docs

### 4. Start the Streamlit Frontend

Open a **second terminal** in the project folder and run:

```bash
streamlit run frontend.py
```

The Streamlit interface will open in your browser. Enter the flower measurements to predict the Iris species.

## 📊 Input Features
| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal |
| Sepal Width | Width of the sepal |
| Petal Length | Length of the petal |
| Petal Width | Width of the petal |

## 💡 Applications
- Learning supervised machine learning
- Understanding classification algorithms
- Building simple ML applications with FastAPI and Streamlit
- Demonstrating model deployment basics

## 👨‍💻 Author
**Sachin Kumar Yadav**

- GitHub: https://github.com/sachinsky63
- Internship: Oasis Infobyte — Data Science Internship

## 📄 Disclaimer
This project was developed for educational purposes as part of a Data Science internship task.
