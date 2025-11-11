import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/country_table.csv')

df = df.set_index('Countries')

sns.heatmap(
    df.drop('Life expectancy', axis=1),
    linewidths=0.5,
    annot=True,
    cmap='viridis'
)
plt.show()

sns.clustermap(
    df.drop('Life expectancy', axis=1),
    linewidths=0.5,
    annot=True,
    cmap='viridis',
    col_cluster=False
)
plt.show()