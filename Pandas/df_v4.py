import numpy as np
import pandas as pd

df = pd.read_csv('Pandas\\Arquivos\\tips.csv')  

df = df.set_index('Payment ID')

# df = df.reset_index()

# print(df.iloc[0:4]) Posição

# print(df.loc[['Sun2959', 'Sun5260']])  Index

df = df.drop('Sun2959', axis=0)

one_row = df.iloc[[0]]
df = pd.concat([df,one_row])

print(df)
