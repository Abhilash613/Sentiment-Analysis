import streamlit as st
import pickle
import pandas as pd
import time

# Load the model
model_path = "C:/Users/adita/OneDrive/Documents/VS CODE/MY PROJECT VS CODE/sentimental analysis/sentiment.pkl"

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

    # Check the column names in the DataFrame
    st.write("Column Names:", df.columns)

    # Assuming your column name is different, modify this line accordingly
    tweet_column_name = 'YOUR_COLUMN_NAME'

    # Perform malware detection for each tweet
    st.write("Malware detection Results:")
    for tweet in df[tweet_column_name]:
        start = time.time()
        prediction = model.predict([tweet])
        end = time.time()
        st.write(f"Tweet: {tweet}, Malware: {prediction[0]}, Detection Time: {round(end-start, 2)} seconds")
