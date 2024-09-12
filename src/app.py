import streamlit as st
import os
from utils import (social_media,
                   template_end,
                   page_config,
                   style_app,
                   save_uploaded_file,
                   remove_existing_files,
                   css_for_card_layout)
from dotenv import load_dotenv
from job_finder import JobFinder

load_dotenv()

page_config()
style_app()

openai_api_key = os.getenv('OPENAI_API_KEY')
lyzr_x_key = os.getenv('X_API_Key')
serp_api_key = os.getenv('SERP_KEY')


image = "./src/logo/lyzr-logo.png"
st.image(image=image, width=250)


ResumeData = "ResumeData"
os.makedirs(ResumeData, exist_ok=True)


st.header("Job Agent")
st.markdown("##### Powered by [Lyzr](https://www.lyzr.ai/)")
st.markdown('---')

resume_file = st.file_uploader(label="Upload your resume pdf file", type=["pdf"])

# Get Job button
if st.button("Search Jobs"):
    if resume_file:
        remove_existing_files(directory=ResumeData)
        save_uploaded_file(directory=ResumeData, uploaded_file=resume_file)
        with st.spinner("🕵🏼‍Searching Jobs For You..."):
            jobs = JobFinder(OPENAI_API_KEY=openai_api_key, LYZR_KEY=lyzr_x_key, SERP_KEY=serp_api_key)
            
            if jobs:
                st.markdown("---")  
                # CSS for card layout
                css_for_card_layout()
                
                for job in jobs["matching_jobs"]:
                    st.markdown(f"""
                        <div class="card">
                            <h2>{job['title']}</h2>
                            <p><strong>Company:</strong> {job['company_name']}</p>
                            <p><strong>Description:</strong> {job['description']}</p>
                            <p><a href="{job['apply_link']}" target="_blank">Apply Here</a></p>
                        </div>
                        """, unsafe_allow_html=True)

                    st.markdown("---")

    else:
        st.warning('Please provide the resume')
        remove_existing_files(directory=ResumeData)



template_end()
st.sidebar.markdown('---')
social_media(justify="space-evenly")

