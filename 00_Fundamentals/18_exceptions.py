try:
    int("hello")
except ValueError as e:
    print("Exception!", e)

print("Done")

try:
    2 / 0
except ValueError as e:
    print("Value Exception!", e)
except ZeroDivisionError as e:
    print("Zero Div Exception!", e)

print("Done 2")

try: 
    int("test")
except Exception as e:
    print("Exception!!!", e)
finally:
    print("Finally done!")

# raise ValueError("This is test error!")
# raise Exception("This is a general exception!")

while True:
    num = input("Enter a number: ")
    try: 
        num = float(num)
        break
    except ValueError:
        print("Not a valid float, try again!")