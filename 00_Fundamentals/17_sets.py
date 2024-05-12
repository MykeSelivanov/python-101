x = set()
y = {1, 2, 3, 1, 2, 3, 4}
print(type(x))
print(type(y))
print(y) # {1, 2, 3, 4}

x.add(1)
x.add(2)
x.add(3)
x.add(4)
x.remove(2)
print(x) # {1, 3, 4}
print(len(x)) # 3
x.clear()
print(x) # set()

