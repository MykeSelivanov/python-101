x = 0
while x < 3:
    print(x)
    x += 1

num = input("Enter an integer: ")
while not num.isdigit():
    num = input("Enter an integer: ")

while True:
    num = input("Enter another integer: ")
    if num.isdigit():
        break

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 0
idx = 0
while result < 9 and idx < len(lst):
    num = lst[idx]
    result += num
    print(num)
    idx += 14

lst2 = [2, 3, 3, 2, -1, 2]
i = 0

while i < len(lst):
    if lst[i] == -2:
        print("-2 found!")
        break
    i += 1
else:
    print("didn't find -2")
