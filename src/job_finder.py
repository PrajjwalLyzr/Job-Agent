from utils import get_file_name
import os
import pypdf
import json
from serpapi import GoogleSearch
from job_agent import JobSearchAgent

def JobFinder(OPENAI_API_KEY, LYZR_KEY, SERP_KEY):
    job_search_agent = JobSearchAgent(APIKey=OPENAI_API_KEY, LyzrKey=LYZR_KEY)

    resume_pdf_content = ""
    file_name = get_file_name(directory="ResumeData")
    file_path = os.path.join("ResumeData", file_name)

    with open(file_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page in range(len(pdf_reader.pages)):
            resume_pdf_content += pdf_reader.pages[page].extract_text()
    
    job_role_query = job_search_agent.job_role_finder_agent(resumeData=resume_pdf_content)

    # return job_role_query

    if job_role_query:
        params = {
            "engine": "google_jobs",
            "q": job_role_query,
            "hl": "en",
            "ltype": "1",
            "api_key": SERP_KEY
            }
        
        search = GoogleSearch(params)
        serp_results = search.get_dict()

        if serp_results:
            job_output_json = job_search_agent.job_match_agent(searchJobData=serp_results,
                                                            resumeData=resume_pdf_content)
                

            if job_output_json:
                job_output_json_obj = json.loads(str(job_output_json))

                return job_output_json_obj

            else:
                raise "Type conversion error for: JSON"
            
        else:
            raise "Agent not able to match the jobs"

    else:
        raise "Job Role are not found"

    