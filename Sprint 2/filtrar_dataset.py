import pandas as pd

df = pd.read_csv("pull_requests.csv")

df["created_at"] = pd.to_datetime(df["created_at"], errors="coerce")
df["merged_at"] = pd.to_datetime(df["merged_at"], errors="coerce")
df["closed_at"] = pd.to_datetime(df["closed_at"], errors="coerce")

df["fim"] = df["merged_at"].fillna(df["closed_at"])

df["tempo_analise_horas"] = (df["fim"] - df["created_at"]).dt.total_seconds() / 3600

df_filtrado = df[
    (df["state"].isin(["merged", "closed"])) &
    (df["tempo_analise_horas"] > 1)  
]

df_filtrado = df_filtrado.drop(columns=["fim"])

df_filtrado.to_csv("pull_requests_filtrados.csv", index=False)
print(f"Filtrado: {len(df_filtrado)} PRs salvos!")
