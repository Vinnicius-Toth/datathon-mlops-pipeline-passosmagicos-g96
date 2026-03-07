import pandas as pd
import boto3
from feature_engineering import preprocess

s3 = boto3.client("s3")

def lambda_handler(event, context):

    bucket_raw = "mlops-pipeline-passosmagicos-prod-raw"
    bucket_gold = "mlops-pipeline-passosmagicos-prod-gold"

    files = [
        "raw/alunos_2022.csv",
        "raw/alunos_2023.csv",
        "raw/alunos_2024.csv"
    ]

    dfs = []

    for file in files:
        obj = s3.get_object(Bucket=bucket_raw, Key=file)
        df = pd.read_csv(obj["Body"], sep=";")
        dfs.append(df)

    df_all = pd.concat(dfs)

    df_clean = preprocess(df_all)

    df_clean.to_csv("/tmp/features.csv", index=False)

    s3.upload_file(
        "/tmp/features.csv",
        bucket_gold,
        "gold/features_dataset.csv"
    )

    return {"status": "ok"}    