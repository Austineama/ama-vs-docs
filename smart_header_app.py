import streamlit as st
import pandas as pd
import re
from io import BytesIO

def find_header_row(file, sheet_name, keywords, max_rows=30):
    preview = pd.read_excel(file, sheet_name=sheet_name, header=None, nrows=max_rows)
    for i, row in preview.iterrows():
        normalized_row = [str(cell).strip().upper() for cell in row]
        if all(any(keyword.upper() in cell for cell in normalized_row) for keyword in keywords):
            return i
    return None

def extract_cleaned_data(uploaded_files, keywords, max_rows=30):
    output_data = []
    for file in uploaded_files:
        try:
            sheet_name = 0
            header_row = find_header_row(file, sheet_name, keywords, max_rows)
            if header_row is not None:
                df = pd.read_excel(file, sheet_name=sheet_name, header=header_row)
                df["Source File"] = file.name
                output_data.append(df)
            else:
                st.warning(f"No header row found in {file.name}")
        except Exception as e:
            st.error(f"Error processing {file.name}: {e}")
    if output_data:
        combined_df = pd.concat(output_data, ignore_index=True)
        return combined_df
    return None

st.set_page_config(page_title="IbuAnyiNdaNda SEHE", layout="wide", page_icon="🧠")
st.image("logo.png", width=120)
st.title("🧠 IbuAnyiNdaNda - Smart Excel Header Extractor")
st.write("Upload Excel files. I will detect headers intelligently and combine your data.")

keywords_input = st.text_input("Enter keywords to detect header row (comma-separated):", "Date,BP,Pulse")
keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()]
uploaded_files = st.file_uploader("Upload Excel files", type=["xlsx"], accept_multiple_files=True)

if uploaded_files and keywords:
    st.info("Processing uploaded files...")
    cleaned_df = extract_cleaned_data(uploaded_files, keywords)

    if cleaned_df is not None:
        st.success("✅ Headers detected and data combined successfully!")
        st.dataframe(cleaned_df)

        st.subheader("📈 Summary Statistics")
        numeric_cols = cleaned_df.select_dtypes(include='number').columns
        st.write(cleaned_df[numeric_cols].describe())

        st.subheader("📊 Charts")
        col_option = st.selectbox("Select column to visualize", options=numeric_cols)
        if col_option:
            st.line_chart(cleaned_df[col_option])

        def convert_df_to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Combined')
            return output.getvalue()

        excel_data = convert_df_to_excel(cleaned_df)
        st.download_button("📥 Download Cleaned Excel", data=excel_data,
                           file_name="IbuAnyiNdaNda_Cleaned_Data.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.warning("No valid data extracted. Please check your files or keyword settings.")