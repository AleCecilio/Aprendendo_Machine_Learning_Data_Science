import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0, 10, 11)
b = a **4

x =  np.arange(0,10)
y = 2*x

fig = plt.figure()

# Larges Axes
axes1 = fig.add_axes([0.15,0.15,0.8,0.8])
axes1.plot(a,b)

axes1.set_xlim(0,8)
axes1.set_ylim(0,8000)
axes1.set_xlabel('A')
axes1.set_ylabel('B')
axes1.set_title('Power of 4')

# Small Axes
axes2 = fig.add_axes([0.25,0.5,0.25,0.25])
axes2.plot(x,y)

axes2.set_xlim(1,2)
axes2.set_ylim(0,30)
axes2.set_xlabel('X')
axes2.set_ylabel('Y')
axes2.set_title('Zoomed In')

plt.show()