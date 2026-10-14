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

## 📁 Project Structure

```text
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
