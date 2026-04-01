import streamlit as st
import streamlit.components.v1 as components

# Set page to wide mode
st.set_page_config(layout="wide", page_title="KrishiAmrut")

# The HTML code we built (Paste the entire HTML content here)
html_code = """
"""

# Render the HTML
components.html(html_code, height=2000, scrolling=True)