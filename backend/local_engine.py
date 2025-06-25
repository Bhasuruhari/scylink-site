TARA_LIBRARY = {
    "tcu": [
        {
            "category": "Spoofing",
            "description": "Attacker impersonates backend cloud system.",
            "impact": "Malicious update injection.",
            "mitigation": "Use mutual TLS.",
            "iso_clause": "Clause 15 – Risk Treatment"
        }
    ],
    "adas ecu": [
        {
            "category": "Tampering",
            "description": "Malicious input from compromised sensor can trigger unsafe decision.",
            "impact": "Loss of safety function.",
            "mitigation": "Input validation, integrity check.",
            "iso_clause": "Clause 7 – Risk Assessment"
        }
    ]
}

def get_threats_from_tara(asset_name: str):
    return TARA_LIBRARY.get(asset_name.strip().lower(), [])
