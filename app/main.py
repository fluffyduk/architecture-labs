import os
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

def get_ip_from_ipapi():
    response = requests.get("http://ip-api.com/json/", timeout=5)
    data = response.json()
    return data.get("query")

def get_ip_from_jsonip():
    response = requests.get("https://jsonip.com/", timeout=5)
    data = response.json()
    return data.get("ip")

@app.get("/")
def index():
    ip_type = ""
    api_type = os.getenv("TYPE", "ipapi").lower()

    if api_type == "ipapi":
        ip_type = "ipapi"
        ip = get_ip_from_ipapi()
    elif api_type == "jsonip":
        ip_type = "jsonip"
        ip = get_ip_from_jsonip()
    else:
        return JSONResponse(
            status_code=400,
            content={"error": "Unknown TYPE. Use 'ipapi' or 'jsonip'"}
        )

    return {"ipType": ip_type, "myIP": ip}