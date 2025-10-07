import numpy as np
import pandas as pd

df = pd.read_csv('Pandas\\Arquivos\\tips.csv')  

# print(df['total_bill'])

# mycols = ['total_bill', 'tip']

# print(df[['total_bill', 'tip']])

df['tip_percentage'] = 100 * df['tip'] / df['total_bill']

df['price_per_person'] = np.round(df['total_bill'] / df['size'], 2)

print(df.drop('tip_percentage', axis=1))

# df.drop('tip_percentage', axis=1, inplace=True) Permanentemente (Não recomendado)
df = df.drop('tip_percentage', axis=1) # Recomendado

print(df)
