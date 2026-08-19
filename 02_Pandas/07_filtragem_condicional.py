import numpy as np
import pandas as pd


df = pd.read_csv('Pandas\\Arquivos\\tips.csv')  

# print(df[df['total_bill'] > 40])

# print(df[df['sex'] == 'Male'])

# print(df[df['size'] > 3])

pd.set_option('display.max_columns', None)

# print(df[(df['total_bill'] > 30) | (df['sex'] == 'Male')])

# print(df[(df['total_bill'] > 30) & (df['sex'] == 'Male')])
 
# print(df[(df['day'] == 'Sun') | (df['day'] == 'Sat') | (df['day'] == 'Fri')])

opitions = ['Sun', 'Set', 'Fri']
print(df[df['day'].isin(opitions)])