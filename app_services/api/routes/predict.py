
import pandas as pd
from fastapi import APIRouter, Request, Body
from pydantic import BaseModel, Field

router = APIRouter()


class PredictionRequest(BaseModel):
    idade: float = Field(
        ...,
        description="Idade do aluno no ano de referência.",
        example=17,
        ge=5,
        le=25
    )

    inde: float = Field(
        ...,
        description="Índice de Desenvolvimento Educacional (métrica agregada).",
        example=7.1,
        ge=0,
        le=10
    )

    iaa: float = Field(
        ...,
        description="Indicador de Auto Avaliação do aluno.",
        example=8.0,
        ge=0,
        le=10
    )

    ieg: float = Field(
        ...,
        description="Indicador de Engajamento.",
        example=6.5,
        ge=0,
        le=10
    )

    ips: float = Field(
        ...,
        description="Indicador Psicossocial.",
        example=7.0,
        ge=0,
        le=10
    )

    ida: float = Field(
        ...,
        description="Indicador de Aprendizagem.",
        example=6.0,
        ge=0,
        le=10
    )

    ipv: float = Field(
        ...,
        description="Indicador de Ponto de Virada.",
        example=7.5,
        ge=0,
        le=10
    )

    ian: float = Field(
        ...,
        description="Indicador de Adequação ao Nível.",
        example=8.0,
        ge=0,
        le=10
    )

    matem: float = Field(
        ...,
        description="Nota média de Matemática.",
        example=6.5,
        ge=0,
        le=10
    )

    portug: float = Field(
        ...,
        description="Nota média de Português.",
        example=7.2,
        ge=0,
        le=10
    )

    ingles: float = Field(
        ...,
        description="Nota média de Inglês.",
        example=6.8,
        ge=0,
        le=10
    )
    
class PredictionResponse(BaseModel):
    risco_defasagem: int
    probabilidade: float
    modelo_versao: str


@router.post(
    "/predict",
    summary="Prediz risco de defasagem escolar",
    tags=["Predição"]
)
def predict(
    request: Request,
    payload: PredictionRequest = Body(
        ...,
        openapi_examples={
            "baixo_risco": {
                "summary": "🟢 Baixo risco de defasagem",
                "description": "Aluno com bom desempenho acadêmico e bons indicadores.",
                "value": {
                    "idade": 17,
                    "inde": 8.5,
                    "iaa": 9.0,
                    "ieg": 8.5,
                    "ips": 8.0,
                    "ida": 8.7,
                    "ipv": 9.0,
                    "ian": 8.8,
                    "matem": 8.5,
                    "portug": 8.0,
                    "ingles": 8.2
                },
            },
            "alto_risco": {
                "summary": "🔴 Alto risco de defasagem",
                "description": "Aluno com baixo desempenho acadêmico e indicadores críticos.",
                "value": {
                    "idade": 17,
                    "inde": 4.2,
                    "iaa": 4.0,
                    "ieg": 3.5,
                    "ips": 5.0,
                    "ida": 4.1,
                    "ipv": 3.8,
                    "ian": 4.5,
                    "matem": 3.2,
                    "portug": 4.0,
                    "ingles": 3.8
                },
            },
        },
    ),
):

    model = request.app.state.model

    df = pd.DataFrame([payload.dict()])
    df = df[model.feature_names_in_]

    THRESHOLD = 0.30

    probability = model.predict_proba(df)[0][1]
    prediction = int(probability >= THRESHOLD)

    return PredictionResponse(
        risco_defasagem=int(prediction),
        probabilidade=float(probability),
        modelo_versao="1.0.0"
    )