import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_threat_scenario_from_llm(asset_name: str) -> str:
    prompt = f"""
You are a cybersecurity expert specializing in ISO 21434 and STRIDE threat modeling.

Generate a structured threat scenario for: {asset_name}

Include:
- Threat Category
- Description
- Impact
- Mitigation
- ISO 21434 Clause
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]
