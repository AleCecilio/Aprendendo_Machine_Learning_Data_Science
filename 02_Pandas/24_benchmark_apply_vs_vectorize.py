"""
Descrição:
    Este script compara o tempo de execução de duas abordagens diferentes 
    para aplicar uma função em um DataFrame do Pandas:
        1. Usando o método DataFrame.apply()
        2. Usando numpy.vectorize()

    O objetivo é medir qual método apresenta melhor desempenho na criação 
    de uma nova coluna 'Quality', baseada na relação entre 'tip' e 'total_bill' 
    do dataset 'tips.csv'.
"""

import timeit

setup = '''
import numpy as np
import pandas as pd

df = pd.read_csv("Pandas/Arquivos/tips.csv")

def quality(total_bill, tip):
    if tip / total_bill > 0.25:
        return "Generoso"
    else:
        return "Outro"
'''

stmt_one = '''
df['Quality'] = df[['total_bill', 'tip']].apply(
    lambda df: quality(df['total_bill'],df['tip']), 
    axis=1
)
'''

stmt_two = '''
df['Quality'] = np.vectorize(quality)(df['total_bill'],df['tip'])
'''

print('apply:', timeit.timeit(setup=setup, stmt=stmt_one, number=1000))

print('vetorizado:', timeit.timeit(setup=setup, stmt=stmt_two, number=1000))