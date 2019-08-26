#命名切片

items = [0, 1, 2, 3, 4, 5, 6] 
a = slice(2,4)
print(items[2:4])

print(items[a])

items[a] = [10,11]
print(items)

del items[a]
print(items)
