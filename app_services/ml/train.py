import os
import joblib
import boto3
from datetime import datetime

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from config import (
    BUCKET_MODEL,
    TARGET,
    TEST_SIZE,
    RANDOM_STATE,
    LOCAL_MODEL_PATH,
    S3_MODEL_PREFIX
)

from data import load_data
from evaluate import evaluate_model


def train():

    print("Carregando dados...")
    df = load_data()

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    print("Dividindo treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("Treinando modelo...")
    model = RandomForestClassifier(
        n_estimators=300,
        random_state=RANDOM_STATE,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)

    print("Avaliando modelo...")
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    evaluate_model(y_test, y_pred, y_prob)

    print("Salvando modelo local...")
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, LOCAL_MODEL_PATH)

    print("Enviando modelo para S3...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    s3_key = f"{S3_MODEL_PREFIX}model_{timestamp}.joblib"
    latest_key = f"{S3_MODEL_PREFIX}model_latest.joblib"

    s3 = boto3.client("s3")

    s3.upload_file(LOCAL_MODEL_PATH, BUCKET_MODEL, s3_key)
    s3.upload_file(LOCAL_MODEL_PATH, BUCKET_MODEL, latest_key)

    print(f"Modelo versionado: s3://{BUCKET_MODEL}/{s3_key}")
    print(f"Modelo atualizado como latest: s3://{BUCKET_MODEL}/{latest_key}")


if __name__ == "__main__":
    train()