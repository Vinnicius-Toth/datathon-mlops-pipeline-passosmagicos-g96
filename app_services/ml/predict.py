import joblib
import pandas as pd


def load_model(path="model.joblib"):
    return joblib.load(path)


@router.post("/predict")
def predict(request: Request, payload: PredictionRequest):

    try:
        model = request.app.state.model

        df = pd.DataFrame([payload.dict()])

        print("Colunas recebidas:", df.columns)
        print("Features esperadas:", model.feature_names_in_)

        prediction = model.predict(df)[0]
        probability = model.predict_proba(df)[0][1]

        return {
            "risco_defasagem": int(prediction),
            "probabilidade": float(probability)
        }

    except Exception as e:
        print("ERRO INTERNO:", e)
        raise e