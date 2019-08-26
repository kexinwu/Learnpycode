#转换并同时计算数据
# 问题：你需要在数据序列上执行聚集函数（比如 sum() , min() , max() ），但是首先你需 要先转换或者过滤数据

nums = [1,2,3,4]
s = sum (x*x for x in nums)
print(s)

#1.20合并多个字典或映射
#问题：现在有多个字典或者映射，你想将它们从逻辑上合并为一个单一的映射后执行某 些操作，比如查找值或者检查某些键是否存在
from collections import ChainMap
a = {'x': 1, 'z': 3 } 
b = {'y': 2, 'z': 4 }
#一个 ChainMap 接受多个字典并将它们在逻辑上变为一个字典。然后，这些字典并 不是真的合并在一起了，ChainMap 类只是在内部创建了一个容纳这些字典的列表并重 新定义了一些常见的字典操作来遍历这个列表。
c = ChainMap(a,b)

print(c['x']) # Outputs 1 (from a) 
print(c['y']) # Outputs 2 (from b) 
print(c['z']) # Outputs 3 (from a) 如果出现重复键，那么第一次出现的映射值会被返回。因此，例子程序中的 c['z'] 总是会返回字典 a 中对应的值，而不是 b 中对应的值。 

#对于字典的更新或删除操作总是影响的是列表中第一个字典。
c['z'] = 10
c['w'] = 40
del c['x']
print (a)
del c['y']

