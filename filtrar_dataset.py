import pandas as pd
from datetime import datetime

df = pd.read_csv("pull_requests.csv")

def calcular_tempo(pr):
    if pd.notnull(pr["merged_at"]):
        fim = pd.to_datetime(pr["merged_at"])
    else:
        fim = pd.to_datetime(pr["closed_at"])
    inicio = pd.to_datetime(pr["created_at"])
    return (fim - inicio).total_seconds() / 3600

df["tempo_analise_horas"] = df.apply(calcular_tempo, axis=1)
df_filtrado = df[
    ((df["state"] == "closed") | (df["state"] == "merged")) &
    (df["review_comments"] > 0) &
    (df["tempo_analise_horas"] > 1)
]

df_filtrado.to_csv("dataset_filtrado.csv", index=False)
