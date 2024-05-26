def print_value(value):
    print(value)

print_value("hello")
print_value(1)
print_value(True)

def add_5(x, y):
    result = x + y + 5
    return result

result = add_5(10, 20)
print(result)

x, y, z = 1, 2, -10
def get_negative_sum(x, y, z):
    result = x + y + z
    if result < 0:
        return result
    return 1

print(get_negative_sum(x, y, z))

def new_range(start = 0, stop = 5):
    while start <= stop:
        print(start)
        start += 1
new_range()
new_range(3)
new_range(4, 7)
new_range(stop = 2)
