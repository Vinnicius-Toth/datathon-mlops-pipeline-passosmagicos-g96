import pandas as pd

def preprocess(df):

    # corrigir decimais
    df = df.replace(",", ".", regex=True)

    numeric_cols = [
        "INDE 22",
        "IAA",
        "IEG",
        "IPS",
        "IDA",
        "IPV",
        "IAN",
        "Matem",
        "Portug",
        "Inglês"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # criar target
    df["RISCO_DEFASAGEM"] = (df["Defas"] > 0).astype(int)

    # features finais
    features = [
        "Idade 22",
        "INDE 22",
        "IAA",
        "IEG",
        "IPS",
        "IDA",
        "IPV",
        "IAN",
        "Matem",
        "Portug",
        "Inglês",
        "RISCO_DEFASAGEM"
    ]

    df = df[features]

    df = df.fillna(df.median())

    return df