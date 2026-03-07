import awswrangler as wr
from feature_engineering import preprocess


def lambda_handler(event, context):

    bucket_raw = "mlops-pipeline-passosmagicos-prod-raw"
    bucket_gold = "mlops-pipeline-passosmagicos-prod-gold"

    df_all = wr.s3.read_csv(
        path=f"s3://{bucket_raw}/raw/",
        sep=","
    )

    df_clean = preprocess(df_all)

    wr.s3.to_parquet(
        df=df_clean,
        path=f"s3://{bucket_gold}/gold/features_dataset/",
        dataset=True,
        partition_cols=["ANO"],
        mode="overwrite"
    )

    return {"status": "ok"}