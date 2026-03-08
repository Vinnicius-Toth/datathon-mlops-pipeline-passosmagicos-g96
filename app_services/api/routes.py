from fastapi import APIRouter, Request
from pydantic import BaseModel
import pandas as pd

router = APIRouter()


class PredictionRequest(BaseModel):
    ano: int
    idade_22: float
    inde_22: float
    iaa: float
    ieg: float
    ips: float
    ida: float
    ipv: float
    ian: float
    matem: float
    portug: float
    ingles: float


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