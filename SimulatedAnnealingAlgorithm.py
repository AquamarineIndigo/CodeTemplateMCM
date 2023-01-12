# Simulated Annealing Algorithm
# https://blog.csdn.net/google19890102/article/details/45395257/
import math
import random

def function(x, y):
	# ret = -6*(x**7) - 8*(x**6) + 7*(x**3) + 5*(x**2) + 4 - x*y
	# ret = math.sin(x) + y
	ret = 0.01 * ((x-15) * (x-27) * (x-49) * (x-63) * (x-74) * (x-91)) * math.sin(x*math.pi / 100) + y
	return float(ret)

def getRand():
	return random.random() * 100

T = 100
Tmin = 1e-8
k = 500 # iteration times
delta = 0.98

def simulatedAnnealing(y):
	arr = []
	for i in range(k):
		arr.append(getRand())

	t = T
	result = float("inf")
	while t > Tmin:
		for i in range(k):
			funTmp = function(arr[i], y)
			xnew = arr[i] + (random.random() * 2 - 1) * t
			# get a random added to the chosen
			if xnew >= 0 and xnew < 100:
				# if xnew is not out of range
				tmpnew = function(xnew, y)
				if tmpnew - funTmp < 0:
					arr[i] = xnew
				else:
					p = 1 / (1 + math.exp(-(tmpnew - funTmp) / T))
					if random.random() < p:
						arr[i] = xnew

		t = t * delta

	for i in range(k):
		print("arr[", i, "] = ", arr[i], ", func(arr[i]) =", function(arr[i], y))
		if result > function(arr[i], y):
			result = function(arr[i], y)
	return result

# y = read()
y = 0
print("ret = 0.01 * ((x-15) * (x-27) * (x-49) * (x-63) * (x-74) * (x-91)) * math.sin(x*math.pi / 100) + y")
y = int(input())
for i in range(100):
	print("function(", i, ") =", function(i, y))
print(simulatedAnnealing(y))
