import pandas as pd
import numpy as np

df = pd.read_csv('Pandas/Arquivos/Sales_Funnel_CRM.csv')

licenses = df[['Company', 'Product', 'Licenses']]
print(pd.pivot(
    data=licenses,
    index='Company',
    columns='Product',
    values='Licenses'),'\n'
)

print(pd.pivot_table(
    df, 
    index='Company',
    values=['Licenses','Sale Price'],
    aggfunc='sum'),'\n'
) 

# Mesmo Reusltado com groupby
print(df.groupby('Company').sum()[['Licenses','Sale Price']],'\n')

print(pd.pivot_table(
    df,
    index=['Account Manager','Contact','Product'],
    values=['Sale Price'],
    aggfunc=[np.sum], # Em versões futuras do pandas será ideal usar 'sum'
    fill_value=0, 
    margins=True),'\n'
)
