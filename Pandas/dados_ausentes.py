import numpy as np
import pandas as pd

df = pd.read_csv('Pandas/Arquivos/movie_scores.csv')

'''
Exemplos rapidos sobre Dados Ausentes

print(np.nan) # Dado ausente 
print(pd.NA) # Dado ausente
print(pd.NaT) # O dado ausente é do tipo data/hora

print(np.nan == np.nan) # False, pois eu não tenho como comparar dados ausentes

print(np.nan is np.nan) # True, pois eu verifico se a váriavel é um Dado ausente

# Esse é um exemplo da linha acima - 'is nan'
myvar = np.nan 
print(myvar is np.nan) # True
'''

'''
print(df.isnull()) 
print(df.notnull())
print(df['pre_movie_score'].notnull())
print(df[df['pre_movie_score'].notnull()])
print(df[(df['pre_movie_score'].isnull()) & (df['first_name'].notnull())])
'''

'''
# Keep Data
print(df)
'''

'''
# Drop Data
print(df.dropna())
print(df.dropna(thresh=1))
print(df.dropna(axis=1))
print(df.dropna(subset=['last_name']))
'''

'''
# Fill Data
print(df.fillna('New Value!')) # Não recomendado, pode transformar colunas numericas em strings
print(df['pre_movie_score'].fillna(0))
print(df['pre_movie_score'].fillna(df['pre_movie_score'].mean()))
print(df.fillna(df.mean()))

# Interpolação
airline_tix = {'first':100, 'business':np.nan, 'economy-plus':50, 'economy':30}
ser = pd.Series(airline_tix)
print(ser.interpolate())
'''