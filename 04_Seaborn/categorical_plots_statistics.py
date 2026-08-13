import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/dm_office_sales.csv')

print(df['division'].value_counts(),'\n')

sns.countplot(data=df, x='division')
# plt.ylim(90,260)
plt.show()

sns.countplot(data=df, x='level of education', hue='division', palette='Set2')
plt.show()

print(df['level of education'].value_counts(),'\n')

sns.barplot(
    data=df, 
    x='level of education', 
    y='salary', 
    estimator=np.mean, 
    ci='sd',
    hue='division'
)
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()