# Aprendendo Machine Learning & Data Science

> Repositório de estudos documentando minha evolução em Python, Análise de Dados e Machine Learning.

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-3.0.1-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-2.4.2-013243?style=flat-square&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.10.8-11557C?style=flat-square&logo=matplotlib&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13.2-4C72B0?style=flat-square&logo=python&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-1.17.1-8CAAE6?style=flat-square&logo=scipy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.8.0-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=flat-square&logo=flask&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2.32.5-2E8B57?style=flat-square&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.14.3-4B8BBE?style=flat-square&logo=python&logoColor=white)
![Joblib](https://img.shields.io/badge/Joblib-1.5.3-FF6F00?style=flat-square&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=flat-square&logo=github&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

## Sobre mim

Este repositório reúne os estudos e experimentos que venho desenvolvendo enquanto construo minha base em **Python, Data Science e Machine Learning**, com foco em me tornar analista de dados.

## Sobre o repositório

Aqui estão os códigos, notebooks e exercícios produzidos principalmente durante o curso **"Python for Machine Learning & Data Science Masterclass"** (Jose Portilla / Pierian Data), organizados em pastas numeradas que seguem a progressão do aprendizado — desde a manipulação de arrays com NumPy até deploy de modelos com Flask.

Não é um projeto comercial único, mas um **registro contínuo de prática**: scripts de estudo, notebooks de exercícios, um projeto de capstone e a implementação de modelos de Machine Learning do início ao fim, incluindo salvamento e disponibilização via API.

## Conteúdos estudados

| Área | Tópicos |
|---|---|
| **Fundamentos Python** | Arrays e indexação com NumPy |
| **Manipulação de dados** | Pandas (Series, DataFrames, groupby, merge/concat, dados ausentes, leitura de CSV/Excel/HTML/SQL) |
| **Visualização** | Matplotlib (figuras, subplots, estilos, legendas) e Seaborn (gráficos categóricos, de distribuição e de matriz) |
| **Pré-processamento** | Padronização (`StandardScaler`, `MinMaxScaler`), features polinomiais, vetorização de texto (`CountVectorizer`, `TfidfVectorizer`) |
| **ML Supervisionado** | Regressão Linear/Polinomial, Regularização (Ridge, Lasso, Elastic Net), Regressão Logística, KNN, SVM, Árvores de Decisão, Random Forest, Boosting, Naive Bayes |
| **ML Não Supervisionado** | K-Means, Clustering Hierárquico, DBSCAN, PCA |
| **Avaliação de modelos** | Métricas de classificação e regressão, validação cruzada, `GridSearchCV` |
| **Deploy** | Persistência de modelos com `joblib` e API REST com Flask |

## Tecnologias e ferramentas

- **Linguagem:** Python
- **Ambiente:** Jupyter Notebook / scripts `.py`
- **Manipulação e análise de dados:** NumPy, Pandas
- **Visualização:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Banco de dados:** SQLAlchemy (conexão com MySQL e SQLite)
- **Persistência de modelos:** joblib
- **API / Deploy:** Flask
- **Versionamento:** Git / GitHub

## Machine Learning

Algoritmos e técnicas implementados ao longo do repositório:

**Supervisionado**
- Regressão Linear e Polinomial
- Ridge, Lasso e Elastic Net (com validação cruzada)
- Regressão Logística (binária e multiclasse)
- K-Nearest Neighbors (classificação e regressão)
- Support Vector Machines (SVC, SVR, LinearSVC, LinearSVR)
- Árvores de Decisão
- Random Forest (classificação e regressão)
- AdaBoost e Gradient Boosting
- Naive Bayes (`MultinomialNB`) aplicado a NLP

**Não supervisionado**
- K-Means (incluindo quantização de cores em imagens)
- Clustering Hierárquico (Agglomerative Clustering)
- DBSCAN
- PCA (implementação manual e via Scikit-learn)

## Projetos e estudos em destaque

- **`12_Supervised_Learning_Capstone_Project`** — Projeto de capstone: previsão de *churn* de clientes usando métodos baseados em árvores (Decision Tree, Random Forest, Boosting), reunindo boa parte do que foi estudado nos módulos anteriores.
- **`13_Naive_Bayes_and_NLP`** — Classificação de texto (análise de sentimento em tweets e reviews de filmes) com extração de features (`CountVectorizer`/`TF-IDF`) e Naive Bayes.
- **`18_Model_Deployment`** — Ciclo completo de um modelo: treino, persistência com `joblib` e exposição via uma API Flask (`api.py`) com endpoint `/predict`.
- **`14_K_Means_Clustering`** — Além do clustering tradicional, inclui um exemplo de quantização de cores em imagens com K-Means.
- **`17_PCA_Principal_Component_Analysis`** — Traz tanto uma implementação manual do PCA quanto o uso da versão pronta do Scikit-learn, o que ajuda a entender o algoritmo por trás da ferramenta.

## Estrutura do repositório

```text
Aprendendo_Machine_Learning_Data_Science/
├── 01_NumPy/                              # Arrays, indexação e operações
├── 02_Pandas/                             # Series, DataFrames, SQL, arquivos
├── 03_Matplotlib/                         # Visualização de dados
├── 04_Seaborn/                            # Visualização estatística
├── 05_Linear_Regression/                  # Regressão linear/polinomial e regularização
├── 06_Logistic_Regression/                # Regressão logística
├── 07_K_Nearest_Neighbor/                 # KNN
├── 08_Support_Vector_Machines/            # SVM (classificação e regressão)
├── 09_Decision_Trees/                     # Árvores de decisão
├── 10_Random_Forests/                     # Random Forest
├── 11_Boosting/                           # AdaBoost e Gradient Boosting
├── 12_Supervised_Learning_Capstone_Project/  # Projeto de previsão de churn
├── 13_Naive_Bayes_and_NLP/                # Classificação de texto
├── 14_K_Means_Clustering/                 # K-Means
├── 15_Hierarchical_Clustering/            # Clustering hierárquico
├── 16_DBSCAN/                             # DBSCAN
├── 17_PCA_Principal_Component_Analysis/   # Redução de dimensionalidade
├── 18_Model_Deployment/                   # Persistência de modelo + API Flask
├── requirements.txt
├── LICENSE
└── README.md
```

Cada pasta segue, em geral, o mesmo padrão: scripts/notebooks numerados na ordem em que os conceitos foram estudados, uma subpasta `data`/`Arquivos` com os datasets usados e, quando aplicável, exercícios de fixação ao final.

## Metodologias e conceitos aplicados

- Análise exploratória de dados (EDA)
- Limpeza e tratamento de dados ausentes
- Visualização de dados (univariada, categórica e de correlação)
- Padronização/normalização de features
- Engenharia de features (polinomiais, vetorização de texto)
- Divisão treino/teste (`train_test_split`)
- Validação cruzada e ajuste de hiperparâmetros (`cross_val_score`, `GridSearchCV`, `RidgeCV`/`LassoCV`/`ElasticNetCV`)
- Avaliação de modelos (métricas de classificação e regressão, matriz de confusão, curva ROC)
- Redução de dimensionalidade (PCA)
- Clustering e sua avaliação
- Persistência e deploy de modelos

## Objetivo de aprendizado

Este repositório não busca apresentar um produto final ou um portfólio de projetos comerciais isolados, e sim **documentar uma jornada prática de aprendizado**. A ideia é mostrar experimentação com diferentes técnicas, aplicação dos conceitos em datasets reais e a evolução técnica ao longo do curso — dos fundamentos de manipulação de dados até a construção e o deploy de modelos de Machine Learning.

## Próximos passos

Alguns direcionamentos futuros para o repositório (ainda não implementados):

- Explorar tópicos de Deep Learning e redes neurais
- Aprofundar projetos de NLP com abordagens mais modernas
- Criar projetos autorais de ponta a ponta, aplicando os conceitos estudados a problemas próprios
- Expandir o deploy de modelos para além do Flask (ex.: containerização, outras formas de hospedagem)

## Curso de referência

Grande parte do conteúdo deste repositório foi desenvolvida durante o curso:

**Python for Machine Learning & Data Science Masterclass** — Jose Portilla / Pierian Data
🔗 [udemy.com/course/python-for-machine-learning-data-science-masterclass](https://www.udemy.com/course/python-for-machine-learning-data-science-masterclass/)

## Autor

**Alessandro Moreira Cecilio**

GitHub: [github.com/AleCecilio/Aprendendo_Machine_Learning_Data_Science](https://github.com/AleCecilio/Aprendendo_Machine_Learning_Data_Science)
