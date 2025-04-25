import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pull_requests_filtrados.csv")
df["descricao_tamanho"] = df["body"].fillna("").apply(len)
df["status_bin"] = df["state"].apply(lambda x: 1 if x == "merged" else 0)

sns.set(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="additions", y="status_bin")
plt.title("Tamanho do PR x Status")
plt.xlabel("Additions")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x="tempo_analise_horas", y="status_bin")
plt.title("Tempo de Análise x Status")
plt.xlabel("Tempo (h)")
plt.ylabel("Status (1 = merged)")
plt.tight_layout()
plt.show()
