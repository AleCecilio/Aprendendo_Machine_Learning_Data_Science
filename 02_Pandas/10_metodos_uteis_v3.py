import numpy as np
import pandas as pd

df = pd.read_csv('Pandas/Arquivos/tips.csv') 

'''
print(df.describe())
print(df.describe().transpose())
'''
'''
print(df.sort_values('tip'))
print(df.sort_values('tip', ascending=False))
print(df.sort_values(['tip', 'size']))
'''

'''
print(df['total-bill'].max())
print(df['total-bill'].idxmax())
print(df['total-bill'].min())
print(df['total-bill'].idxmin())
print(df.iloc[df['total-bill].idmin()])
'''
'''
print(df.corr())
'''

'''
print(df['sex'].value_counts())
print(df['day'].unique())
print(df['day'].nunique())
print(df['day'].value_counts())
'''

'''
print(df['sex'].replace(['Female', 'Male'], ['F', 'M']))
'''

'''
mymap = {'Female': 'F', 'Male': 'M'}
print(df['sex'].map(mymap))
'''

'''
print(df.duplicated())
'''

'''
simple_df = pd.DataFrame([1,2,2], ['a','b','c'])
print(simple_df.duplicated())
print(simple_df.drop_duplicates())
'''

'''
print(df[df['total_bill'].between(10,10,inclusive=True)])
'''

'''
print(df.nlargest(2, 'tip'))
print(df.sort_values('tip', ascending=False).iloc[0:2])
print(df.nsmallest(2, 'tip'))
print(df.sort_values('tip', ascending=True).iloc[0:2])
'''

'''
print(df.sample(5))
print(df.sample(frac=0.1))
'''