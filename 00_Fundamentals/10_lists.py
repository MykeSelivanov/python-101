x = [1, 2, 3, True, "World", 3.14]
print(x[1]) # 2
print(x) # [1, 2, 3, True, 'World', 3.14]

x[2] = "Hello"
print(x) # [1, 2, 'Hello', True, 'World', 3.14]
x.append(False)
print(x) # [1, 2, 'Hello', True, 'World', 3.14, False]





