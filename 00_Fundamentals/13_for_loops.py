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

lst = [1, 2, 3, True, "Hello"]
for i in range(len(lst)):
    print(lst[i])

for element in lst:
    print(element)

for i, element in enumerate(lst):
    print("Idx: ", i, "Element: ", element)

tup = (2, 3, 4, "Hello", "world", True)
for i in range(len(tup)):
    element = tup[i]
    print(element)

for i, element in enumerate(tup):
    print(i, element)

str = "my string"
for i in range(0, len(str), 2):
    print(str[i])

lst = [1, 2, 3, 3, 5, 67, 345, 4, 4, 4, 4]
for num in lst:
    if num == 4:
        break
    print(num)

for num in lst:
    if num == 3:
        continue
    print(num)

for i in range(4):
    for j in range(4):
        for w in range(4):
            print(i, j, w)

list1 = [[1,2], [3,4], [5,6], [7,8]]
for i in range(len(list1)):
    internal_list = list1[i]
    for j in range(len(internal_list)):
        print(internal_list[j])


# Some examples
str = "hello world"
for i, char in enumerate(str):
    if char == "w":
        print("Postion of w is : ", i)

nums = []
for i in range(3):
    num = input("Enter a number: ")
    nums.append(int(num))
print(nums)

words = ("hello", "test", "this", "name", "123", "word")
target = "name1"
found = False
for word in words:
    if word == target:
        print("Target found")
        break
else: 
    print("Target not found")