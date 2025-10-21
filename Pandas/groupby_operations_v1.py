import numpy as np
import pandas as pd

df = pd.read_csv('Pandas\\Arquivos\\mpg.csv')

# print(df['model_year'].unique())

# print(df['model_year'].value_counts())

# print(df.groupby('model_year').mean(numeric_only=True))
# Os parâmetros da função 'mean' são necessários devido à má formatação da coluna 'horsepower',
# que contém o caractere '?' e, por isso, foi interpretada como 'object' em vez de 'int'.
# Isso causa conflito ao calcular a média, pois há valores não numéricos.
# Caso essa inconsistência não existisse, o método 'mean' poderia ser chamado sem parâmetros adicionais.

# print(df.groupby('model_year').mean(numeric_only=True)['mpg'])

# print(df.groupby(['model_year', 'cylinders']).mean(numeric_only=True))

# print(df.groupby(['model_year', 'cylinders']).mean(numeric_only=True).columns)

# print(df.groupby(['model_year', 'cylinders']).mean(numeric_only=True).index)

# print(df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)['mpg'])

# print(df.groupby('model_year').describe())

# print(df.groupby('model_year').describe().transpose())

year_cyl = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)

print(year_cyl.index.names)
print(year_cyl.index.levels)
print(year_cyl.loc[70])
print(year_cyl.loc[[70, 82]])
print(year_cyl.index)
