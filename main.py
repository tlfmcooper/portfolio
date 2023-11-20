import streamlit as st
from data import projects, stack, categories
from styles import add_fonts, apply_sidebar_styles
from utils import (
    set_page_config,
    add_custom_html_to_head,
    add_logo_to_sidebar,
    initialize_session_state,
    apply_sidebar_styles,
    add_fonts,
    display_projects,
    display_resume,
    display_tech_stack,
    display_contact_form,
    display_direct_email_link,
    display_social_media_icons,
    display_footer,
)


def main():
    set_page_config()
    add_custom_html_to_head()
    add_logo_to_sidebar()
    initialize_session_state()
    apply_sidebar_styles()
    add_fonts()
    display_projects(projects)
    display_resume()
    display_tech_stack(stack)
    display_contact_form()
    display_direct_email_link()
    display_social_media_icons()
    display_footer()


if __name__ == "__main__":
    main()
