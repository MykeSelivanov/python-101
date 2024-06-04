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

d = {}
d["k"] = "v"
a = d
a["a"] = "b"
print(d, a) # {'k': 'v', 'a': 'b'} {'k': 'v', 'a': 'b'}
print(d is a) # True

s1 = set()
s2 = s1
s1.add(1)
s2.add(2)
print(s1 is s2) # True

# Copy a mutable object
a = [1, 2, 3]
b = a[:]
a.append(4)
print(a, b) # [1, 2, 3, 4] [1, 2, 3]
print(a is b) # False
