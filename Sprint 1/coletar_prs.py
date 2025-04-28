import requests
import pandas as pd
import time

GITHUB_TOKEN = "GITHUB_TOKEN"
HEADERS = {"Authorization": f"Bearer {GITHUB_TOKEN}"}

def buscar_prs(repo):
    prs = []
    page = 1
    while True:
        url = f"https://api.github.com/repos/{repo}/pulls?state=closed&per_page=100&page={page}"
        r = requests.get(url, headers=HEADERS)
        if r.status_code != 200:
            print(f" Erro {r.status_code} ao buscar {repo}")
            break
        data = r.json()
        if not data:
            break
        for pr in data:
            prs.append({
                "repo": repo,
                "number": pr.get("number"),
                "title": pr.get("title"),
                "user": pr["user"]["login"] if pr.get("user") else None,
                "created_at": pr.get("created_at"),
                "closed_at": pr.get("closed_at"),
                "merged_at": pr.get("merged_at"),
                "state": pr.get("state"),
                "review_comments": pr.get("review_comments", 0),
                "body": pr.get("body") or "",
                "additions": pr.get("additions", 0),
                "deletions": pr.get("deletions", 0),
                "changed_files": pr.get("changed_files", 0)
            })
        page += 1
        time.sleep(1)
    return prs

def main():
    repos = pd.read_csv("repositorios.csv")["full_name"].tolist()[:5]  
    todos_prs = []
    for repo in repos:
        prs = buscar_prs(repo)
        todos_prs.extend(prs)
        time.sleep(2)

    df = pd.DataFrame(todos_prs)
    df.to_csv("pull_requests.csv", index=False)
    print(f" {len(todos_prs)} PRs coletados e salvos!")

if __name__ == "__main__":
    main()
