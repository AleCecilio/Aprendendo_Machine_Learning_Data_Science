import numpy as np
import matplotlib.pyplot as plt

labels = ['1 Mo','3 Mo','6 Mo','1 Yr','2 Yr','3 Yr','5 Yr','7 Yr','10 Yr','20 Yr','30 Yr']

july16_2007 =[4.75,4.98,5.08,5.01,4.89,4.89,4.95,4.99,5.05,5.21,5.14]
july16_2020 = [0.12,0.11,0.13,0.14,0.16,0.17,0.28,0.46,0.62,1.09,1.31]

fig1 = plt.figure()

axes = fig1.add_axes([0.05,0.1,0.7,0.7])
axes.plot(july16_2007, label='july16_2007', color='#344cd1')
axes.plot(july16_2020, label='july16_2020' , color='orange')
axes.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes.set_xticklabels(labels)
axes.legend(loc=(1.05,0.5))

plt.show()


fig2, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(july16_2007)
axes[0].set_title('July 16th, 2007')
axes[0].set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes[0].set_xticklabels(labels)

axes[1].plot(july16_2020)
axes[1].set_title('July 16th, 2020')
axes[1].set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
axes[1].set_xticklabels(labels)

plt.tight_layout()
plt.show()
