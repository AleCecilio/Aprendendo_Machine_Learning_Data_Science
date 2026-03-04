import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Arquivos/Advertising.csv')

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(df['TV'], df['sales'], 'o')
axes[0].set_title('TV Spend')
axes[0].set_ylabel('Sales')


axes[1].plot(df['radio'], df['sales'], 'o')
axes[1].set_title('Radio Spend')
axes[1].set_ylabel('Sales')

axes[2].plot(df['newspaper'], df['sales'], 'o')         
axes[2].set_title('Newspaper Spend')
axes[2].set_ylabel('Sales')

plt.tight_layout()
plt.show()


sns.pairplot(df)
plt.show()

X = df.drop(columns=['sales'])
Y = df['sales']

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=101)


#continua...
from sklearn.linear_model import LinearRegression
model = LinearRegression()