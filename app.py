# Imports
import streamlit as st
import pandas as pd

# Set a page title and icon
st.set_page_config(page_title = "Claudine x MarginEdge Dashboard", page_icon = '📊', layout = 'wide', initial_sidebar_state = 'expanded')

# Margin Edge Link Button
st.write("Step 1: Pick a CSV to Upload")
st.link_button("Go to Margin Edge", "https://app.marginedge.com/#/")

st.write("---")

# Upload a CSV
st.write("Step 2: Upload CSV")
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

st.write("---")

# Reading CSVs?

# Sidebar
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTtBQPspmf-qtxxZ1d-fkjDq3UrTyoN03XFhg&s")
st.sidebar.image("https://help.marginedge.com/hc/theming_assets/01HZKY1P3EJS99553QQ2GET0ET")
st.sidebar.subheader("**:blue[Categories]**")
page = st.sidebar.selectbox("Select a Category", ["Orders", "Performace", "Vendors", "Products", "Recipes", "Inventory"])
