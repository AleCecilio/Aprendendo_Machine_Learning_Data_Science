import pandas as pd
import os

print(os.getcwd())

df = pd.read_csv('Pandas/Arquivos/example.csv',index_col=0)
print(df,'\n')

df.to_csv('Pandas/Arquivos/newflile.csv', index=True)

df = pd.read_csv('Pandas/Arquivos/newflile.csv')
print(df)