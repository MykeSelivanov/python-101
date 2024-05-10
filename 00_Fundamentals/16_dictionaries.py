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