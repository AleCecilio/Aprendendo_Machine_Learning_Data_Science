import numpy as np
import matplotlib.pyplot as plt

labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]


# FIGURA 1 — COMPARAÇÃO SIMPLES ENTRE AS DUAS CURVAS
fig1 = plt.figure()
axes = fig1.add_axes([0.05,0.1,0.7,0.7])

axes.plot(july16_2007, label='july16_2007', color='#344cd1')
axes.plot(july16_2020, label='july16_2020' , color='orange')

axes.set_xticks(range(len(labels)))
axes.set_xticklabels(labels)

axes.legend(loc=(1.05,0.5))

plt.show()


# FIGURA 2 — COMPARAÇÃO VERTICAL ENTRE AS CURVAS
fig2, axes = plt.subplots(nrows=2, ncols=1)

# Subplot 1 — 2007
axes[0].plot(july16_2007)
axes[0].set_title('July 16th, 2007')
axes[0].set_xticks(range(len(labels)))
axes[0].set_xticklabels(labels)

# Subplot 2 — 2020
axes[1].plot(july16_2020)
axes[1].set_title('July 16th, 2020')
axes[1].set_xticks(range(len(labels)))
axes[1].set_xticklabels(labels)

plt.tight_layout()
plt.show()


# FIGURA 3 — EIXOS DUPLOS (DUAS ESCALAS Y)
fig3, axes1 = plt.subplots()

# Curva 2007 — eixo Y da esquerda (azul)
axes1.plot(labels,july16_2007, lw=2, color='blue')
axes1.set_ylabel('2007', fontsize=14, color='blue')

axes1.spines['left'].set_color('blue')
axes1.spines['left'].set_linewidth(2)

for label in axes1.get_yticklabels():
    label.set_color('blue')
plt.yticks(fontsize=12)    


# Curva 2020 — eixo Y da direita (vermelho)
axes2 = axes1.twinx()
axes2.plot(labels, july16_2020, lw=2, color='red')
axes2.set_ylabel('2020', fontsize=14, color='red')

axes2.spines['right'].set_color('red')
axes2.spines['right'].set_linewidth(2)

for label in axes2.get_yticklabels():
    label.set_color('red')
plt.yticks(fontsize=12)  

axes1.set_title('July 16th Yield Curves')

plt.show()
