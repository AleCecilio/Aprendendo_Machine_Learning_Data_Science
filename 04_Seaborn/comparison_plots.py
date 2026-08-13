import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Seaborn/Arquivos/StudentsPerformance.csv')

# Padrão
sns.jointplot(data=df, x='math score', y='reading score', kind='scatter', alpha=0.2)
plt.show()

# Hexagonos 
sns.jointplot(data=df, x='math score', y='reading score', kind='hex')
plt.show()

# Histograma (Blocos "Pixelados")
sns.jointplot(data=df, x='math score', y='reading score', kind='hist')
plt.show()

# Kde
sns.jointplot(data=df, x='math score', y='reading score', kind='kde', fill=True)
plt.show()

sns.jointplot(data=df, x='math score', y='reading score', hue='gender')
plt.show()

# Gráfico de pares
sns.pairplot(df, hue='gender', diag_kind='kde', corner=True)
plt.show()
