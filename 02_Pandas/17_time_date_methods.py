import numpy as np
import pandas as pd

from datetime import datetime

myyear = 2015
mymonth = 1
myday = 1
myhour = 2
mymin = 30
mysec = 15

mydate = datetime(myyear, mymonth, myday)
print(mydate,'\n')  

mydatetime = datetime(myyear, mymonth, myday, myhour, mymin, mysec)
print(mydatetime,'\n')

print(mydatetime.year,'\n')


myser = pd.Series(['Nov 3, 1990', '2000-01-01', None])
print(myser,'\n')
timeser = pd.to_datetime(myser, format='mixed')
print(timeser, '\n')

obv_euro_date = '31-12-2000'
print(pd.to_datetime(obv_euro_date),'\n')

euro_date = '10-12-2000'
print(pd.to_datetime(euro_date, dayfirst=True),'\n')

style_date = '12--Dec--2000'
print(pd.to_datetime(style_date,format='%d--%b--%Y'),'\n')

custom_date = '12th of Dec 2000'
print(pd.to_datetime(custom_date),'\n')

sales = pd.read_csv('Pandas/Arquivos/RetailSales_BeerWineLiquor.csv')
print(sales,'\n')
print(sales['DATE'].dtypes,'\n')

sales['DATE'] = pd.to_datetime(sales['DATE'])
print(sales['DATE'].dtypes,'\n')


sales = pd.read_csv('Pandas/Arquivos/RetailSales_BeerWineLiquor.csv', parse_dates=[0])
print(sales['DATE'].dtypes,'\n')
print(sales['DATE'].dt.year,'\n')
print(sales['DATE'].dt.month,'\n')

sales = sales.set_index('DATE')
print(sales)

print(sales.resample(rule='YE').mean(),'\n')

