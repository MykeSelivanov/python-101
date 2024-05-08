test = {
    2: "Hello", 
    "one": True
    }
print(test[2]) # Hello

x = {}
x["key"] = "value"
print(x["key"])

x["key2"] = "value2"
print(x)

del x["key"]
print(x) # {'key2': 'value2'}

