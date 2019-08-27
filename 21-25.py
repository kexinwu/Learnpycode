##第二章 字符串和文本
#2.1使用多个界定符分割字符串
#问题：你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定 的。

import re
line = 'asdf fjdk; afed, fjek,asdf, foo'
#函数 re.split() 是非常实用的，因为它允许你为分隔符指定多个正则模式。
# print(re.split(r'[;,\s]\s*',line))

# fields = re.split(r'(;|,|\s)\s*', line) 
# print(fileds)

# values = fields[::2]
# delimiters = fields[1::2] + ['']
# print(values)


#字符串开头或结尾匹配
#问题：你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme 等等。

# filename = 'spam.txt'
# flag = filename.endswith('.txt')
# print(flag)
# flag1 = filename.startswith('file:')
# print(flag1)
# url = 'http://www.python.org'
# flag2 = url.startswith('http:')
# print(flag2)

#os.listdir()用来陈列本文件下所有文件
# import os
# filenames = os.listdir('.')
# print(filenames)

# names = [name for name in filenames if name.endswith(('.txt'))]
# print(names)

from urllib.request import urlopen 

def read_data(name):
    if name.startswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()
choices = ['http:','ftp:']
url = 'http://www.python.org'
#这个方法中必须要输入一个元组作为参数。
# 如果你恰巧有一个 list 或 者 set 类型的选择项，要确保传递参数前先调用 tuple() 将其转换为元组类型。
# print (url.startswith(choices)) 结果错误
print (url.startswith(tuple(choices)) )

#2.3用 Shell 通配符匹配字符串
#问题：你想使用 Unix Shell 中常用的通配符 (比如 *.py , Dat[0-9]*.csv 等) 去匹配文 本字符串

from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
p = [name for name in names if fnmatch(name,'Dat*.csv')]
print(p)
#fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间。如果在 数据处理操作中只需要简单的通配符就能完成的时候，这通常是一个比较合理的方案

#2.4字符串匹配和搜索
#问题：你想匹配或者搜索特定模式的文本
text1 = '11/27/2012' 
text2 = 'Nov 27, 2012' 
import re
if re.match(r'\d+/\d+/\d',text1):
    print('yes')
else:
    print('no')

#2.5 字符串搜索和替换
#问题：你想在字符串中搜索和匹配指定的文本模式
text = 'yeah, but no, but yeah, but no, but yeah'
#对于简单的字面模式，直接使用 str.replace() 方法即可，比如： 
r = text.replace('yeah','yep')
print(r)

#对于复杂的模式，请使用 re 模块中的 sub() 函数。为了说明这个，假设你想将形 式为 11/27/2012 的日期字符串改成 2012-11-27 
#sub() 函数中的第一个参数是被匹配的模式，第二个参数是替换模式。反斜杠数字 比如 \3 指向前面模式的捕获组号。 
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2', text))




