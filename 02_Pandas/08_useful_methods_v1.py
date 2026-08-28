import numpy as np
import pandas as pd

df = pd.read_csv('Pandas/Arquivos/tips.csv')

def last_four(num):
    return str(num)[-4:]

def yelp(price):
    if price < 10:
        return '$'
    elif price >= 10 and price < 30:
        return '$$'
    else :
        return '$$$'

if __name__ == '__main__':
    df['last_four'] = df['CC Number'].apply(last_four)
    # print(df['last_four'])

    # print(df['total_bill'].mean())
    df['yelp'] = df['total_bill'].apply(yelp)
    # print(df['yelp'])

    print(df)
