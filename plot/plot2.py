import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 3.5, 500)
y = np.sin(3 * x)
z = np.cos(np.arctan(x))

fig, ax = plt.subplots(1, 2, figsize = (14, 7))
ax[0].plot(x, y)
ax[1].plot(x, z)

ax[0].set_title('sin(3x)', fontsize = 18)
ax[1].set_title('cos(arctan(x))', fontsize = 18)

plt.show()

# matplotlib.org
# pyecharts.org
