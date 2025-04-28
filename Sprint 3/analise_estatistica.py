import pandas as pd
from scipy.stats import spearmanr

df = pd.read_csv("pull_requests_filtrados.csv")

df["descricao_tamanho"] = df["body"].fillna("").apply(len)
df["status_bin"] = df["state"].apply(lambda x: 1 if x == "merged" else 0)

df["tamanho_pr"] = df["additions"] + df["deletions"]

def analisar(x, y, nome_x, nome_y):
    if x.nunique() <= 1 or y.nunique() <= 1:
        print(f"Dados constantes entre {nome_x} x {nome_y}. Correlação não pode ser calculada.")
        return
    corr, p = spearmanr(x, y)
    print(f"{nome_x} x {nome_y} -> Correlação: {corr:.2f}, p-valor: {p:.4f}")

print("🔍 Correlações:")
analisar(df["tamanho_pr"], df["status_bin"], "Tamanho PR", "Status")
analisar(df["tempo_analise_horas"], df["status_bin"], "Tempo Análise", "Status")
analisar(df["descricao_tamanho"], df["status_bin"], "Descrição", "Status")
analisar(df["review_comments"], df["status_bin"], "Comentários", "Status")
