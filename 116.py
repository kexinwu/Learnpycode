#过滤序列元素
#问题：你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
p = [n for n in mylist if n>0]
print(p)

q = (n for n in mylist if n>0)
for y in q:
    print(y)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        u = int(val)
        return True
    except ValueError:
        return False
#filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，就得像示例 那样使用 list() 去转换。
ivals = list(filter(is_int,values))
print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
import math 
t = [math.sqrt(n) for n in mylist if n >0]
print(t)

clip_neg = [n if n>0 else 0 for n in mylist]
print(clip_neg)

addresses = [ '5412 N CLARK', '5148 N CLARK', '5800 E 58TH', '2122 N CLARK', '5645 N RAVENSWOOD', '1060 W ADDISON', '4801 N BROADWAY', '1039 W GRANVILLE', ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more5 = [n>5 for n in counts]
print(more5)
o = list(compress(addresses,more5))
print(o)


