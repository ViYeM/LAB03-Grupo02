# Análise de Pull Requests em Repositórios Populares no GitHub

## 1. Introdução

Com a crescente adoção de repositórios públicos para o desenvolvimento colaborativo de software, o estudo de Pull Requests (PRs) torna-se essencial para compreender práticas de revisão e integração de código.

Este trabalho visa analisar características de PRs submetidos a projetos populares do GitHub, buscando identificar padrões que possam influenciar sua aceitação (merge) ou rejeição (close).

---

## 2. Objetivos

- Coletar dados reais de Pull Requests em repositórios populares do GitHub.
- Filtrar os PRs relevantes com base em critérios específicos de qualidade e tempo de análise.
- Aplicar métodos estatísticos para investigar relações entre tamanho, tempo de análise e status dos PRs.
- Visualizar graficamente as relações encontradas para embasar discussões.

---

## 3. Metodologia

A metodologia adotada para este trabalho envolveu as seguintes etapas:

### 3.1 Coleta de Dados

- Utilização da API pública do GitHub para coletar PRs de 10 repositórios populares listados em `repositorios.csv`.
- Coleta realizada utilizando autenticação via token pessoal, respeitando limites de requisições.

### 3.2 Filtro dos Dados

Após a coleta inicial:

- Foram mantidos apenas PRs com status `merged` ou `closed`.
- Selecionaram-se PRs que possuíssem pelo menos 1 comentário de revisão (`review_comments > 0`).
- Filtraram-se PRs cujo tempo de análise foi superior a 1 hora.

Esses critérios foram aplicados por meio do script `filtrar_dataset.py`, gerando o arquivo `pull_requests_filtrados.csv`.

### 3.3 Análise Estatística

- Aplicação do teste de correlação de Spearman para avaliar a relação entre variáveis.
- As correlações foram consideradas relevantes apenas quando apresentaram p-valor < 0.05.

### 3.4 Geração de Gráficos

- Foram produzidos gráficos de dispersão e histogramas para representar visualmente os dados.

---

## 4. Resultados Obtidos

Os resultados da análise estatística estão resumidos na tabela a seguir:

| Relação Avaliada                          | Correlação | p-valor | Interpretação                            |
|--------------------------------------------|------------|---------|------------------------------------------|
| Tamanho do PR (additions+deletions) x Status  | -0.06      | 0.5513  | Correlação fraca e não significativa     |
| Tempo de Análise x Status                    | -0.01      | 0.9373  | Sem correlação                           |
| Tamanho da Descrição x Status                | Nulo       | Nulo    | Dados constantes, sem variação           |
| Comentários de Review x Status               | -0.10      | 0.3164  | Fraca correlação, não significativa      |
| Tamanho do PR x Nº de Revisões               | -0.08      | 0.4441  | Sem correlação relevante                 |
| Tempo de Análise x Nº de Revisões            | 0.02       | 0.8129  | Sem correlação relevante                 |
| Interações (review comments) x Nº de Revisões| 1.00       | 0.0000  | Correlação perfeita (métrica relacionada)|

---

## 5. Análise dos Resultados

De acordo com os dados analisados:

- O tamanho do PR e o tempo de análise não demonstraram influência relevante sobre o status de aceitação.
- O número de comentários de revisão também não mostrou correlação forte com o merge dos PRs.
- A única relação perfeita encontrada foi entre o número de comentários de revisão e o número de interações, pois ambos medem a mesma métrica.

Esses achados indicam que, em projetos de grande porte no GitHub, a aceitação de PRs pode depender mais de fatores qualitativos (como qualidade do código ou pertinência da proposta) do que de métricas quantitativas básicas.

---

## 6. Considerações Finais

O presente trabalho permitiu a prática de técnicas de extração, tratamento e análise de dados de projetos de software open source.

As limitações encontradas incluem:

- Dados incompletos em alguns PRs.
- Dificuldade em inferir qualitativamente os critérios de aceitação de PRs apenas por dados numéricos.

Sugere-se, para trabalhos futuros, a aplicação de métodos de análise qualitativa (como análise de conteúdo de revisões) para complementar a avaliação.

---

## Anexos

### Scripts Utilizados

- `coletar_prs.py`: coleta de dados
- `filtrar_dataset.py`: aplicação de filtros
- `analise_estatistica.py`: cálculo das correlações
- `graficos.py`: geração de visualizações

### Gráficos

- Scatterplot: Tamanho do PR x Status
- Scatterplot: Tempo de Análise x Status
- Scatterplot: Nº de Comentários x Status
- Histograma: Distribuição de Comentários de Review

---
