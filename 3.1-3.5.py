#第三章 数字日期和时间 3.1-3.5内容

#3.1数字的四舍五入
#问题：你想对浮点数执行指定精度的舍入运算

print(round (1.453,1))
print(round (-1.345,1))
#当一个值刚好在两个边界的中间的时候，round 函数返回离它最近的偶数。也就是 说，对 1.5 或者 2.5 的舍入运算都会得到 2。 
print(round (1.5,0))
print(round (2.5,0))

#传给 round() 函数的 ndigits 参数可以是负数，这种情况下，舍入运算会作用在 十位、百位、千位等上面
print(round (12567,-1))
print(round (12567,-2))
print(round (12567,-3))

#3.2执行精确的浮点数运算
#问题：你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现

#这些错误是由底层 CPU 和 IEEE 754 标准通过自己的浮点单位去执行算术时的特 征。由于 Python 的浮点数据类型使用底层表示存储数据，因此你没办法去避免这样的 误差。
a=4.2
b=2.1
print(a+b)

from decimal import Decimal
a=Decimal('4.2')
b=Decimal('2.1')
print(a+b) 

#3.3数字的格式化输出
#问题：你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。
x=1234.23456
print(format(x,'0.2f'))
print(format(x,'>10.2f'))
print(format(x,'<10.1f'))
print(format(x,'^10.1f'))

#3.4二八十六进制整数
#问题:你需要转换或者输出使用二进制，八进制或十六进制表示的整数
x=64
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

#3.5 字节到大整数的打包与解包
#问题:你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为 一个字节字符串。

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data,'little'))
print(int.from_bytes(data,'big'))