import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 11, 10)

fig = plt.figure() 

ax = fig.add_axes([0.06, 0.06, 0.85,0.85])
# possible linestyle options '--', '-', '-.', ':', 'steps'

ax.plot(x,x, color='#e6153f', lw=2,marker='o', ls=':', ms=6, label='X vs X') # RGB HEX Code

lines = ax.plot(x,x-2,color='blue', linewidth=2, label='X vs X-2')
lines[0].set_dashes([5,2])

ax.plot(
    x,x+2,
    color='#b515e6', 
    linewidth=2, 
    marker='s',
    ls='--', 
    markersize=6,
    markerfacecolor='red', 
    markeredgewidth=2, 
    markeredgecolor='orange',
    label='X vs X+2'
)

ax.legend(loc=0)


plt.show()
