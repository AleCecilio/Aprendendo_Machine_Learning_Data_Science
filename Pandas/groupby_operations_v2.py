import numpy as np
import pandas as pd

df = pd.read_csv('Pandas\\Arquivos\\mpg.csv')


year_cyl = df.groupby(['model_year', 'cylinders']).mean(numeric_only=True)

# print(year_cyl.xs(key=70,level='model_year')) 

# print(year_cyl.xs(key=4,level='cylinders')) 
# É interessante definir como valor de uma variável, 
# por exemplo 'four_cyl'

'''
print(
    df[df['cylinders'].isin([6,8])]
    .groupby(['model_year', 'cylinders'])
    .mean(numeric_only=True)
)
'''

# print(year_cyl.swaplevel())

# print(year_cyl.sort_index('model_year',ascending=False))

# print(df.select_dtypes('number').agg(['std', 'mean'])) 
# No caso acima, o 'select_dtypes' só é necessário pois a coluna 'horsepower' 
# está mal formatada, em um arquivo melhor ele não seia usado

# print(df.select_dtypes('number').agg(['std', 'mean'])['mpg'])  

print(
    df.select_dtypes('number')
    .agg({
        'mpg':    ['max','mean'], 
        'weight': ['mean','std']
    })
)