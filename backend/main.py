from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from local_engine import get_threats_from_tara
from llm_client import get_threat_scenario_from_llm

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class AssetInput(BaseModel):
    asset_name: str
    use_ai: bool = False  # Toggle AI on or off

@app.post("/get-threat")
def get_threat(data: AssetInput):
    if data.use_ai:
        scenario = get_threat_scenario_from_llm(data.asset_name)
        return {"asset": data.asset_name, "source": "AI", "scenario": scenario}
    else:
        threats = get_threats_from_tara(data.asset_name)
        return {"asset": data.asset_name, "source": "TARA Library", "threats": threats}
