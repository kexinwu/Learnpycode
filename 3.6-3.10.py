#第三章 数字日期和时间 3.6-3.10内容
#3.6 复数的数学运算
#问题:你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使 用复数空间。再或者是你仅仅需要使用复数来执行一些计算操作。

a=complex(2,4)
b=3-5j
print(a)
print(b)
print(a.real)
print(b.imag)

print(a+b)
print(a*b)
print(a/b)
print(abs(a))

import numpy as np
c=np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(c)
print(c+2)

#3.7无穷大与 NaN
#问题:你想创建或测试正无穷、负无穷或 NaN(非数字) 的浮点数。
d=float('inf')
print(d+45)
e=float('-inf')
print(e+d)

#3.8分数运算
#问题:你进入时间机器，突然发现你正在做小学家庭作业，并涉及到分数计算问题。或者 你可能需要写代码去计算在你的木工工厂中的测量值。

from fractions import Fraction
f=Fraction(5,4)
g=Fraction(7,16)
t=f+g
l=f*g
print(t)
print(l)
print(l.numerator)
print(l.denominator)

#3.9 大型数组运算
#问题:你需要在大数据集 (比如数组或网格) 上面执行计算

x = [1, 2, 3, 4] 
y = [5, 6, 7, 8] 
import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax)
print(ax+10)
print(ax*2)
print(ax+ay)
print(ax*ay)

v = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) 
print(v)
print(v[1])
print(v[:,1])
print(v[1:3,1:3])

#3.10 矩阵与线性代数运算
#问题:你需要执行矩阵和线性代数运算，比如矩阵乘法、寻找行列式、求解线性方程组等 等。

import numpy as np
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]]) 
print(m)
print(m.T)
print(m.I)
