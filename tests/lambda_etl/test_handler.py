from unittest.mock import patch
import pandas as pd
from app_services.lambda_etl.handler import lambda_handler


@patch("app_services.lambda_etl.handler.wr")
def test_lambda_handler(mock_wr):

    mock_df = pd.DataFrame({
        "Idade 22": [17],
        "INDE 22": [7.0],
        "IAA": [8],
        "IEG": [7],
        "IPS": [7],
        "IDA": [6],
        "IPV": [7],
        "IAN": [8],
        "Matem": [6],
        "Portug": [7],
        "Inglês": [6],
        "Defas": [0]
    })

    mock_wr.s3.read_csv.return_value = mock_df
    mock_wr.s3.to_parquet.return_value = None

    response = lambda_handler({}, {})

    assert response["status"] == "ok"