import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/StudentsPerformance.csv')

print(df.head(),'\n')
print(df.columns,'\n')

# Diagrama de Caixa 
plt.figure(figsize=(6.4,2.8), dpi=150)
sns.boxplot(
    data=df, 
    y='reading score', 
    x='parental level of education', 
    hue='test preparation course',
    palette='tab10',
    flierprops={
        'marker': 'd',
        'markersize': 4,
        'markerfacecolor': '#555555',
        'markeredgecolor': '#555555'
    }
)

plt.subplots_adjust(left=0.07)

plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

plt.xlabel(plt.gca().get_xlabel(), fontsize=8)
plt.ylabel(plt.gca().get_ylabel(), fontsize=8)

plt.legend(bbox_to_anchor=(1.001,1), fontsize=6)

plt.show()


# Gráfico de Violino 
plt.figure(figsize=(8.4,5.8), dpi=150)
sns.violinplot(
    data=df, 
    y='parental level of education', 
    x='reading score',
    palette='Set2', 
    hue='test preparation course',
    split=True,
    inner=None,
    bw_adjust=0.5
)

plt.subplots_adjust(left=0.150)

plt.xticks(fontsize=6)
plt.yticks(fontsize=6)

plt.xlabel(plt.gca().get_xlabel(), fontsize=8)
plt.ylabel(plt.gca().get_ylabel(), fontsize=8)

plt.legend(bbox_to_anchor=(1.001,1), fontsize=6)

plt.show()


#Gráfico de Enxame
plt.figure(figsize=(6.4,2.8), dpi=150)
sns.swarmplot(
    data=df, 
    x='math score',
    y='gender', 
    size=2, 
    palette='Set2',
    hue='test preparation course',
    dodge=True
)

plt.xticks(fontsize=7)
plt.yticks(fontsize=7)

plt.xlabel(plt.gca().get_xlabel(), fontsize=9)
plt.ylabel(plt.gca().get_ylabel(), fontsize=9)

plt.legend(bbox_to_anchor=(1.13,1), fontsize=6)

plt.show()


# Gráfico de caixas em camadas
sns.boxenplot(
    data=df, 
    x='math score',
    y='test preparation course', 
    hue='gender'
)
plt.show()