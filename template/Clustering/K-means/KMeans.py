import numpy as np
import matplotlib.pyplot as plt
import random
import math
from copy import deepcopy

data = np.genfromtxt('data.txt')
CNT = len(data) # total count of data
# print(CNT)

plt.ion()
k = 5
LENGTH = 100
WIDTH = 100
# print('{}, {}'.format(LENGTH, WIDTH))

center = []
cluster = [[] for i in range(k)]
distance = []

def Init_Center(_k):
	for i in range(_k):
		x = random.random() * LENGTH
		y = random.random() * WIDTH
		center.append([x, y])
	return center

def Cal_Distance(_k):
	for i in range(CNT):
		buf = []
		for j in range(_k):
			disx = data[i][0] - center[j][0]
			disy = data[i][1] - center[j][1]
			buf.append(math.sqrt(disx**2 + disy**2))
		distance.append(buf)

def Cal_Cluster(_k):
	for i in range(CNT):
		mindis = distance[i][0]
		minpos = 0
		for j in range(1, _k):
			if distance[i][j] < mindis:
				mindis = distance[i][j]
				minpos = j
		cluster[minpos].append(i)

def Cal_AverageCenter(_k):
	ret = []
	
	for j in range(_k):
		totx = 0
		toty = 0
		_cnt = 0
		for i in cluster[j]:
			totx += data[i][0]
			toty += data[i][1]
			_cnt += 1
		if _cnt == 0:
			continue
		ret.append([totx / _cnt, toty / _cnt])
	global center
	# global k
	if ret == center:
		return True
	center = deepcopy(ret)
	# k = len(center)
	return False

flag = False
center = Init_Center(k)
while flag == False:
	distance = []
	cluster = [[] for i in range(k)]
	print(center)
	Cal_Distance(k)
	Cal_Cluster(k)
	# print(cluster)
	flag = Cal_AverageCenter(k)

ansx = []
ansy = []
color = []
for i in range(k):
	for j in cluster[i]:
		ansx.append(data[j][0])
		ansy.append(data[j][1])
		color.append(i)

plt.scatter(ansx, ansy, c = color, cmap = 'viridis')
plt.savefig('ans.jpg')
plt.show()
plt.pause(5)
