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


