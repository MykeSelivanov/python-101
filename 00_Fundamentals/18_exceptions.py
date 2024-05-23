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