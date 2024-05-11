test = {
    2: "Hello", 
    "one": True
    }
print(test[2]) # Hello

x = {}
x["key"] = "value"
print(x["key"])

x["key2"] = "value2"
x["key3"] = "value3"
x["key4"] = "value4"
print(x)

del x["key"]
print(x) # {'key2': 'value2'}

keys = x.keys()
print(keys)
values = x.values()
print(values)

items = x.items()
print(items)
print(len(x))

for key in x:
    value = x[key]
    print(key, value)

for key, value in x.items():
    print(key, value)

test2 = {"key1": "value1", 2: "value2", 34: "value3", "key4": 10 }
test2["key5"] = test2.get("key5", 0) + 1
print(test2) # {'key1': 'value1', 2: 'value2', 34: 'value3', 'key4': 10, 'key5': 1}

characters = {}
str = "hello world"
for char in str:
    characters[char] = characters.get(char, 0) + 1
print(characters) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

counts = {}
while True:
    num = input("Number (enter q to quit): ")
    if num == "q":
        break
    num = int(num)
    counts[num] = counts.get(num, 0) + 1
print(counts)