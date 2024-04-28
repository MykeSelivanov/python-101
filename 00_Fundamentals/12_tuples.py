x = (1,2,3)

count = x.count(1)
print(len(x))
print(count)

contains = 2 in x
print(contains)

# nested tuple
y = (1, 2, (1, 2, 'Hello'), 3, 4, True, [])
print(y)
print(y[2][2])

a = (1,2)
b = (10,11)
combined = a + b
print(combined) # (1, 2, 10, 11)
multiplied = a * 2 # (1, 2, 1, 2)
print(multiplied)

y = 1, 2, 3, 4 # creates as a tuple as well
print(y)

# create a tuple from another tuple with changes
z = (y[0], 11, y[2])
print(z)