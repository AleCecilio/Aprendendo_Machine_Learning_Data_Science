import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# plt.ion()

df = pd.read_csv('Arquivos/Advertising.csv')

print(df.head())

df['total_spend'] = df['TV'] + df['radio'] + df['newspaper']

print('\n', df.head())

plt.figure(figsize=(8.4, 2.8), dpi=120)
sns.regplot(data=df, x='total_spend', y='sales')
plt.subplots_adjust(top=0.98)
plt.show()

X = df['total_spend']
Y = df['sales']

# y = mx + b
# y = B1x + B0

print('\n',np.polyfit(X, Y, deg=1))

potential_spend = np.linspace(0, 500, 100)
predicted_sales = 0.04868788 * potential_spend + 4.24302822

plt.figure(figsize=(8.4, 2.8), dpi=120)
sns.scatterplot(data=df, x='total_spend', y='sales')
plt.plot(potential_spend, predicted_sales, color='red')
plt.show()

spend = 200 

predicted_sales = 0.04868788 * spend + 4.24302822
print(f'\nPrevisão de vendas para um gasto total de {spend} é de {predicted_sales:.2f} unidades')

'''
while plt.get_fignums():  # enquanto existir janela aberta
    plt.pause(0.1)
'''