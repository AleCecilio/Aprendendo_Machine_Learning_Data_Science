import numpy as np
import matplotlib.pyplot as plt

m = np.linspace(0,10,11)
print(f"The array m should look like this: \n\n{m}\n")

c = 3 * 10**8
E = m*c**2

print(f"The array E should look like this: \n\n {E}\n")

fig = plt.figure()

axes = fig.add_axes([0.2,0.2,0.7,0.7])
axes.plot(E, color='#e6153f', lw=5)

axes.set_yscale('log')
axes.grid(alpha=0.5,linestyle='-', lw=1, axis='y', which='both')
axes.set_xlim(0)
axes.set_title('E=mc^2')
axes.set_xlabel('Mass in Grams')
axes.set_ylabel('Energy in joules')
plt.show()
