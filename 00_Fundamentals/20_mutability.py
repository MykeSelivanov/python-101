# immutable data types
# int, float, str, tuple, bool

# mutable data types
# set, list, dict

x = [1, 2, 3]
y = x
print(y) # [1, 2, 3]
x.remove(1)
print(y) # [2, 3]

a = 1
b = a
print(id(a)) # 4397133536
print(id(b)) # 4397133536 both a and b point to the same object

x = []
def func(lst, x):
    lst.append(x)
    print(lst)

a = []
func(a, 2) # [2]
print(a) # [2] - because a was mutated in the function call