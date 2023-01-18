# TSP problem using Genetic Algorithm
import numpy as np
import matplotlib as plt
import random
import math

file = 'data.txt'
data = np.genfromtxt(file, dtype = float) # city locations
datalen = len(data)

print('Input iteration times:')
iter_times = int(input())

N = datalen # number of cities
pop = 100 # population
maxrandlen = int(N / 5)
acc = 2 # accelerate selection index
Pc = 0.8 # posibility of change
Pmutation = 0.05 # posibility of mutation

bestFitRecord = [] # [array[N], min_dis]
# f = open('runlog.txt', 'w+')
# print(data)
def init_dis(): # return: array[N, N]
	ret = []
	buf = []
	dist = 0
	for i in range(N):
		for j in range(N):
			if i == j:
				buf.append(0)
			else:
				dist = (data[i, 0] - data[j, 0]) ** 2
				dist += (data[i, 1] - data[j, 1]) ** 2
				dist = math.sqrt(dist)
				buf.append(dist)
		ret.append(buf)
		buf = []
	return np.array(ret)

dis = init_dis()
# print(dis)

def init_pop(): # return: array[pop, N]
	ret = []
	buf = []
	for i in range(pop):
		buf.append(0)
		for j in range(1, N):
			r = random.randint(1, N - 1)
			while (r in buf) == True:
				r = random.randint(1, N - 1)
			buf.append(r)
		ret.append(buf)
		buf = []
	return np.array(ret)

arr = init_pop()

def cal_dis(tar): # tar: array[N]; return: float
	ret = 0
	for i in range(N):
		if i < N - 1:
			ret += dis[tar[i], tar[i + 1]]
		else:
			ret += dis[tar[i], tar[0]]
	return ret

def cal_fitness(popmat): # popmat: array[pop, N]; return: array[pop], float
	buf = []
	sum = 0
	for i in range(pop):
		buf.append(cal_dis(popmat[i, :]))
	maxlen = max(buf)
	minlen = min(buf)
	ret = []
	for i in range(pop):
		# f.writelines('distance[{}] = {}\n'.format(i, buf[i]))
		ret.append((1 - (buf[i] - minlen)/(maxlen - minlen + 0.001)) ** acc)
		# f.writelines('fitness[{}] = {}\n'.format(i, ret[i]))
		sum += ret[i - 1]
	return np.array(ret), sum

# fit, totfit = cal_fitness(arr)
# maxfitval = fit.max(axis = None)
# maxfitpos = np.argmin(fit, axis = 0)

# print('maxfitval = {}, maxfitpos = {}'.format(maxfitval, maxfitpos))

def cross(tar1, tar2): # Position-Based Crossover; targets: array[N]
	# print('tar1 ={}\ntar2 ={}'.format(tar1, tar2))
	rlen = random.randint(1, maxrandlen)
	rval1 = [-1 for i in range(N)]
	rval2 = [-1 for i in range(N)]
	rpos1 = []
	rpos2 = []
	rval1[0] = rval2[0] = 0
	for i in range(rlen):
		rand = random.randint(1, N - 1)
		while (rand in rpos1) == True:
			rand = random.randint(1, N - 1)
		rpos1.append(rand)
		rval1[rpos1[i]] = tar1[rpos1[i]]
		val_index = np.where(tar2 == rval1[rpos1[i]])
		rpos2.append(int(val_index[0]))
		rval2[rpos2[i]] = tar2[rpos2[i]]
	cnt = 0
	for i in range(N):
		if rval1[i] == -1:
			while (tar2[cnt] in rval1) == True:
				cnt += 1
			rval1[i] = tar2[cnt]
			cnt += 1
	cnt = 0
	for i in range(N):
		if rval2[i] == -1:
			while (tar1[cnt] in rval2) == True:
				cnt += 1
			rval2[i] = tar1[cnt]
			cnt += 1
	# print('ret1 = {}\nret2 = {}'.format(rval1, rval2))
	return np.array(rval1), np.array(rval2)

# cross(arr[0, :], arr[1, :])
def mutation(tar): # tar: a copy of array[N]
	index1 = int(random.random() * (N - 1)) + 1
	index2 = int(random.random() * (N - 1)) + 1
	while (index2 == index1):
		index2 = int(random.random() * (N - 1)) + 1
	
	tar[index1], tar[index2] = tar[index2], tar[index1]
	return tar

for _iter_cnt in range(iter_times + 1):
	# f.write('----- iter = {}\n'.format(_iter_cnt))
	# f.writelines('arr = {}\n'.format(arr))
	# assess fitness
	fit, totfit = cal_fitness(arr) # fit: array[pop], totfit: float
	maxfitpos = np.argmax(fit, axis = 0)
	# print('maxfitval = {}, maxfitpos = {}'.format(maxfitval, maxfitpos))
	min_dis = cal_dis(arr[maxfitpos])
	# f.write('min_dis = {}\n'.format(min_dis))
	if bestFitRecord == []:
		bestFitRecord = [arr[maxfitpos], min_dis]
	elif min_dis < bestFitRecord[1]:
		bestFitRecord = [arr[maxfitpos], min_dis]
	# f.write('Best Record = {}\n'.format(bestFitRecord[1]))
	# selection
	# randomly select 2 and compare
	new_arr_list = []
	for i in range(pop):
		_index1 = int(random.random() * pop)
		_index2 = int(random.random() * pop)
		while _index2 == _index1:
			_index2 = int(random.random() * pop)
		if fit[_index1] > fit[_index2]:
			new_arr_list.append(arr[_index1, :])
		else:
			new_arr_list.append(arr[_index2, :])

	new_arr = np.array(new_arr_list)
	# crossover
	_perm = np.random.permutation(pop)
	for i in range(int(Pc * pop)):
		new_arr[_perm[i]], new_arr[_perm[i+1]] = cross(new_arr[_perm[i], :], new_arr[_perm[i+1], :])

	# Mutation
	for i in range(pop):
		if random.random() <= maxrandlen:
			new_arr[i] = mutation(new_arr[i, :])

	arr = new_arr
print('solution ={}\nminimum distance = {}'.format(bestFitRecord[0], bestFitRecord[1]))

# Input iteration times:
# 6003
# solution =[ 0 19 10 14 23  1 24  4  3 13 16 22 18  7  5  9 17 20 15 12 21  6  8  2
#  11]
# minimum distance = 26.16939047324117
