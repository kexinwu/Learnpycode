##第二章 2.16-2.20内容
#2.16 以指定列宽格式化字符串
#问题 你有一些长字符串，想以指定的列宽将它们重新格式化

# import textwrap
# s = "Look into my eyes, look into my eyes, the eyes, the eyes, the eyes, not around the eyes, don't look around the eyes, \ look into my eyes, you're under."
# print(textwrap.fill(s,60))
# print(textwrap.fill(s,10))

# print(textwrap.fill(s,50,subsequent_indent='   '))

# textwrap 模块对于字符串打印是非常有用的，特别是当你希望输出自动匹配终端 大小的时候。
# 你可以使用 os.get_terminal_size() 方法来获取终端的大小尺寸。
import os
print (os.get_terminal_size().columns)

#2.17 在字符串中处理 html 和 xml
#问题 你想将 HTML 或者 XML 实体如 &entity; 或 &#code; 替换为对应的文本。再者， 你需要转换文本中特定的字符 (比如 <, >, 或 &)。

import html
s = 'Elements are written as "<tag>text</tag>".' 
print(s)
print(html.escape(s))

#2.18 字符串令牌解析
#问题 你有一个字符串，想从左至右将其解析为一个令牌流
#感觉不太常用 不知道什么是令牌化 略过

#2.19 实现一个简单的递归下降分析器
#问题 你想根据一组语法规则解析文本并执行命令，或者构造一个代表输入的抽象语法 树。如果语法非常简单，你可以自己写这个解析器，而不是使用一些框架。
#也不常用 而且都是编译原理的东东 略

#2.20 字节字符串上的字符串操作
#问题 你想在字节字符串上执行普通的文本操作 (比如移除，搜索和替换)。

data = b'Hello World' 
print(data[0:5])
print(data.startswith(b'Hello') )
print( data.split() )
print(data.replace(b'Hello', b'Hello Cruel') )

