import numpy as np
import random
import math

f = open('data.txt', 'w')

def calFunction(index):
	# index: list[2]
	return -2.7 * (index[0]**2) + 1.3 * (index[1]**2)

for _cnt in range(10000):
	x = (random.random() - 0.5) * 50
	y = (random.random() - 0.5) * 50
	z = calFunction([x, y]) + (random.random() - 0.5) * 10
	f.write('{} {} {}\n'.format(x, y, z))
	
