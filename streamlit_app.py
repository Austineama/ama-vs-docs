import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ama VS Dashboard", layout="wide")
st.title("📊 Ama VS Project Dashboard")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")
    st.dataframe(df)

    if st.button("Show Summary"):
        st.write(df.describe())

st.markdown("---")
st.caption("Powered by Streamlit • GitHub • Python")
