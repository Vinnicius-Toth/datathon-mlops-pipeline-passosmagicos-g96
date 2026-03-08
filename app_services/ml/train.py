import os
import joblib
import boto3
import numpy as np
from datetime import datetime

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    confusion_matrix
)

from config import (
    BUCKET_MODEL,
    TARGET,
    TEST_SIZE,
    RANDOM_STATE,
    LOCAL_MODEL_PATH,
    S3_MODEL_PREFIX
)

from data import load_data


THRESHOLD = 0.30 


def train():

    print("Carregando dados...")
    df = load_data()

    X = df.drop(TARGET, axis=1)
    y = df[TARGET]

    print("\nDistribuição da variável alvo:")
    print(y.value_counts(normalize=True))

    print("\nDividindo treino e teste...")
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("\nTreinando modelo com balanceamento...")
    model = RandomForestClassifier(
        n_estimators=400,
        max_depth=None,
        random_state=RANDOM_STATE,
        class_weight="balanced_subsample",
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    print("\nGerando probabilidades...")
    y_prob = model.predict_proba(X_test)[:, 1]

    print(f"\nAplicando threshold customizado: {THRESHOLD}")
    y_pred = (y_prob >= THRESHOLD).astype(int)

    print("\n===== MÉTRICAS =====")

    print("\nROC-AUC:")
    print(roc_auc_score(y_test, y_prob))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))

    print("\nImportância das Features:")
    importances = model.feature_importances_
    for feature, importance in sorted(
        zip(X.columns, importances),
        key=lambda x: x[1],
        reverse=True
    ):
        print(f"{feature}: {round(importance, 4)}")

    print("\nSalvando modelo local...")
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, LOCAL_MODEL_PATH)

    print("Enviando modelo para S3...")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    s3_key = f"{S3_MODEL_PREFIX}model_{timestamp}.joblib"
    latest_key = f"{S3_MODEL_PREFIX}model_latest.joblib"

    s3 = boto3.client("s3")

    s3.upload_file(LOCAL_MODEL_PATH, BUCKET_MODEL, s3_key)
    s3.upload_file(LOCAL_MODEL_PATH, BUCKET_MODEL, latest_key)

    print(f"\nModelo versionado: s3://{BUCKET_MODEL}/{s3_key}")
    print(f"Modelo atualizado como latest: s3://{BUCKET_MODEL}/{latest_key}")

    print("\nTreinamento concluído com sucesso!")


if __name__ == "__main__":
    train()