from fastapi import FastAPI
from langserve import add_routes
from disgonostics_graph import build_graph

app = FastAPI()
graph = build_graph()

add_routes(app,graph,path="/diagnose")
""" 
# langserve_backend/auth.py
from fastapi import Header, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME = "Authorization"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIxYjM5YWQxOS1hOTUwLTQ4N2EtOWUzYS1lNTJkYzliMWRkNTciLCJlbWFpbCI6InBhcGFtYWRvdWJhQGdtYWlsLmNvbSIsImlhdCI6MTczODg4MTM2MiwiZXhwIjoxNzcwNDE3MzYyfQ.hD6pLgkIo_LhsGbLLShQKSdInzk3BiRAOgpgPoLwOZ4"  # change this to a strong key or read from ENV

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != f"Bearer {API_KEY}":
        raise HTTPException(status_code=403, detail="Unauthorized access")
    return api_key


add_routes(app,graph,path="/diagnose",dependencies = [Depends(verify_api_key)]) """