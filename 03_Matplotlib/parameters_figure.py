import matplotlib.pyplot as plt
import numpy as np
import os 

caminho = os.path.join(
    'C:\\Aprendendo_a_Programar\\Python\\Aprendendo_Machine_Learning_Data_Science\\Matplotlib\\Arquivos',
    'new_figure.png'
)

a = np.linspace(0, 10, 11)
b = a **4

fig = plt.figure(figsize=(2,2),dpi=200)
axes1 = fig.add_axes([0.15,0.15,0.8,0.8])
axes1.plot(a,b)
fig.savefig(caminho, bbox_inches='tight')

plt.show()