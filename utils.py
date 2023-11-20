import streamlit as st
from PIL import Image
from data import categories
from styles import colors
import smtplib
from email.message import EmailMessage
import os, random


# Set page configuration
def set_page_config():
    st.set_page_config(
        page_title="Ali Kone's personal portfolio",
        page_icon=":chart_with_upwards_trend:",
    )


# Add custom HTML to the head section
def add_custom_html_to_head():
    st.markdown(
        """
        <head>
            <!-- Your custom HTML elements go here -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        </head>
    """,
        unsafe_allow_html=True,
    )


# Add logo to sidebar
def add_logo_to_sidebar():
    logo = Image.open("alkhaf_quants.jpeg")
    st.sidebar.image(logo)


# Initialize session state
def initialize_session_state():
    # Initialize session state
    if "submitted" not in st.session_state:
        st.session_state.submitted = False

    if "color" not in st.session_state:
        st.session_state.color = secondary_color


# Define colors
primary_color = "#0e1133"
text_color = "#ffffff"
secondary_color = "#000000"


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


# Display projects
def display_projects(projects):
    selected_section = st.sidebar.radio("Select Section", list(categories))
    st.title(f"{selected_section} Projects")

    # Filter projects based on selected category
    category_projects = [p for p in projects if p["category"] == selected_section]

    # Use expander for full project details
    for project in category_projects:
        with st.expander(project["title"]):
            st.write(project["description"])
            st.markdown(f"GitHub: [{project['title']}]({project['github']})")
            st.markdown(f"Website: [{project['title']}]({project['website']})")


# Display resume section
def display_resume():
    with st.container():
        st.header("Resume")
        resume_file = open("resume.pdf", "rb")
        st.download_button(
            label="Download Resume", data=resume_file, file_name="resume.pdf"
        )


# Display tech stack
def display_tech_stack(stack):
    with st.container():
        st.header("Tech Stack")
        for tech in stack:
            st.markdown(
                f"<p style='font-size: 16px; color:{random.choice(colors)};'>{tech}</p>",
                unsafe_allow_html=True,
            )


# Display contact form
def display_contact_form():
    if not st.session_state.submitted:
        with st.form("contact form"):
            st.header("Contact Me")

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Name")
                sender_email = st.text_input("Your Email")
            with col2:
                message = st.text_area("Message")

            submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state.submitted = True
            # Send email
            password = os.getenv("PYTHON_EMAIL")
            email = "developer0.ali1@gmail.com"

            # Create email message
            msg = EmailMessage()
            msg["Subject"] = f"New Message from {name}"
            msg["From"] = sender_email
            msg["To"] = email
            msg["Reply-To"] = sender_email
            msg.set_content(message)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(email, password)
                smtp.send_message(msg)
            # Show success message
    if st.session_state.submitted:
        st.success("Thank you for your message!")


# Display direct email link
def display_direct_email_link():
    st.markdown(
        """
        <a href="mailto:ali1.1kone@gmail.com?subject=Message from Portfolio&body=Hi, I'm getting in touch after visiting your portfolio site." target="_blank">
            <button>Send Direct Email</button>    
        </a>
    """,
        unsafe_allow_html=True,
    )


# Display social media icons
def display_social_media_icons():
    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Display social media icons
    st.markdown(
        """
        <a href="https://www.linkedin.com/in/ali-kone" target="_blank">
            <i class="fab fa-linkedin" style="font-size:2em; color: #0077b5; margin-right: 10px;"></i>
        </a>

        <a href="https://twitter.com/tlfmcooper" target="_blank">
            <i class="fab fa-twitter" style="font-size:2em; color: #1da1f2; margin-right: 10px;"></i>
        </a>
        
        <a href="https://github.com/tlfmcooper" target="_blank">
            <i class="fab fa-github" style="font-size:2em; color: #333; margin-right: 10px;"></i>
        </a>
        """,
        unsafe_allow_html=True,
    )


# Display footer
def display_footer():
    # Add spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Display footer
    footer = """
    <style>
    .reportview-container .main footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        height: 60px;  
    }
    </style>
    <footer>
        <p><i class="far fa-copyright"></i> 2023 Ali Kone</p>
    </footer>
    """
    st.markdown(footer, unsafe_allow_html=True)
