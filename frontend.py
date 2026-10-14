
import streamlit as st
import requests

st.set_page_config(
    page_title="Iris Flower Classification",
    page_icon="🌸",
    layout="centered"
)

st.title("🌸 Iris Flower Classification")
st.write("Predict the species of an Iris flower using Machine Learning.")

st.divider()

st.subheader("Enter Flower Measurements")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)", min_value=0.1, value=5.1, step=0.1
    )
    petal_length = st.number_input(
        "Petal Length (cm)", min_value=0.1, value=1.4, step=0.1
    )

with col2:
    sepal_width = st.number_input(
        "Sepal Width (cm)", min_value=0.1, value=3.5, step=0.1
    )
    petal_width = st.number_input(
        "Petal Width (cm)", min_value=0.1, value=0.2, step=0.1
    )

if st.button("Predict Species", type="primary", use_container_width=True):

    input_data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    API_URL = "http://127.0.0.1:8000/predict"

    try:
        response = requests.post(
            API_URL,
            json=input_data,
            timeout=10
        )
        response.raise_for_status()

        result = response.json()
        species = result["prediction"]

        st.success("Prediction completed successfully!")
        st.subheader(f"🌺 Predicted Species: {species}")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI backend is not running. Start the backend first.")

    except requests.exceptions.RequestException as error:
        st.error(f"API Error: {error}")

    except (KeyError, ValueError):
        st.error("Invalid response received from the API.")
