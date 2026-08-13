import numpy as np
import pandas as pd

'''
np.random.seed(101)
mydta = np.random.randint(0, 101, (4,3))
print(mydta)

myindex = ['CA', 'NY', 'AZ', 'TX']
mycolumns = ['Jan', 'Feb', 'Mar']

df = pd.DataFrame(data=mydta, index=myindex, columns=mycolumns)

print(f'\n{df}')
print(df.info())
'''

#                'Pandas/Arquivos/tips.csv'
#                r'Pandas\Arquivos\tips.csv'
df = pd.read_csv('Pandas\\Arquivos\\tips.csv')  

# pd.set_option('display.max_rows', None)   # Mostra todas as linhas
# pd.set_option('display.max_columns', None)  # Mostra todas as colunas
print(df)
