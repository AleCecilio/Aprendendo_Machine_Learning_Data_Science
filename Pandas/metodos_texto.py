import numpy as np
import pandas as pd

email = 'jose@email.com'
print(email.split('@'),'\n')

names = pd.Series(['andrew', 'bobo', 'claire', 'david', '5'])

print(names,'\n')
print(names.str.upper(),'\n')
print(names.str.isdigit(),'\n')

tech_finance = ['GOOG,APPL,AMZN','JPM,BAC,GS']
print(len(tech_finance),'\n')

tickers = pd.Series(tech_finance)
print(tickers,'\n')
print(tickers.str.split(','),'\n')
print(tickers.str.split(',').str[0],'\n')
print(tickers.str.split(',',expand=True),'\n')

messy_names = pd.Series(['andrew  ','bo;bo','   claire   '])
print(messy_names,'\n')
print(messy_names.str.replace(';','').str.strip().str.capitalize(),'\n')

def cleanup(name):
    name = name.replace(';','')
    name = name.strip()
    name = name.capitalize()
    return name 

print(messy_names.apply(cleanup))
