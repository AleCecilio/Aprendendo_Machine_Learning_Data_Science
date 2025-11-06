import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/dm_office_sales.csv')

print(df.head())

plt.figure(figsize=(9.4,3.8), dpi=200)
sns.scatterplot(x='salary',y='sales',data=df)
plt.savefig('Seaborn/Arquivos/my_plot_v1.jpg')
plt.show()

plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    hue='level of education', 
    palette='Dark2'
)
plt.savefig('Seaborn/Arquivos/my_plot_v2.jpg')
plt.show()

plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    hue='work experience', 
)
plt.savefig('Seaborn/Arquivos/my_plot_v3.jpg')
plt.show()

plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    hue='work experience', 
    palette='viridis'
)
plt.savefig('Seaborn/Arquivos/my_plot_v4.jpg')
plt.show()


plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    size='work experience'
)
plt.savefig('Seaborn/Arquivos/my_plot_v5.jpg')
plt.show()


plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    s=200,
    alpha=0.2
)
plt.savefig('Seaborn/Arquivos/my_plot_v6.jpg')
plt.show()


plt.figure(figsize = (9.4, 3.8), dpi=200)
sns.scatterplot(
    x='salary', 
    y='sales', 
    data=df, 
    style='level of education',
    hue='level of education'
)
plt.savefig('Seaborn/Arquivos/my_plot_v7.jpg')
plt.show()
