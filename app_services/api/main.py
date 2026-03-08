from fastapi import FastAPI
import joblib
from routes.predict import router as predict_router
from routes.health import router as health_router

app = FastAPI(
    title="Passos Mágicos - Modelo de Risco de Defasagem",
    description="""
API para predição do risco de defasagem escolar.

O modelo foi treinado com dados históricos de desempenho educacional
e retorna a probabilidade de um aluno apresentar defasagem acadêmica.

Arquitetura:
- Feature Engineering via Lambda
- Treinamento automatizado
- Modelo Random Forest
- Deploy via Docker
""",
    version="1.0.0",
    contact={
        "name": "Vinnicius Toth",
        "email": "vinni.toth@gmail.com"
    }
)

@app.on_event("startup")
def load_model():
    app.state.model = joblib.load("model/model_latest.joblib")

# incluir rotas
app.include_router(predict_router)
app.include_router(health_router)