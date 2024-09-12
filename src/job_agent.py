from lyzragentapi import LyzrAgentConfig


class JobSearchAgent:
    def __init__(self, APIKey, LyzrKey):
        self.Agent = LyzrAgentConfig(
            x_api_key=LyzrKey,
            llm_api_key= APIKey)
        
        self.environment = self.Agent.create_environment(name="Job Search",
                                               features=[{
                                                            "type": "TOOL_CALLING",
                                                            "config": {"max_tries": 3},
                                                            "priority": 0
                                                        }],
                                                        tools=["perplexity_search"])


    def job_role_finder_agent(self, resumeData):
        agent_prompt = f"You are an expert agent to scrape skills and experience from the given resume data:{resumeData}, and after sraping the skills and experience, you can decide which job role is suitable for this resume along with experience."

        role_finder_agent = self.Agent.create_agent(
            env_id=self.environment['env_id'],
            system_prompt=agent_prompt,
            name='Job Role Finder Agent'
        )

        response = self.Agent.send_message(
            agent_id=role_finder_agent['agent_id'],
            user_id="default_user",
            session_id="resume optimization session",
            message=f"Scrape the skills and experience from the given resume data: {resumeData}. [!Important] After scrapping the skills and exprience convert them into a suitable job role, make a one liner query which is having the job role and experience, query should not e more then 3 words. Ouput formate: '[[job role]] having [[experience]] of experience' "
            )


        return response['response']

    def job_match_agent(self, searchJobData, resumeData):
        agent_prompt = f"Given the following job search results and a candidate's resume data, identify which job descriptions or qualifications match the candidate's resume data. Consider the matching based on relevance to skills, experience, and job roles. Return a new JSON containing only those job listings with their description, qualifications, and apply links where there is a match between the candidate's resume summary and the job description or qualifications.[!Important] make sure the required job experiece is matched with the cadidate's experience"

        resume_agent = self.Agent.create_agent(
            env_id=self.environment['env_id'],
            system_prompt=agent_prompt,
            name='Job Search Agent'
        )

        response = self.Agent.send_message(
            agent_id=resume_agent['agent_id'],
            user_id="default_user",
            session_id="resume optimization session",
            message=f"""
                        Job Search Results (JSON): {searchJobData}

                        Candidate Resume Summary: {resumeData}

                        Please extract and filter the job listings where the job description or qualifications align with the candidate's resume data. [!Important] make sure the required job experiece is matched with the cadidate's experience. The output should be a JSON that includes only the relevant job listings with their description, qualifications, and apply link. [!Important] Don't provide anything other than JSON Object, just pure JSON object remove any prefix if have.
                        Create brief Job Descritption such as 2-3 liner JD, also add the responsibilities/skills in the description as well. [!Important] Ignore the expecting working experience in description, don't use that. Just a brief about job role, responsibilities and skills.

                        Output JSON will be:    {{ 
                                                    "matching_jobs": [
                                                        {{
                                                            "title": {{"Job Title"}},
                                                            "description":{{"Job Description"}},
                                                            "company_name": {{"Company Name"}},
                                                            "apply_link": {{"Apply link"}}
                                                        }},
                                                        {{
                                                            "title": {{"Job Title"}},
                                                            "description":{{"Job Description"}},
                                                            "company_name": {{"Company Name"}},
                                                            "apply_link": {{"Apply link"}}
                                                        }},
                                                        {{
                                                            "title": {{"Job Title"}},
                                                            "description":{{"Job Description"}},
                                                            "company_name": {{"Company Name"}},
                                                            "apply_link": {{"Apply link"}}
                                                        }},
                                                        {{
                                                            "title": {{"Job Title"}},
                                                            "description":{{"Job Description"}},
                                                            "company_name": {{"Company Name"}},
                                                            "apply_link": {{"Apply link"}}
                                                        }}
                                                    ]}}
                    """
                        )
        return response['response']
    

    def job_role_finder(self, resumeSummary):
        agent_prompt = "You are an AI agent that can extract key details from a resume, including job role, experience, skills, and qualifications. You should identify and summarize these details accurately from the resume data provided."

        job_role_agent = self.Agent.create_agent(
            env_id=self.environment['env_id'],
            system_prompt=agent_prompt,
            name='Job Role Agent'
        )

        response = self.Agent.send_message(
                agent_id=job_role_agent['agent_id'],
                user_id="default_user",
                session_id="resume optimization session",
                message=f"""Extract the job role and experience from the following resume summary, and write those in a single liner statement, such as job query:\n\n{resumeSummary}""")
        

        return response['response']