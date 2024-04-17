x = [1, 2, 3, True, "World", 3.14]
print(x[1]) # 2
print(x) # [1, 2, 3, True, 'World', 3.14]

x[2] = "Hello"
print(x) # [1, 2, 'Hello', True, 'World', 3.14]
x.append(False)
print(x) # [1, 2, 'Hello', True, 'World', 3.14, False]

popped = x.pop()
print(popped) # False
print(x) # [1, 2, 'Hello', True, 'World', 3.14]

x.append(2)
x.append(2)
x.append(2)
print(x) # [1, 2, 'Hello', True, 'World', 3.14, 2, 2, 2]

count = x.count(2)
print(count) # 4

index = x.index(3.14)
print(index) # 5

remove = x.remove(2)
print(x) # [1, 'Hello', True, 'World', 3.14, 2, 2, 2]

list_contains_5 = 5 in x # another approach would be list_contains_5 = x.count(5) > 0
print(list_contains_5) # False

a = x[-1] # negative numbers access list elements from the end
print(a) # 2
b = x[-5]
print(b) # World

# Combine lists
x = [1,2,3]
y = [1,2]

combined = x + y
print(combined)

# Extend one of the lists
x.extend(y)
print(x)

# Nested Lists
lst = [[5,6,[]], [2,3], [1,2,3]]