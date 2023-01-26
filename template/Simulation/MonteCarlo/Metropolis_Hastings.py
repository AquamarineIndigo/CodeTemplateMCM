# Metropolis-Hastings Algorithm
# Used in Monte Carlo Simulation & Markov Chain
# p(x) = 1 / (pi * (1 + x**2))  Cauchy Distribution
# https://zhuanlan.zhihu.com/p/141528408
# https://www.cnblogs.com/emanlee/p/12370434.html
# https://zhuanlan.zhihu.com/p/109415693
import numpy as np
import matplotlib.pyplot as plt
import random
import math

STEPM = 100
SMCNT = 100000 # Samples cnt
SIGMA = 1 # Normal Distribution
LAM = 25
SCALE = 1.0

def CauchyProbability(x, pi = False):
	if pi == True:
		return 1 / (math.pi * (1 + (x / SCALE)**2) * SCALE)
	else:
		return 1 / (1 + x**2)

def getNormSample(x, sigma = SIGMA):
	# x = average
	return np.random.normal(x, scale = sigma, size = 1)[0]

def calNormProb(avg, x):
	const1 = math.sqrt(2 * math.pi) * SIGMA
	const2 = -2 * (SIGMA**2)
	return math.exp(((x - avg)**2) / const2) / const1

def calAcc(x0, x1):
	px0 = CauchyProbability(x0)
	px1 = CauchyProbability(x1)
	q1 = calNormProb(x0, x1)
	q0 = calNormProb(x1, x0)
	return (px1 * q1) / (px0 * q0)

def MetropolisHastings():
	x_init = random.random()
	ret = []
	for t in range(STEPM + SMCNT + 1):
		x_sample = getNormSample(x_init)
		accecptProb = min(1, calAcc(x_init, x_sample))
		if random.random() <= accecptProb:
			x_init = x_sample
		if t > STEPM:
			ret.append(x_init)
	return ret

# x0 = [(i / 100000) for i in range(100000)]
# y0 = [CauchyProbability(i / 100000, pi = True) for i in range(100000)]

i = -10
x0 = []
y0 = []
while i <= 10:
	x0.append(i)
	y0.append(CauchyProbability(i, True))
	i += 0.1
plt.subplot(1, 2, 1)
plt.plot(x0, y0)
plt.title('Cauchy Distribution')

# x1 = [i for i in range(100000)]
y1 = MetropolisHastings()
plt.subplot(1, 2, 2)
plt.hist(y1, 500)
plt.title('Simulated Cauchy Distribution')
plt.savefig('Metropolis_Hastings.jpg')
plt.show()
