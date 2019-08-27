##第二章 后6节内容
#2.6 字符串忽略大小写的搜索替换
#问题：你需要以忽略大小写的方式搜索与替换文本字符串

#为了在文本操作时忽略大小写，你需要在使用 re 模块的时候给这些操作提供 re.IGNORECASE 标志参数。比如：
import re 
text = 'UPPER PYTHON, lower python, Mixed Python'
result1 = re.findall('python',text,flags=re.IGNORECASE)
print(result1)

result2 = re.sub('python','snake',text,flags = re.IGNORECASE)
print(result2)

#对于一般的忽略大小写的匹配操作，简单的传递一个 re.IGNORECASE 标志参数就 已经足够了。

# 替换字符串并不会自动跟被匹配字符串的大 小写保持一致。

# 为了修复这个，你可能需要一个辅助函数，就像下面的这样： 
def matchcase(word): 
    def replace(m): # ??????????????????
        text = m.group() 
        print(text)
        if text.isupper(): 
            return word.upper() 
        elif text.islower(): 
            return word.lower() 
        elif text[0].isupper(): 
            return word.capitalize() 
        else: 
            return word 
    return replace


print (re.sub('python',matchcase('snake'),text,flags = re.IGNORECASE))

#2.7最短匹配模式
#问题：你正在试着用正则表达式匹配某个文本模式，但是它找到的是模式的最长可能匹 配。而你想修改它变成查找最短的可能匹配

#在这个例子中，模式 r'\"(.*)\"' 的意图是匹配被双引号包含的文本。但是在正 则表达式中 * 操作符是贪婪的，因此匹配操作会查找最长的可能匹配。于是在第二个 例子中搜索 text2 的时候返回结果并不是我们想要的。 

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
print(str_pat.findall(text2))

#为了修正这个问题，可以在模式中的 * 操作符后面加上? 修饰符，这样就使得匹配变成非贪婪模式，从而得到最短的匹配，也就是我们想要的结果
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

#2.8 多行匹配模式
# 问题:你正在试着使用正则表达式去匹配一大块的文本，而你需要跨越多行去匹配
comment = re.compile(r'/\*(.*?)\*/')
text3 = '/* this is a comment */'
text4 = '''/* this is a ... multiline comment */ ... ''' 

print(comment.findall(text3))
print(comment.findall(text4))

#2.9 将 Unicode 文本标准化
#问题:你正在处理 Unicode 字符串，需要确保所有字符串在底层有相同的表示

s1 = 'Spicy Jalape\u00f1o' 
s2 = 'Spicy Jalapen\u0303o'

print(s1)
print(s2)
print(s1 == s2)#false

print(len(s1)) #14
print(len(s2)) #15

#在需要比较字符串的程序中使用字符的多种表示会产生问题。为了修正这个问题， 你可以使用 unicodedata 模块先将文本标准化： 

import unicodedata
#normalize() 第一个参数指定字符串标准化的方式。
# NFC 表示字符应该是整体组 成 (比如可能的话就使用单一编码)，而 NFD 表示字符应该分解为多个组合字符表示。
t1 = unicodedata.normalize('NFC',s1)
print(ascii(t1))
t2 = unicodedata.normalize('NFC',s2)
print(ascii(t2))
print (t1 == t2)

t3 = unicodedata.normalize('NFD', s1)
t4 = unicodedata.normalize('NFD', s2)
print(ascii(t3))
print (t3 == t4)

#2.10 在正则式中使用 Unicode
#问题:你正在使用正则表达式处理文本，但是关注的是 Unicode 字符处理。
#混合使用 Unicode 和正则表达式通常会让你抓狂。如果你真的打算这样做的话，最 好考虑下安装第三方正则式库，它们会为 Unicode 的大小写转换和其他大量有趣特性 提供全面的支持，包括模糊匹配。

import re
num1 = re.compile('\d+')
print(num1)
print(num1.match('123'))
print (num1.match('\u0661\u0662\u0663'))