import streamlit as st
import joblib

# Load the trained machine learning model
model = joblib.load("model_diabetics.pkl")

# Define custom CSS for the background image
background_image = "website_background_A.jpg"
background_css = f"""
    <style>
    .stApp {{
        background-image: url({background_image});
        background-size: cover;
    }}
    </style>
"""
st.markdown(background_css, unsafe_allow_html=True)

# Set the app title and page layout
st.set_page_config(
    page_title="Diabetes Prediction App",
    layout="wide",
    initial_sidebar_state="expanded"  # Expand the sidebar by default
)

# Define the main content layout with custom CSS styles
st.markdown(
    """
    <style>
    /* Customize the background color of the main content */
    .main {
        background-color: rgba(255, 255, 255, 0.7); /* Add a semi-transparent white overlay */
        padding: 2rem;
    }

    /* Style the title text */
    .title {
        font-size: 36px;
        color: #0074e4;
    }

    /* Style the sidebar */
    .sidebar .sidebar-content {
        background-color: #0074e4;
        color: white;
    }

    /* Style the sidebar header */
    .sidebar .sidebar-content .sidebar-title {
        color: white;
    }

    /* Style the input fields */
    .stNumberInput input, .stNumberInput label {
        background-color: #fff;
        color: #0074e4;
    }

    /* Style the 'Predict' button */
    .stButton button {
        background-color: #0074e4;
        color: white;
        font-weight: bold;
    }

    /* Style the success message */
    .stAlert.success {
        background-color: #3cba54;
        color: white;
    }

    /* Style the error message */
    .stAlert.error {
        background-color: #db3236;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Define the main content
st.markdown('<p class="title">Diabetes Prediction Web App</p>', unsafe_allow_html=True)
st.markdown("Enter patient information:")

# Define input fields for patient information
col1, col2 = st.columns(2)
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 0)
    glucose = st.number_input("Glucose Level", 0, 300, 0)
    blood_pressure = st.number_input("Blood Pressure", 0, 150, 0)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 0)
with col2:
    insulin = st.number_input("Insulin Level", 0, 500, 0)
    bmi = st.number_input("BMI", 0.0, 50.0, 0.0)
    age = st.number_input("Age", 0, 120, 0)
    diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", 0.0, 2.0, 0.0)

# Make predictions
if st.button("Predict"):
    input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age, diabetes_pedigree_function]]
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("The patient is likely to have diabetes.")
    else:
        st.success("The patient is likely not to have diabetes.")
