import requests

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxYjM5YWQxOS1hOTUwLTQ4N2EtOWUzYS1lNTJkYzliMWRkNTciLCJlbWFpbCI6InBhcGFtYWRvdWJhQGdtYWlsLmNvbSIsImlhdCI6MTczODg4MTM2MiwiZXhwIjoxNzcwNDE3MzYyfQ.hD6pLgkIo_LhsGbLLShQKSdInzk3BiRAOgpgPoLwOZ4"
BASE_URL = "https://api.euron.one/api/v1/euri/alpha"

def euri_chat_completion(messages, model="gpt-4.1-nano", temperature=0.7, max_tokens=1000):
    url = f"{BASE_URL}/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]