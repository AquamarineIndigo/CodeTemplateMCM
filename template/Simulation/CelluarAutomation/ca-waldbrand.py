# Simulation of Waldbrand
# Rules:
# trees being hit -> burn -> dead
# tree burn -> 8 neighboors burn with posibility of PIN
# 0 -> None; int -> age; -1 -> burn
import numpy as np
from matplotlib import pyplot as plt
import random

PGR = 0.01 # Posibility of growth
PLI = 6e-5 # Posibility of lightening
PIN = 0.7 # Posibility of being interfered to burn
PSP = 0.9 # Posibility of becoming blank space when burning
# L = int(input()) # initial size
LEN = 100
TIME = 2000
FIGPAUSE = 1e-7

plt.ion()
def printStatus(target, pause, gen = 0, tot = 0):
	bufx = []
	bufy = []
	colors = []
	for i in range(1, LEN + 1):
		for j in range(1, LEN + 1):
			if target[i, j] == 0:
				continue
			bufx.append(j)
			bufy.append(i)
			if target[i, j] > 0:
				colors.append('g')
			else:
				colors.append('r')
	plt.scatter(bufx, bufy, c = colors, alpha = 0.5, marker = 'x')
	# plt.colorbar()
	plt.show()
	plt.title('Generation = {}\nTotal Trees = {}'.format(gen + 1, tot))
	plt.pause(pause)
	plt.clf()
# https://www.runoob.com/matplotlib/matplotlib-scatter.html

init_row = [0 for i in range(LEN + 2)]
init_list = [init_row for i in range(LEN + 2)]
init_status = np.array(init_list)
del init_list
del init_row

printStatus(init_status, 1)
status = init_status
interfere = [np.zeros((LEN + 2, LEN + 2)), np.zeros((LEN + 2, LEN + 2))]
totcnt_tree = [0]

def setInterfere(posx, posy, gen):
	cnt = (gen + 1) % 2
	interfere[cnt][posx + 1, posy] += 1
	interfere[cnt][posx - 1, posy] += 1
	interfere[cnt][posx, posy + 1] += 1
	interfere[cnt][posx, posy - 1] += 1
	interfere[cnt][posx - 1, posy - 1] += 1
	interfere[cnt][posx - 1, posy + 1] += 1
	interfere[cnt][posx + 1, posy - 1] += 1
	interfere[cnt][posx + 1, posy + 1] += 1

for _cnt_generation in range(TIME):
	cnt_trees = 0
	for i in range(1, LEN + 1):
		for j in range(1, LEN + 1):
			if status[i, j] == -1:
				if random.random() < PSP:
					status[i, j] = 0
				else:
					setInterfere(i, j, _cnt_generation)
				continue
			if status[i, j] == 0:
				r = random.random()
				if r <= PGR:
					status[i, j] = 1
			if status[i, j] == 1:
				cnt_trees += 1
				if interfere[_cnt_generation % 2][i, j] > 0:
					if random.random() < (1 - (1 - PIN) ** interfere[_cnt_generation % 2][i, j]):
						status[i, j] = -1
						setInterfere(i, j, _cnt_generation)
				else:
					r = random.random()
					if r <= PLI:
						status[i, j] = -1
						setInterfere(i, j, _cnt_generation)

	interfere[_cnt_generation % 2] = np.zeros((LEN + 2, LEN + 2))
	printStatus(status, FIGPAUSE, gen = _cnt_generation, tot = cnt_trees)
	totcnt_tree.append(cnt_trees)

plt.plot([i for i in range(TIME + 1)], totcnt_tree, marker = ',', label = 'Trees count')
plt.xlabel('Generation')
plt.ylabel('Trees')
plt.title('Trees count in Waldbrand')
plt.savefig('result.jpg')
plt.show()
plt.pause(2)
plt.clf
