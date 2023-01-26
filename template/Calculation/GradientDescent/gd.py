import numpy as np
import matplotlib.pyplot as plt
import math

LEARNING_RATE = 5e-7
PARAMETER_LENGTH = 2
ITERATION_COUNT = 10000

def getFullIndex(index, is_matrix = False):
	if is_matrix == False:
		ret = [index[0]**2, index[1]**2]
	else:
		ret = [index[0, 0]**2, index[0, 1]**2]
	return ret

def TargetFunction(index: list, parameters: list):
	# index: list[2]; parameters: list[4]
	_full_index = getFullIndex(index)
	ret = 0
	for i in range(PARAMETER_LENGTH):
		ret += _full_index[i] * parameters[i]
	return ret

def CostFunction(_var: list, _val: list, para, dtype = list) -> float:
	# _full_index = getFullIndex(index)
	ret = 0
	_tot_set = len(_val)
	_para = []
	if dtype != list:
		for i in range(PARAMETER_LENGTH):
			_para.append(para[i, 0])
	else:
		_para = para.copy()
	for i in range(_tot_set):
		ret += (TargetFunction(_var[i], _para) - _val[i]) ** 2
	return ret / _tot_set

def Grad(_var_data, _value, parameters, _tot_set) -> np.mat: 
	# all are numpy.mat, all totalSet rows
	_full_var = []
	# print('parameter =\n{}'.format(parameters))
	# print('value = {}'.format(_value))
	for i in range(_tot_set):
		_full_var.append(getFullIndex(_var_data[i, :], is_matrix = True))
	_full_index = np.mat(_full_var)
	ret = []
	# print('_full_index = {}'.format(_full_index))
	_cost_function = _value.T - np.dot(_full_index, parameters)
	# print('cost = {}'.format(_cost_function))
	for i in range(PARAMETER_LENGTH):
		_sum = 0
		for j in range(_tot_set):
			_sum += _full_index[j, i] * _cost_function[j, 0]
		ret.append(LEARNING_RATE * _sum / _tot_set)
	# print('ret = {}'.format(ret))
	return np.mat(ret).reshape(PARAMETER_LENGTH, 1)

def StepLength(step: np.mat) -> bool:
	ret = 0
	for i in step:
		ret += i**2
	if math.sqrt(ret) <= 1e-6:
		return False
	return True

def GradientDescent(index: list, value: list, _tot_set: int) -> np.mat:
	X = np.mat(index)
	Y = np.mat(value)
	status = np.random.rand(PARAMETER_LENGTH).reshape(PARAMETER_LENGTH, 1)
	_cnt_process = 0
	print('Gradient Descent processing: [.', end = ' ')
	for i in range(ITERATION_COUNT):
		step = Grad(X, Y, status, _tot_set)
		status += step
		if StepLength(step) == False:
			break
		if _cnt_process < i / 100:
			_cnt_process += 1
			print('.', end = ' ')
	print(']\n', end = '')
	return status

data = np.genfromtxt('data.txt')
totalSet = len(data)
valueSet = []
variableSet = []
for i in range(totalSet):
	valueSet.append(data[i][2])
	variableSet.append([data[i][0], data[i][1]])
ans = GradientDescent(variableSet, valueSet, totalSet)
print('Result parameters =\n{}'.format(ans))
print('Cost Function = {}'.format(CostFunction(variableSet, valueSet, ans, dtype = np.mat)))
