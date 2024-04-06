x = 2
y = 4

compound = x < y and y + 2 > 3 and y - x >= x # True True True => True
print(compound) 

compound = x > y or y + 2 <= 3 or y - x - 1 >= x # False False False => False
print(compound)

