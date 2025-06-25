from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define input format
class AssetInput(BaseModel):
    asset_name: str

@app.post("/get-threat")
def get_threat(data: AssetInput):
    asset = data.asset_name.strip().lower()
    if asset == "tcu":
        return {
            "threats": [
                {
                    "category": "Spoofing",
                    "description": "Attacker impersonates OEM cloud to inject malicious updates.",
                    "mitigation": "Use mutual TLS; validate certificates.",
                    "iso_clause": "Clause 15 – Risk Treatment"
                }
            ]
        }
    else:
        return { "threats": [] }
