import requests

API_TOKEN = ""

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

def query(payload):
    response = requests.post(
        API_URL,
        headers=headers,
        json=payload
    )
    return response.json()

disease = "Tomato Early Blight"

prompt = f"""
Explain {disease}.
Give causes, symptoms, prevention and treatment.
"""

output = query({"inputs": prompt})

print(output)
