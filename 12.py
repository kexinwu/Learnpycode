#解压可迭代对象赋值给多个变量
import numpy
def drop_first_last(grades):
    f ,*middle,l  = grades
    print(middle)
    return numpy.mean(middle)

print(drop_first_last([1,2,3,4]))

#星号表达式也能用在列表的开始部分
*trailing,current = [1,2,3,4,5,6]
print(sum(trailing)//len(trailing))
print(current)

#带有标签的元组序列： 
records = [('f',1,2),('b','hello'),('f',3,4)]
def do_f(x,y):
    print('f',x,y)
def do_b(s):
    print('b',s)

for tag ,*args in records:
    if tag =='f':
        do_f(*args)
    elif tag =='b':
        do_b(*args)

# 星号解压语法在字符串操作的时候也会很有用，比如字符串的分割
line = 'nobody:*:1:1:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fileds,homedir,sh = line.split(':')
print(uname)
print(sh)

#有时候，你想解压一些元素后丢弃它们，你不能简单就使用 * ，但是你可以使用一 个普通的废弃名称，比如 _ 或者 ign （ignore）。 
record = ('ACME',50,234.45,(12,4,2017))
name,*_,(*_,year) = record
print(name)
print(year)
        