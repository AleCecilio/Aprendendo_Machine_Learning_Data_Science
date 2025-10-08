import numpy as np
import pandas as pd 

df = pd.read_csv('Pandas/Arquivos/tips.csv')

def quality(total_bill, tip):
    if tip/total_bill > 0.25:
        return 'Generoso'
    else:
        return 'Outro'

'''
df['Quality'] = df[['total_bill', 'tip']].apply(
    lambda df: quality(df['total_bill'],df['tip']), 
    axis=1
)
'''

df['Quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])
print(df['Quality'])