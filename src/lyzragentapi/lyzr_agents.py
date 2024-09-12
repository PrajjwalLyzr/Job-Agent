import requests
import json
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

agent_api_url = os.getenv('AGENT_API_URL')
provider = os.getenv('LLM_CONFIG_PROVIDER')
model = os.getenv('LLM_CONFIG_MODEL')
temperature = os.getenv('LLM_CONFIG_TEMPERATURE')
top_p = os.getenv('LLM_CONFIG_TOP_P')
env_url = os.getenv('AGENT_ENVIRONEMNT_URL')
agent_url = os.getenv('CREATE_AGENT_URL')
chat_url = os.getenv('AGENT_CHAT_URL')
task_url = os.getenv('AGENT_TASK_URL')

class LyzrAgentConfig:
    def __init__(self, x_api_key, llm_api_key):
        self.url = agent_api_url
        self.headers = {
            "accept": "application/json",
            "x-api-key": x_api_key
        }
        self.llm_api_key = llm_api_key

    def create_environment(self, name, features, tools=None):
        payload = json.dumps({
            "name": name,
            "features": features,
            "tools": tools,
            "llm_config": {
                            "provider": provider,
                            "model": model,
                            "config": {
                                "temperature": temperature,
                                "top_p": top_p
                            },
            "llm_api_key": self.llm_api_key
        }})

        url = env_url

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None

    def create_agent(self, env_id, system_prompt, name):
        payload = json.dumps({
            "env_id": env_id,
            "system_prompt": system_prompt,
            "name": name,
            "agent_persona": "",
            "agent_instructions": "",
            "agent_description": ""
        })

        url = agent_url

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None

    def send_message(self, agent_id, user_id, session_id, message):
        payload = json.dumps({
            "user_id": user_id,
            "agent_id": agent_id,
            "session_id": session_id,
            "message": message
        })

        url = chat_url

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None

    def create_task(self, agent_id, session_id, input_message):
        payload = json.dumps({
            "agent_id": agent_id,
            "session_id": session_id,
            "input": input_message
        })

        url = task_url

        response = requests.post(url, headers=self.headers, data=payload)

        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None