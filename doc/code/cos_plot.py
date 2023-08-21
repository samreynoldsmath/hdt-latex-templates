import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 200)
x = np.cos(5 * t)

plt.figure()
plt.plot(t,x)
plt.show()
