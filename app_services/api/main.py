from fastapi import FastAPI
import joblib
import os

from routes import router

MODEL_PATH = os.path.join("model", "model_latest.joblib")

app = FastAPI(title="Passos Mágicos - ML API")

print("Carregando modelo...")
model = joblib.load(MODEL_PATH)
print("Modelo carregado com sucesso.")

# injeta modelo nas rotas
app.state.model = model

app.include_router(router)