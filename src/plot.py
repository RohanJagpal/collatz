import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np

with open('src/results.csv', "r+") as file:
    array = np.loadtxt(file, delimiter=",", skiprows=1)

plt.scatter(array[:, 0], array[:, 1])
#axs.plot(array[:, 0], array[:, 1])
#axs.set(ylabel='poo')

plt.show()