#通过某个关键字排序一个字典列表
from operator import itemgetter
rows = [ {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}, {'fname': 'David', 'lname': 'Beazley', 'uid': 1002}, {'fname': 'John', 'lname': 'Cleese', 'uid': 1001}, {'fname': 'Big', 'lname': 'Jones', 'uid': 1004} ]

rows_by_fname = sorted(rows,key = itemgetter('fname'))
rows_by_uid = sorted(rows,key = itemgetter('uid'))

print(rows_by_fname)
print('__'*10)
print(rows_by_uid)

print (min (rows,key = itemgetter('uid')))
print (max (rows,key = itemgetter('uid')))