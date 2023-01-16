import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 3.5, 300)
y = np.sin(x * 3)

plt.plot(x, y, color = 'g', linestyle = '-', linewidth = 1, marker = 'o', markersize = 4, label = 'Line')

plt.yticks(np.linspace(-1, 1, 50))

plt.title('un plot')
plt.legend(loc = 1)
plt.grid(axis = 'x')
plt.grid(axis = 'y')
plt.xlabel('time', fontname = 'Courier New', fontsize = 10)
plt.ylabel('voltage')

plt.show()
