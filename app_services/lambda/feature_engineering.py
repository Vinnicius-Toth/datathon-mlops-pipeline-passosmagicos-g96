import pandas as pd
import unicodedata


def normalize_column_name(col: str) -> str:
    col = col.strip()
    col = col.replace(" ", "_")
    col = unicodedata.normalize("NFKD", col)
    col = col.encode("ascii", "ignore").decode("utf-8")
    col = col.lower()
    return col


def preprocess(df):

    # Padronizar nomes das colunas
    df.columns = [normalize_column_name(c) for c in df.columns]

    # Corrigir separador decimal
    df = df.replace(",", ".", regex=True)

    numeric_cols = [
        "inde_22",
        "iaa",
        "ieg",
        "ips",
        "ida",
        "ipv",
        "ian",
        "matem",
        "portug",
        "ingles",
        "defas"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Criar target
    df["risco_defasagem"] = (df["defas"] > 0).astype(int)

    # Definir features finais
    features = [
        "ano",
        "idade_22",
        "inde_22",
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

    df = df[features]

    df = df.fillna(df.median(numeric_only=True))

    return df