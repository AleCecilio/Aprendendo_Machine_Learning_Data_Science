import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/dm_office_sales.csv')

plt.figure(dpi=150)
sns.rugplot(x='salary', data=df, height=0.5)
plt.show()


# sns.set_theme(style='darkgrid')
sns.displot(
    data=df, 
    x='salary', 
    bins=10, 
    color='red', 
    edgecolor='blue', 
    linewidth=4, 
    ls='--'
)
plt.show()


sns.histplot(data=df, x='salary')
plt.show()


sns.displot(
    data=df, 
    x='salary', 
    kde=True,
    rug=True
)
plt.show()


sns.kdeplot(data=df, x='salary')
plt.show()

np.random.seed(42)
sample_ages = np.random.randint(0,100,200)
sample_ages = pd.DataFrame(sample_ages, columns=['age'])

sns.rugplot(data=sample_ages, x='age')
plt.show()


sns.displot(data=sample_ages, x='age', rug=True, bins=30, kde=True)
plt.show()


sns.kdeplot(
    data=sample_ages, 
    x='age', 
    clip=[0,100], 
    bw_adjust=0.6,
    fill=True
)
plt.show()
