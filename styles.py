import streamlit as st

# Define colors
primary_color = "#0e1133"
text_color = "#ffffff"
secondary_color = "#000000"


# Colors
colors = ["#000000", "#CFE8FF", "#0000FF", "#FFD700"]


# Sidebar styles
def apply_sidebar_styles():
    st.sidebar.markdown(
        f"""
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {{
            background-color: {st.session_state.color} 
        }}
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {{
            background-color: {st.session_state.color}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Add fonts
def add_fonts():
    st.markdown(
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap">',
        unsafe_allow_html=True,
    )
