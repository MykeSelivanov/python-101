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