#怎么样找到序列中出现次数最多的元素？

from collections import Counter

words =  [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ] 
word_counts = Counter(words)
print('結果')
print (word_counts)

top_three = word_counts.most_common(3)
print (top_three)

print (word_counts['not'])
print (word_counts['eyes'])

morewords = ['why','are','you','not','looking','in','my','eyes'] 
for word in morewords:
    word_counts[word] +=1
print(word_counts['eyes'])

#Counter 实例一个鲜为人知的特性是它们可以很容易的跟数学运算操作相结合。比 如： 
a = Counter(words)
b = Counter(morewords)
c =a + b
d =a - b
print (a)
print (b)
print (c)
print (d)

#毫无疑问，Counter 对象在几乎所有需要制表或者计数数据的场合是非常有用的 工具。在解决这类问题的时候你应该优先选择它，而不是手动的利用字典去实现。

