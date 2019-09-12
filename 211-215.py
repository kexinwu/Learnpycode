##第二章 2.10-2.15内容

#2.11删除字符串中不需要的字符
#问题:你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。

#strip() 方法能用于删除开始或结尾的字符。lstrip() 和 rstrip() 分别从左和 从右执行删除操作。默认情况下，这些方法会去除空白字符

# s= ' hello world \n'
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# t = '-----hello====='
# print(t.lstrip('-'))
# print(t.strip('-='))

#2.12  审查清理文本字符串
#问题 一些无聊的幼稚黑客在你的网站页面表单中输入文本”pýtĥöñ”，然后你想将这些 字符清理掉。

# s = 'pýtĥöñ\fis\tawesome\r\n'
# print(s)


# remap={
#      ord('\t'):' ',
#      ord('\f'):' ',
#      ord('\r'):None
#  }

# a= s.translate(remap)
# print(a)

# #如果你去测试的话，你就会发现这种方式会比使用 translate() 或者正则表达式 要快很多。 
# def clean_spaces(s):
#     s = s.replace('\r','')
#     s = s.replace('\t',' ')
#     s = s.replace('\f',' ')
#     return s
# b=clean_spaces(s)
# print(b)

#2.13  字符串对齐
#问题 你想通过某种对齐方式来格式化字符串

text = 'hello world'
#逐一对应下面format 且等价
print(text.ljust(20)) 
print(text.ljust(20,'*'))
print(text.rjust(20))
print(text.rjust(20,'*'))
print(text.center(20))
print(text.center(20,'*'))

print(format(text,'>20'))
print(format(text,'&>20'))
print(format(text,'<20'))
print(format(text,'&<20'))
print(format(text,'^20'))
print(format(text,'&^20'))

#当格式化多个值的时候，这些格式代码也可以被用在 format() 方法中。
print('{:>20s}{:>10s}'.format('hello','world'))

#format() 函数的一个好处是它不仅适用于字符串。它可以用来格式化任何值，使 得它非常的通用
x= 1.234
print(format(x,'>10'))
print( format(x, '^10.2f') )

#2.14 合并拼接字符串
#问题 你想将几个小的字符串合并为一个大的字符串

parts = ['Is', 'Chicago', 'Not', 'Chicago?'] 
parts1 =['ppp']
print(' '.join(parts))
print(','.join(parts))
print('.'.join(parts))

#2.15 字符串中插入变量
#问题 你想创建一个内嵌变量的字符串，变量被它的值所表示的字符串替换掉。

s = '{name} has {n} messages.' 
print( s.format(name='Guido', n=37) )

#如果要被替换的变量能在变量域中找到，那么你可以结合使用format_map() 和 vars() 
name = 'Guido' 
n = 37 
print(s.format_map(vars()) ) 