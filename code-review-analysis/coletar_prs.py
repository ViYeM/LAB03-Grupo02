import requests
import pandas as pd
from datetime import datetime
import time

GITHUB_TOKEN = "TokenGithub"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def listar_repos_populares(qtd=10):
    url = f"https://api.github.com/search/repositories?q=stars:>10000&sort=stars&order=desc&per_page={qtd}"
    resposta = requests.get(url, headers=HEADERS)
    dados = resposta.json()
    return [repo["full_name"] for repo in dados["items"]]

def converter_data(data_str):
    return datetime.strptime(data_str, "%Y-%m-%dT%H:%M:%SZ")

def coletar_dados_prs(repo_full_name, max_prs=30):
    prs = []
    page = 1

    print(f"Coletando PRs de: {repo_full_name}")
    while len(prs) < max_prs:
        url = f"https://api.github.com/repos/{repo_full_name}/pulls?state=all&per_page=30&page={page}"
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print("Erro ao coletar PRs")
            break
        dados = r.json()
        if not dados:
            break

        for pr in dados:
            if pr["state"] not in ["closed"] or pr["merged_at"] is None:
                continue

            created = converter_data(pr["created_at"])
            closed = converter_data(pr["closed_at"]) if pr["closed_at"] else None
            if not closed or (closed - created).total_seconds() < 3600:
                continue  

            review_url = pr["_links"]["review_comments"]["href"]
            comentarios = requests.get(review_url, headers=HEADERS).json()
            if isinstance(comentarios, list) and len(comentarios) < 1:
                continue

            pr_detalhado = requests.get(pr["url"], headers=HEADERS).json()
            comentarios_gerais = pr_detalhado["comments"]
            participantes = len(set([pr["user"]["login"]]))

            metricas = {
                "repo": repo_full_name,
                "numero": pr["number"],
                "status": "merged" if pr["merged_at"] else "closed",
                "arquivos_alterados": pr_detalhado["changed_files"],
                "linhas_adicionadas": pr_detalhado["additions"],
                "linhas_removidas": pr_detalhado["deletions"],
                "tempo_analise_horas": round((closed - created).total_seconds() / 3600, 2),
                "descricao_tamanho": len(pr["body"]) if pr["body"] else 0,
                "comentarios": comentarios_gerais,
                "participantes": participantes,
                "reviews": len(comentarios),
            }

            prs.append(metricas)

            if len(prs) >= max_prs:
                break

        page += 1
        time.sleep(1)

    return prs

todos_prs = []

repos = listar_repos_populares(qtd=5)
for repo in repos:
    prs_repo = coletar_dados_prs(repo)
    todos_prs.extend(prs_repo)

df = pd.DataFrame(todos_prs)
df.to_csv("dataset_prs.csv", index=False)
print("✅ Dataset salvo como dataset_prs.csv")
