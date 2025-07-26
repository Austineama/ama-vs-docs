
import streamlit as st
import pandas as pd
import os
from smart_indexing import auto_index_dataframe

st.set_page_config(page_title="IbuAnyiNdaNda SEHE", layout="wide")

st.title("🧠 IbuAnyiNdaNda SEHE - Smart Header Extractor & Indexing App")

st.markdown("""
Welcome to the **IbuAnyiNdaNda SEHE** app – a powerful tool for dynamically detecting headers,
standardizing units, and indexing engineering datasets using either Depth or DateTime.
Upload multiple Excel files and let the intelligence do the heavy lifting.
""")

uploaded_files = st.file_uploader("📁 Upload Excel Files", type=["xlsx"], accept_multiple_files=True)

keywords = st.text_input("🔍 Enter header keywords to detect (comma-separated)", "DEPTH,TIME")

if uploaded_files:
    keyword_list = [k.strip().upper() for k in keywords.split(',') if k.strip()]
    combined_df = pd.DataFrame()

    for uploaded_file in uploaded_files:
        try:
            st.write(f"Processing: {uploaded_file.name}")
            preview = pd.read_excel(uploaded_file, header=None, nrows=30)
            header_row = None
            for i, row in preview.iterrows():
                normalized = [str(cell).strip().upper() for cell in row]
                if all(any(kw in cell for cell in normalized) for kw in keyword_list):
                    header_row = i
                    break
            if header_row is not None:
                df = pd.read_excel(uploaded_file, header=header_row)
                df = auto_index_dataframe(df)
                df["Source File"] = uploaded_file.name
                combined_df = pd.concat([combined_df, df], ignore_index=True)
            else:
                st.warning(f"Header not found in {uploaded_file.name}")
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")

    if not combined_df.empty:
        st.success("✅ All files processed and indexed successfully!")
        st.dataframe(combined_df.head(50))

        file_format = st.radio("📤 Download Format", ["CSV", "Excel"])
        if file_format == "CSV":
            csv = combined_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download Combined CSV", data=csv, file_name="combined_output.csv", mime="text/csv")
        else:
            excel_path = "combined_output.xlsx"
            combined_df.to_excel(excel_path, index=False)
            with open(excel_path, "rb") as f:
                st.download_button("Download Combined Excel", data=f, file_name="combined_output.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.warning("No valid data to display.")
else:
    st.info("Upload files to begin.")
