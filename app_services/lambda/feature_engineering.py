import pandas as pd
import unicodedata
import re


def normalize_column_name(col: str) -> str:
    col = col.strip()
    col = col.replace(" ", "_")
    col = unicodedata.normalize("NFKD", col)
    col = col.encode("ascii", "ignore").decode("utf-8")
    col = col.lower()

    # Remover sufixo _22, _23, _24 etc
    col = re.sub(r"_\d{2}$", "", col)

    return col


def preprocess(df):

    df.columns = [normalize_column_name(c) for c in df.columns]

    df = df.replace(",", ".", regex=True)

    numeric_cols = [
        "inde",
        "iaa",
        "ieg",
        "ips",
        "ida",
        "ipv",
        "ian",
        "matem",
        "portug",
        "ingles",
        "defas",
        "idade"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["risco_defasagem"] = (df["defas"] < 0).astype(int)

    print("\nDistribuição da variável alvo:")
    print(df["risco_defasagem"].value_counts())

    features = [
        "idade",
        "inde",
        "iaa",
        "ieg",
        "ips",
        "ida",
        "ipv",
        "ian",
        "matem",
        "portug",
        "ingles",
        "risco_defasagem"
    ]

    missing_cols = [col for col in features if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Colunas ausentes: {missing_cols}")

    df = df[features]

    df = df.fillna(df.median(numeric_only=True))

    return df