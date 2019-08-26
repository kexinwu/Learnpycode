#字典排序
# from collections import OrderedDict
# import json
# d = OrderedDict()
# d['foor'] = 1 
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4

# for key in d:
#     print(key,d[key])
# json.dumps(d)

#18字典的运算

prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
min_p = min(zip(prices.values(),prices.keys()))
max_p = max(zip(prices.values(),prices.keys()))

print(min_p)
print(max_p)

key_p1 = min(prices,key = lambda k: prices[k])
key_p2 = max(prices,key = lambda k: prices[k])

print(key_p1)
print(key_p2)

v_p1 = min(prices.values())
v_p2 = max(prices.values())

print(v_p1)
print(v_p2)