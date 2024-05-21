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

contains = 1 in x
print(contains)

x = {1, 2}
y = {2, 3}
z = x.union(y)
print(z) # {1, 2, 3}

z1 = x | y
print(z1) # {1, 2, 3}

x = {1, 2, 3}
x = {2, 3, 4, 5}
z = y.intersection(x)
print(z) # {2, 3}

z1 = x & y
print(z1) # {2, 3}

x = {1, 2, 3}
y = {1, 2, 4}
z = y.difference(x)
z1 = y - x
print(z) # {4}
print(z1) # {4}

a = {1, 2, 3}
b = {1, 2, 4}
a.update(b)
print(a)

b.difference_update(a)
print(b)

x = {1, 2, 3} # x is a subset of y
y = {1, 2, 3, 4, 5, 6} # y is a superset of x
print(x.issubset(y)) # True
print(x <= y) # True
print(y.issuperset(x)) # True
print(y >= x) # True
