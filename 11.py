#解压序列赋值给多个变量
p = (4,5)
x, y = p
print(x)

data = ['ddd', 90, 67.99, (2068,67,89)]
a,b,c,(y,m,d) = data

print(y)

s = 'hello'
a,b,c,d,e = s
print(a ,b ,c ,d ,e )