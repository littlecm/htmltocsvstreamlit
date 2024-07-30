import streamlit as st
import pandas as pd
from io import StringIO
import streamlit_shadcn_ui as ui

# Set page title and layout
st.set_page_config(page_title="Process Pro CRM HTML → CSV Converter", layout="centered")

# Title and file uploader
st.title("Process Pro CRM HTML → CSV Converter")
uploaded_file = st.file_uploader("Upload an HTML file", type=["html"])

# Function to convert HTML table to CSV
def table_to_csv(html_content):
    dfs = pd.read_html(html_content)
    if len(dfs) > 0:
        csv = dfs[0].to_csv(index=False)
        return csv
    return None

if uploaded_file is not None:
    # Read HTML file content
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    html_content = stringio.read()
    
    # Convert HTML table to CSV
    csv = table_to_csv(html_content)
    
    if csv:
        st.success("Conversion successful! Download the CSV file below.")
        st.download_button(label="Download CSV", data=csv, file_name="table.csv", mime="text/csv")
    else:
        st.error("No table found in the uploaded HTML file.")

trigger_btn = ui.button(text="Trigger Conversion", key="trigger_btn")

if trigger_btn:
    ui.alert_dialog(
        show=trigger_btn,
        title="Conversion Triggered",
        description="Your HTML file is being processed to convert to CSV.",
        confirm_label="OK",
        cancel_label="Cancel",
        key="alert_dialog1"
    )
