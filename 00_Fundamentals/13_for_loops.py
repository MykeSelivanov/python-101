for i in range(5):
    print(i)

for i in range(10, 15):
    print(i)

for i in range(20, 35, 5):
    print(i)

result = 0
for i in range(1, 11):
    result += i
print("Result: ", result)

lst = [1, 2, 3, 4, 5, True, "Hello"]
for i in range(len(lst)):
    print(lst[i])