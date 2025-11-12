import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Seaborn/Arquivos/application_record.csv')

# GRÁFICO 1 — Dispersão entre Idade (DAYS_BIRTH) e Tempo de Emprego (DAYS_EMPLOYED)
empregados = df[df['DAYS_EMPLOYED'] < 0].copy()
empregados['DAYS_EMPLOYED'] *= -1
empregados['DAYS_BIRTH'] *= -1

plt.figure(dpi=150)
sns.scatterplot(
    x='DAYS_BIRTH',
    y='DAYS_EMPLOYED',
    data=empregados,
    alpha=0.01,
    linewidth=0
)

plt.savefig('Seaborn/Arquivos/ex_sns_01.jpg')
plt.show()



# GRÁFICO 2 — Histograma da Idade dos Clientes
df['YEARS'] = (df['DAYS_BIRTH']  / -365)

plt.figure(dpi=150)
sns.histplot(
    data=df,
    x='YEARS',
    linewidth=2,
    edgecolor = 'black',
    color='red',
    bins=45,
    alpha=0.4
)
plt.xlabel('Age in Years')
plt.savefig('Seaborn/Arquivos/ex_sns_02.jpg')
plt.show()



# GRÁFICO 3 — Boxplot da Renda (Metade Inferior dos Clientes)
bottom_half = df[df['AMT_INCOME_TOTAL'] <= df['AMT_INCOME_TOTAL'].median()]

plt.figure(figsize=(5.4, 2.8),dpi=120)
sns.boxplot(
    data=bottom_half,
    x='NAME_FAMILY_STATUS',
    y='AMT_INCOME_TOTAL',
    hue='FLAG_OWN_REALTY',
    order=['Married', 'Civil marriage', 'Widow', 'Single / not married', 'Separated'],
    flierprops={
        'marker': 'd',
        'markersize': 4,
        'markerfacecolor': '#555555',
        'markeredgecolor': '#555555'
    }
)
plt.subplots_adjust(left=0.09)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.xlabel(plt.gca().get_xlabel(), fontsize=10)
plt.ylabel(plt.gca().get_ylabel(), fontsize=10)

plt.legend(
    bbox_to_anchor=(1.01,1), 
    title='FLAG_OWN_REALTY',
    borderaxespad=0., 
    fontsize=6,
    title_fontsize=6
)

plt.title(
    'Income Totals per Family Status for Bottom Half of Earners', 
    fontsize=10
)

plt.savefig('Seaborn/Arquivos/ex_sns_03.jpg')
plt.show()



# GRÁFICO 4 — Heatmap de Correlação entre Variáveis Numéricas
plt.figure(figsize=(7.4, 3.8),dpi=120)

sns.heatmap(
    df.drop('FLAG_MOBIL',axis=1).select_dtypes(include='number').corr(), 
    cmap="viridis",
)
plt.subplots_adjust(left=0.2)

plt.xticks(fontsize=5, rotation=20)
plt.yticks(fontsize=5)

plt.savefig('Seaborn/Arquivos/ex_sns_04.jpg')
plt.show()