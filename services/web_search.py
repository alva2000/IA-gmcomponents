import requests
import os
from dotenv import load_dotenv

load_dotenv()

SERP_API_KEY = os.getenv("SERP_API_KEY")

def buscar_en_google(query):
    url = "https://serpapi.com/search"

    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }

    res = requests.get(url, params=params).json()

    resultados = []
    for r in res.get("organic_results", [])[:3]:
        resultados.append(r.get("snippet", ""))

    return "\n".join(resultados)