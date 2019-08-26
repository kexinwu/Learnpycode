#从字典中提取子集
#问题：你想构造一个字典，它是另外一个字典的子集

prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
#创建一个所有价格都大于200的字典
p1 = {key: value for key, value in prices.items() if value>200}
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key : value for key,value in prices.items() if key in tech_names}
#等价于p2
p2_2 ={key:prices[key] for key in prices.keys() & tech_names}
print(p1)
print(p2)
print(p2_2)