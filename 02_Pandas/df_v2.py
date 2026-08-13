import numpy as np
import pandas as pd

df = pd.read_csv('Pandas\\Arquivos\\tips.csv')  

print(df.columns)
print(df.index)
print(df.head(10))
print(df.tail(10))
print(df.info())
print(df.describe())
print(df.describe().transpose())