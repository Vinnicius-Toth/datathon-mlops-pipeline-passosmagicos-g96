# import pandas as pd
# from app_services.lambda_etl.feature_engineering import preprocess


# def test_target_creation():

#     data = {
#         "Idade 22": [17, 16],
#         "INDE 22": [7.0, 5.0],
#         "IAA": [8, 6],
#         "IEG": [7, 4],
#         "IPS": [7, 3],
#         "IDA": [6, 4],
#         "IPV": [7, 2],
#         "IAN": [8, 3],
#         "Matem": [6, 2],
#         "Portug": [7, 3],
#         "Inglês": [6, 2],
#         "Defas": [0, -2]
#     }

#     df = pd.DataFrame(data)

#     result = preprocess(df)

#     assert result["risco_defasagem"].iloc[0] == 0
#     assert result["risco_defasagem"].iloc[1] == 1