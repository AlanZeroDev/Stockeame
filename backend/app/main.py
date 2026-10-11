
from fastapi import FastAPI

app = FastAPI(
    title="Stockeame API",
    description="Sistema de gestión y control de inventarios",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a Stockeame"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "application": "Stockeame"
    }
