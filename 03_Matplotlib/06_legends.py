import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 11, 10)

fig = plt.figure()

ax = fig.add_axes([0.06,0.06,0.7,0.7])
ax.plot(x,x, label='X vs X')
ax.plot(x,x**2, label='X vs X^2')
ax.legend(loc=(1.05, 0.5))
plt.show()