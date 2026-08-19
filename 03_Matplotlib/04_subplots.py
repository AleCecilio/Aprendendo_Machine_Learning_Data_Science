import matplotlib.pyplot as plt
import numpy as np
import os

caminho = os.path.join(
    'C:\\Aprendendo_a_Programar\\Python\\Aprendendo_Machine_Learning_Data_Science\\Matplotlib\\Arquivos',
    'new_subplots.png'
)

a = np.linspace(0, 10, 11)
b = a **4

x = np.arange(0,10)
y = 2*x

# Fig 1
fig1, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x,y)
axes[1].plot(a,b)

# Fig 2
fig2, axes = plt.subplots(nrows=3, ncols=1)
for ax in axes:
    ax.plot(x,y)
plt.tight_layout()

# Fig 3
fig3, axes = plt.subplots(nrows=2, ncols=2, figsize=(4,10), dpi=100)
axes[0][0].plot(x,y)

axes[0][1].plot(x,y)
axes[0][1].set_ylabel('Y Label 0,1')

axes[1][0].plot(x,y)
axes[1][0].set_title('Title 1,0')
axes[1][0].set_xlim(2,6)

axes[1][1].plot(x,y)

fig3.suptitle('Figure Level',fontsize=16)
fig3.subplots_adjust(wspace=1, hspace=0.5)

fig3.savefig(caminho, bbox_inches='tight')

# Show all figures
plt.show()
