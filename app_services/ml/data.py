import awswrangler as wr
from config import BUCKET_GOLD


def load_data():
    df = wr.s3.read_parquet(
        path=f"s3://{BUCKET_GOLD}/gold/features_dataset/"
    )
    return df

