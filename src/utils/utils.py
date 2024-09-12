import streamlit as st
from st_social_media_links import SocialMediaIcons
import os
import shutil
from PIL import Image



def remove_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            st.error(f"Error while removing existing files: {e}")



def get_files_in_directory(directory):
    # This function help us to get the file path along with filename.
    files_list = []

    if os.path.exists(directory) and os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                files_list.append(file_path)

    return files_list



def save_uploaded_file(directory, uploaded_file):
    remove_existing_files(directory=directory)
    file_path = os.path.join(directory, uploaded_file.name)
    with open(file_path, "wb") as file:
        file.write(uploaded_file.read())
    # st.success("File uploaded successfully")



def get_file_name(directory):
    try:
        files = os.listdir(directory)
        file_names = [file for file in files if os.path.isfile(os.path.join(directory, file))]
        
        return file_names[0]
    
    except FileNotFoundError:
        return f"The directory '{directory}' does not exist."
    
    except Exception as e:
        return f"An error occurred: {e}"


def file_checker(directoryName):
    file = []
    for filename in os.listdir(directoryName):
        file_path = os.path.join(directoryName, filename)
        file.append(file_path)

    return file

def social_media(justify=None):
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all"
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=True, justify_content=justify) # will render in the sidebar


def css_for_card_layout():
    st.markdown(
                    """
                    <style>
                    .card {
                        background-color: #f9f9f9;
                        border-radius: 10px;
                        padding: 20px;
                        margin-bottom: 15px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    }
                    .card h2 {
                        color: #333;
                        margin-bottom: 10px;
                    }
                    .card p {
                        color: #666;
                        font-size: 16px;
                    }
                    .card a {
                        color: #007bff;
                        text-decoration: none;
                    }
                    .card a:hover {
                        text-decoration: underline;
                    }
                    </style>
                    """,
                    unsafe_allow_html=True,
                )          


def social_media_page():
    # This function will help you to render socila media icons with link on the app
    social_media_links = [
    "https://github.com/LyzrCore/lyzr",
    "https://www.youtube.com/@LyzrAI",
    "https://www.instagram.com/lyzr.ai/",
    "https://www.linkedin.com/company/lyzr-platform/posts/?feedView=all",
                        ]   

    social_media_icons = SocialMediaIcons(social_media_links)
    social_media_icons.render(sidebar=False, justify_content="space-evenly")



def style_app():
    # You can put your CSS styles here
    st.markdown("""
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    [data-testid="stSidebar"][aria-expanded="true"]{
           min-width: 450px;
           max-width: 450px;
           background-color: #FAF0E6;
       }
    </style>
    """, unsafe_allow_html=True)



def page_config(layout = "centered"):
    st.set_page_config(
        page_title="Virtual Career Mentor",
        layout=layout,  # or "wide" 
        initial_sidebar_state="auto",
        page_icon="./logo/lyzr-logo-cut.png"
    )



def template_end():
    st.sidebar.markdown("### This app is build by using Lyzr's Agent API ")

    st.sidebar.markdown(
        """
        <style>
        .button-container {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
        }
        .button-column {
            flex: 1;
            margin-right: 5px;
        }
        .button-column:last-child {
            margin-right: 0;
        }
        .sidebar-button {
            display: block;
            width: 100%;
            padding: 10px;
            margin: 5px 0;
            text-align: center;
            color: white;
            background-color: #ffffff;
            border: none;
            border-radius: 5px;
            text-decoration: none;
        }
        .sidebar-button:hover {
            background-color: #7458E8;
        }
        </style>

        <div class="button-container">
            <div class="button-column">
                <a class="sidebar-button" href="https://www.lyzr.ai/" target="_blank">Lyzr</a>
                <a class="sidebar-button" href="https://www.lyzr.ai/book-demo/" target="_blank">Book a Demo</a>
                <a class="sidebar-button" href="https://discord.gg/nm7zSyEFA2" target="_blank">Discord</a>
                <a class="sidebar-button" href="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw" target="_blank">Slack</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )