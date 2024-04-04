x = "4"
y = int(x)
print(type(x))
print(type(y))
print(y)

a = float("4.5") + 5
print(a)

y = bool("4")
print(y) # true
y = bool(2)
print(y) # true
y = bool(-10)
print(y) # true
y = bool("")
print(y) # false
y = bool(0)
print(y) # false

x = str(1) + " hello"
print(x)

number = input("Enter a number: ")
result = float(number) + 5
print("The result is: ", result)