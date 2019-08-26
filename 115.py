#通过某个字段将记录分组

from operator import itemgetter
from itertools import groupby
from collections import defaultdict
rows = [ {'address': '5412 N CLARK', 'date': '07/01/2012'}, {'address': '5148 N CLARK', 'date': '07/01/2012'}, {'address': '5800 E 58TH', 'date': '07/02/2012'}, {'address': '2122 N CLARK', 'date': '07/03/2012'}, {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'}, {'address': '1060 W ADDISON', 'date': '07/02/2012'}, {'address': '4801 N BROADWAY', 'date': '07/01/2012'}, {'address': '1039 W GRANVILLE', 'date': '07/04/2012'}, ]
#按照date排序
rows.sort(key=itemgetter('date'))
print(rows)
print('_'*50)
#一个非常重要的准备步骤是要根据指定的字段将数据排序。
#因为 groupby() 仅仅 检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果。#
# 如果把 rows.sort(key=itemgetter('date'))注释掉 结果完全不一样
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i,'!')

#如果你仅仅只是想根据 date 字段将数据分组到一个大的数据结构中去，并且允许 随机访问，那么你最好使用 defaultdict() 来构建一个多值字典
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)  
print('*'*40)  
print(rows_by_date)
for r in rows_by_date['07/01/2012']:
    print(r)