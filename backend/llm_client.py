import os
from openai import OpenAI

# Read the environment variable directly (Render handles this)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def get_threat_scenario_from_llm(asset_name: str) -> str:
    prompt = f"""
You are a cybersecurity expert specializing in ISO 21434 and STRIDE threat modeling.

Generate a structured threat scenario for this automotive asset:

Asset: {asset_name}

Include:
- Threat Category
- Description
- Impact
- Mitigation
- ISO 21434 Clause
"""


    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[AI ERROR] {str(e)}"
