import joblib
import pandas as pd


def load_model(path="model.joblib"):
    return joblib.load(path)


def predict(model, data: dict):

    df = pd.DataFrame([data])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "risco_defasagem": int(prediction),
        "probabilidade": float(probability)
    }