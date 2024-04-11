name = input("Name: ")
if name == "Tim":
    print("Hello Tim!")

number = float(input("Enter a number below 5: "))
if number < 5:
    print("Number ", number, "is less than 5")
else:
    print("Number ", number, "is greater than 5") 

number = float(input("Enter a number: "))
if number < 0:
    print("Provided ", number, " is a negative number")
elif number == 0:
    print("Provided ", number, " is zero")
else:
    print("Provided ", number, " is positive")

# Nested statements
if number > 0 and number % 2 == 0:
    print(number, " is a positive even number")
    num2 = float(input("Enter another number: "))
    if num2 < 0:
        print(num2, " num2 is a negative number")
    else:
        print(num2, " num2 is a positive number")

# In-Line if statement
x = 5
result = "ok" if x > 5 else "not ok"
print(result)

name = "Mike"
print("Hello Mike") if name == "Mike" else print('Not Mike')
