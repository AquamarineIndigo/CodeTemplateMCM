from scipy.optimize import linprog
# Linear Programming solves the minimizing problem.
# https://zhuanlan.zhihu.com/p/446462562
'''
maximize: z = x + 2*y
such that:
	2*x + y <= 20
	-4*x + 5*y <= 10
	-x + 2*y >= -2
	-x + 5*y >= 15
	x >= 0
	y >= 0

'''

obj = [-1, -2] # which is minimizing -z = -x - 2*y

lhs_ineq = [[2, 1], 
	   [-4, 5], 
	   [1, -2]]

rhs_ineq = [20, 
	    10, 
	    2]

lhs_eq = [[-1, 5]]
rhs_eq = [15]
bnd = [(0, float("inf")), (0, float("inf"))] # 0 to infinitive

opt = linprog(c = obj, A_ub = lhs_ineq, b_ub = rhs_ineq,
		A_eq = lhs_eq, b_eq = rhs_eq, bounds = bnd,
		method = "revised simplex")

print(opt)

'''
参数c是指来自目标函数的系数。A_ub和b_ub分别与不等式约束左边和右边的系数有关。同样，A_eq并b_eq参考等式约束。您可以使用bounds提供决策变量的下限和上限。

您可以使用该参数method来定义要使用的线性规划方法。有以下三种选择：

    method="interior-point"选择内点法。默认情况下设置此选项。
    method="revised simplex" 选择修正的两相单纯形法。
    method="simplex" 选择传统的两相单纯形方法。

linprog() 返回具有以下属性的数据结构：

    .con 是等式约束残差。
    .fun 是最优的目标函数值（如果找到）。
    .message 是解决方案的状态。
    .nit 是完成计算所需的迭代次数。
    .slack 是松弛变量的值，或约束左右两侧的值之间的差异。
    .status是一个介于0和之间的整数4，表示解决方案的状态，例如0找到最佳解决方案的时间。
    .success是一个布尔值，显示是否已找到最佳解决方案。
    .x 是一个保存决策变量最优值的 NumPy 数组。
'''
