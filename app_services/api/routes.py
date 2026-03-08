from fastapi import APIRouter, Request
from pydantic import BaseModel
import pandas as pd

router = APIRouter()


class PredictionRequest(BaseModel):
    ANO: int
    Idade_22: float
    INDE_22: float
    IAA: float
    IEG: float
    IPS: float
    IDA: float
    IPV: float
    IAN: float
    Matem: float
    Portug: float
    Ingles: float


@router.get("/")
def health():
    return {"status": "API funcionando"}


@router.post("/predict")
def predict(request: Request, payload: PredictionRequest):

    model = request.app.state.model

    df = pd.DataFrame([payload.dict()])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "risco_defasagem": int(prediction),
        "probabilidade": float(probability)
    }