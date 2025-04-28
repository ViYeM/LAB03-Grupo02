import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pull_requests_filtrados.csv")

df["descricao_tamanho"] = df["body"].fillna("").apply(len)
df["status_bin"] = df["state"].apply(lambda x: 1 if x == "merged" else 0)
df["tamanho_pr"] = df["additions"] + df["deletions"]

sns.set(style="whitegrid")

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["tamanho_pr"], y=df["status_bin"])
plt.title("RQ01 - Tamanho do PR x Status")
plt.xlabel("Tamanho do PR (additions + deletions)")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.savefig("rq01_tamanho_pr_status.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["tempo_analise_horas"], y=df["status_bin"])
plt.title("RQ02 - Tempo de Análise x Status")
plt.xlabel("Tempo de Análise (h)")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.savefig("rq02_tempo_status.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["descricao_tamanho"], y=df["status_bin"])
plt.title("RQ03 - Tamanho da Descrição x Status")
plt.xlabel("Tamanho da Descrição (número de caracteres)")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.savefig("rq03_descricao_status.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["review_comments"], y=df["status_bin"])
plt.title("RQ04 - Número de Comentários x Status")
plt.xlabel("Número de Comentários de Revisão")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.savefig("rq04_comentarios_status.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["tamanho_pr"], y=df["review_comments"])
plt.title("RQ05 - Tamanho do PR x Nº de Revisões")
plt.xlabel("Tamanho do PR (additions + deletions)")
plt.ylabel("Número de Comentários de Revisão")
plt.tight_layout()
plt.savefig("rq05_tamanho_pr_revisoes.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["tempo_analise_horas"], y=df["review_comments"])
plt.title("RQ06 - Tempo de Análise x Nº de Revisões")
plt.xlabel("Tempo de Análise (h)")
plt.ylabel("Número de Comentários de Revisão")
plt.tight_layout()
plt.savefig("rq06_tempo_revisoes.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["descricao_tamanho"], y=df["review_comments"])
plt.title("RQ07 - Tamanho da Descrição x Nº de Revisões")
plt.xlabel("Tamanho da Descrição (número de caracteres)")
plt.ylabel("Número de Comentários de Revisão")
plt.tight_layout()
plt.savefig("rq07_descricao_revisoes.png")
plt.close()

plt.figure(figsize=(8,6))
sns.scatterplot(x=df["review_comments"], y=df["review_comments"])
plt.title("RQ08 - Comentários x Comentários (autocorrelação)")
plt.xlabel("Número de Comentários de Revisão")
plt.ylabel("Número de Comentários de Revisão")
plt.tight_layout()
plt.savefig("rq08_comentarios_revisoes.png")
plt.close()

