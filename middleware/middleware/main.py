from fastapi import FastAPI, HTTPException
import requests
import os

app = FastAPI()
APP_URL = os.getenv("APP_URL", "http://app-service:8000")

@app.get("/health")
def health():
    return {"status": "ok", "role": "middleware"}

@app.get("/items-proxied")
def items_proxied():
    try:
        r = requests.get(f"{APP_URL}/items", timeout=5)
        r.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return r.json()
