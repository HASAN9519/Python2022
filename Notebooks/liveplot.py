# Live PLotting
import numpy as np
import matplotlib.pyplot as plt

x, y = [], []
for i in range(100):
    x.append(np.random.randint(1,100))
    y.append(np.random.randint(1,100))
    plt.scatter(x, y, color='lightblue')
    plt.grid(True)
    plt.pause(0.1)
plt.show()