import numpy as np
import matplotlib.pyplot as plt
import random
import math

ImageStr = '3-fin.jpg'
ImageNdArray = plt.imread(ImageStr)
# print(ImageData)
HEIGHT = len(ImageNdArray)
WIDTH = len(ImageNdArray[0])
FEATURES = 3
print('h = {}, w = {}'.format(HEIGHT, WIDTH))

ImageData = []
for i in range(HEIGHT):
	buf2 = []
	for j in range(WIDTH):
		buf1 = []
		for k in range(FEATURES):
			buf1.append(ImageNdArray[i, j, k])
		buf2.append(buf1)
	ImageData.append(buf2)
# print(ImageData)

FUZZY_WEIGHT_INDEX = 2 # m
ITERATION_TIMES = 10000
# ITERATION_THRESHOLD = 0.001
ITERATION_THRESHOLD = 100
K_TOTAL = 2

def Cal_DistanceSquare(pos1, target, cluster_type = 'All') -> float:
	if cluster_type == 'Red':
		return float((pos1[0] - target[0]) ** 2)
	ret = float(0)
	for i in range(FEATURES):
		ret += float(pos1[i] - target[i])**2
	return ret

def Cal_MembershipDegree(_center_list: list) -> np.array:
	ret = []
	# index = 1 / (FUZZY_WEIGHT_INDEX - 1)
	for _enum_center in range(K_TOTAL):
		buf = []
		for i in range(HEIGHT):
			for j in range(WIDTH):
				_sum = float(0)
				this_dis = Cal_DistanceSquare(ImageData[i][j], _center_list[_enum_center])
				for _sum_center in range(K_TOTAL):
					other_dis = Cal_DistanceSquare(ImageData[i][j], _center_list[_sum_center])
					if other_dis == 0:
						continue
					# _sum += math.pow(this_dis / other_dis, index)
					_sum += this_dis / other_dis
				if _sum == 0:
					buf.append(1)
				else:
					buf.append(1/_sum)
		ret.append(buf)
	return np.array(ret)

def Cal_ObjectiveFunction(_center_list: list, _membership_degree: np.array) -> float:
	ret = float(0)
	for _enum_center in range(K_TOTAL):
		for i in range(HEIGHT):
			for j in range(WIDTH):
				this_dis = Cal_DistanceSquare(ImageData[i][j], _center_list[_enum_center])
				_mem = math.pow(_membership_degree[_enum_center, i*WIDTH + j], FUZZY_WEIGHT_INDEX)
				ret += (this_dis * _mem)
	return ret

def UpdateClusteringCenter(_membership_degree: np.array) -> list:
	ret = []
	for _enum_center in range(K_TOTAL):
		_sum_base = 0
		_sum_posx = 0
		_sum_posy = 0
		_sum_posz = 0
		for i in range(HEIGHT):
			for j in range(WIDTH):
				_pow = math.pow(_membership_degree[_enum_center, i*WIDTH + j], FUZZY_WEIGHT_INDEX)
				_sum_base += _pow
				_sum_posx += (_pow * ImageData[i][j][0])
				_sum_posy += (_pow * ImageData[i][j][1])
				_sum_posz += (_pow * ImageData[i][j][2])
		buf = [_sum_posx / _sum_base, _sum_posy / _sum_base, _sum_posz / _sum_base]
		ret.append(buf)
	return ret

def getLabel(_center: list) -> list:
	ret = []
	for i in range(HEIGHT):
		buf = []
		for j in range(WIDTH):
			mindis = Cal_DistanceSquare(ImageData[i][j], _center[0])
			minpos = 0
			for k in range(1, K_TOTAL):
				_dis = Cal_DistanceSquare(ImageData[i][j], _center[k])
				if _dis < mindis:
					mindis = _dis
					minpos = k
			buf.append(minpos)
		ret.append(buf)
	return ret

# Initialize Center
center = []
for i in range(K_TOTAL):
	x = int(random.random() * HEIGHT)
	y = int(random.random() * WIDTH)
	while (ImageData[x][y] in center) == True:
		x = int(random.random() * HEIGHT)
		y = int(random.random() * WIDTH)
	center.append(ImageData[x][y])
print('iter = 0, center =\n{}'.format(center))

rec_ObjectiveFunction = 0
for _cnt_iteration in range(ITERATION_TIMES):
	membership = Cal_MembershipDegree(center)
	center = UpdateClusteringCenter(membership)
	obj = Cal_ObjectiveFunction(center, membership)
	print('obj = {}, center = {}'.format(obj, center))
	if (rec_ObjectiveFunction - obj < ITERATION_THRESHOLD) and (obj - rec_ObjectiveFunction < ITERATION_THRESHOLD):
		break
	rec_ObjectiveFunction = obj
print(center)
label = getLabel(center)

x = []
y = []
colors = []
plt.ion()
for i in range(HEIGHT):
	for j in range(WIDTH):
		x.append(j + 1)
		y.append(HEIGHT - i)
		colors.append(label[i][j])
plt.scatter(x, y, c = colors, cmap = 'bone', marker = ',')
plt.savefig('ans3.jpg')
plt.show()
plt.pause(4)
