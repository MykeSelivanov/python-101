str = "hello world"

count = str.count("l")
print(count) # 3

index = str.find("w")
print(index) # 6

upper = str.upper()
print(upper) # HELLO WORLD

lower = str.lower()
print(lower) # hello world

str1 = "test"
print(str1.capitalize()) # Test

contains = "hel" in str
print(contains) # True

str2 = "21"
if str2.isdigit():
    x = int(str2)
    print(type(x))

# num = input("Number: ")
# if num.isdigit():
#     print("It's a number ")
#     print(int(num))
# else:
#     print('This is not a number')

str3 = "Hello, my name is Myke"
words = str3.split(",")
print(words)

str4 = "Hello. this is myke"
str5 = str4.replace(".", ",").replace("m", "M")
print(str5)
print(str4)


