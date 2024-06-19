# absolute value
print(abs(-10)) # 10

lst = [1,2,3,4,5]
print(max(lst)) # 5
print(max(1,10, -15)) # 10
print(min(lst)) # 1
print(min(-1, -20, 34, 56, -11)) # -20

x = max("a","b")
print(x) # b

print(sum(lst)) # 15
print(round(3.14)) # 3

# Math module
import math

x = math.sin(90)
print(x)

y = math.cos(math.pi)
print(y)

import random

random_num = random.randint(1, 200)
print(random_num)

rand_num2 = random.randrange(0, 1000, 10)
print(rand_num2)

lst = ["he", "hi", "ho", "hello"]
random_val = random.choice(lst)
print(random_val)