# Equality
cond = 2 == 3
print(cond) # False

cond = 3.0 == 3
print(cond) # True

cond = 3.1 != 3
print(cond)

x = 5
y = 6
print(x == y)

cond = x < 9
print(cond)

cond = x >= 5
print(cond)

# Compare strings
str1 = "hello"
str2 = "hello"
cond = str1 == str2
print(cond) # True

str1 = "a"
str2 = "b"
cond = str1 < str2
print(cond)

cond = True == 1 # True
print(cond)
cond = False == 0 # True
print(cond)
True == "" # False
True == "True" # False