import streamlit as st
import pandas as pd
from crisis_dataset import crisis_data

st.set_page_config(page_title="CrisisDetect AI", layout="wide")
st.title("🌍 CrisisDetect AI — Real-Time Crisis Feed")

df = pd.DataFrame(crisis_data)
st.dataframe(df)
