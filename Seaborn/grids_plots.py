import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/StudentsPerformance.csv')

sns.catplot(
    data=df, 
    x='gender', 
    y='math score', 
    kind='box', 
    col='lunch', 
    row='test preparation course'
)
plt.show()

g = sns.PairGrid(df, hue='gender')

g = g.map_upper(sns.scatterplot)

g = g.map_diag(sns.kdeplot)

g = g.map_lower(sns.kdeplot)

g = g.add_legend()

plt.show()