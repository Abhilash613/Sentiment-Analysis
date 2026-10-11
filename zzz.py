import streamlit as st
import pickle
import pandas as pd
import time

# Load the model
model_path = "D:\Learning project 2 group-06\Learning project 2 group-06\sentiment analysis of social media presence (Twitter)\sentimental analysis\sentiment.pkl"

@st.cache(allow_output_mutation=True)
def load_model(path):
    return pickle.load(open(path, "rb"))

model = load_model(model_path)

st.title('Malware detection')

# Create a file uploader
uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

if uploaded_file is not None:
    # Load CSV data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Perform sentiment analysis for each tweet
    st.write("Malware detection Results:")
    for tweet in df['Tweet']:
        start = time.time()
        prediction = model.predict([tweet])
        end = time.time()
        st.write(f"Tweet: {tweet}, Malware: {prediction[0]}, Detection Time: {round(end-start, 2)} seconds")
