import random
import math
import matplotlib.pyplot as plt

f = open('data.txt', 'w')
plt.ion()
# N = int(input())

N = 1000
LENGTH = 100
WIDTH = 100
K = 5

posx = []
posy = []

centerx = []
centery = []

# for i in range(K):
# 	centerx.append(random.random() * LENGTH)
# 	centery.append(random.random() * WIDTH)

centerx = [20, 75, 10, 85, 50]
centery = [20, 27, 67, 79, 54]

for i in range(K):
	for j in range(int(N / K)):
		x = (random.random() - 0.5) * (LENGTH / 2.5)
		y = (random.random() - 0.5) * (WIDTH / 2.5)

		if x + centerx[i] < 0 or y + centery[i] < 0:
			continue
		posx.append(x + centerx[i])
		posy.append(y + centery[i])
		f.write('{} {}\n'.format(x + centerx[i], y + centery[i]))

plt.scatter(posx, posy)
plt.show()
plt.savefig('data.jpg')
plt.pause(3)
plt.clf()
