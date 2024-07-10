# comprehensions
lst = []
for i in range(1,11):
    lst.append(i)
print(lst) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# list comprehension
lst2 = [i for i in range(1,11)]
print(lst2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lst3 = [i / 2 for i in range(1,11) if i % 2 == 0]
print(lst3) # [1.0, 2.0, 3.0, 4.0, 5.0]

# multiple assignments
x = y = 1
print(x, y) # 1 1

x, y = 1, 2
print(x, y) # 1, 2