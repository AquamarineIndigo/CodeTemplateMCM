# Markov Chain Basic
'''
某人有 2 把伞，并在办公室和家之间往返．
如果某天他在家中(办公室时)下雨而且家中(办公室)有伞他就带一把伞去上班(回家)，不下雨时他从不带伞．
如果每天与以往独立地早上(晚上)下雨的概率为0.7，试求他被雨淋湿的机会．
'''
import numpy as np
import random
import os

'''
Posibility of umbrellas at home: [a, b, c]
Home -> Company: [a1, b1, c1] = [a0, b0, c0] * mat1
mat1 = 
[[1, 0, 0],
 [0.7, 0.3, 0],
 [0, 0.7, 0.3]]

Company -> Home: [a2, b2, c2] = [a1, b1, c1] * mat2
mat2 = 
[[0.3, 0.7, 0],
 [0, 0.3, 0.7],
 [0, 0, 1]]
'''

list1 = [[1, 0, 0], [0.7, 0.3, 0], [0, 0.7, 0.3]]
list2 = [[0.3, 0.7, 0], [0, 0.3, 0.7], [0, 0, 1]]
# list2 = [[0, 0, 1], [0, 0.3, 0.7], [0.3, 0.7, 0]]

mat1 = np.mat(list1)
mat2 = np.mat(list2)
# trans = mat2 * mat1
# print(trans)
print("mat1 = \n", mat1)
print("mat2 = \n", mat2)

ans = np.mat([0, 0, 1])
# ans.append(np.mat([0, 0, 1]))

for i in range(50):
	print("----iteration times = {}:".format(i))
	ans = np.dot(ans, mat1)
	print(ans)
	ans = np.dot(ans, mat2)
	print(ans)

print("ans = {}\niteration times = {}".format(0.7 * ans[0, 0], 50))