# ! not
# && and
# || or

x = 2
y = 4

# and
compound = x < y and y + 2 > 3 and y - x >= x # True True True => True
print(compound) 

# or
compound = x > y or y + 2 <= 3 or y - x - 1 >= x # False False False => False
print(compound)

# not
compound = not (x > y) # True
print(compound)

compound = not (x + 10 > y == y > x) # False
print(compound)  

compound = True or False and not True or False
print(compound)
# Operator Precedence
# 1 - not - compound = True or False and False or False
# 2 - and - compound = True or False or False
# 3 - or - compound = True or False, compound = True

