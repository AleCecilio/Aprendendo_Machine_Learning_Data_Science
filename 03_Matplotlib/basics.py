import matplotlib.pyplot as plt
import numpy as np

x =  np.arange(0,10)
y = 2*x

plt.plot(x,y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.xlim(0,6)
plt.ylim(0,15)
plt.title('String Title')
plt.savefig('C:\\Aprendendo_a_Programar\\Python\\Aprendendo_Machine_Learning_Data_Science\\Matplotlib\\Arquivos\\myfirstplot.png')
plt.show()