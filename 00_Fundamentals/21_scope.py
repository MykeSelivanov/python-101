def foo():
    x = 0

foo()
# print(x) # NameError: name 'x' is not defined

inp = int(input(("Enter a number: ")))
if inp > 5: 
    value  = "Greater than 5!"
else: 
    value = "Not greater than 5!"

print(value)

def append_5(x):
    x = x[:]
    x.append(5)
    print(x)
x = []
print(x)
append_5(x)
print(x)

# global keyword is considered a bad practice
value = 5
def foo():
    global  value # actually changes the value that is outside of the scope of this function
    value = 10

print(value) # 5
foo()
print(value) # 10
