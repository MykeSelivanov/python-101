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
