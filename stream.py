import joblib
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Suicide Analysis",
    page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

# Load the pre-trained model
file_name = "finalized_model.sav"
loaded_model = joblib.load(file_name)

# Title and header
st.title("Suicide Analysis")
st.header("Detect Suicidal Text")

# Description
st.markdown("Enter text below to analyze whether it contains suicidal content or not.")

# Text input
text_input = st.text_area("Enter your text here:", height=150)

# Prediction button
if st.button("Analyze"):
    # Perform prediction
    result = loaded_model.predict([text_input])[0]
    
    # Display result
    if result == 1:
        st.error("The text contains suicidal content.")
    else:
        st.success("The text does not contain suicidal content.")

# Footer
st.markdown(
    """
    <style>
        .stApp footer {
            visibility: hidden;
        }
    </style>
    """,
    unsafe_allow_html=True
)



