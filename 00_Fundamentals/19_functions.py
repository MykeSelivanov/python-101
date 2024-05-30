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

def return_values(x, y, z):
    return x + 1, y + 1, z + 1
print(return_values(2, 3, 4)) # (3, 4, 5)

def remove_chars(base, chars):
    new_string = base
    for char in chars:
        new_string = new_string.replace(char, "")
    
    return new_string

result = remove_chars("hello world", "l")
print(result) # heo word

def sum_lists(list1, list2):
    def sum_list(lst):
        total = 0
        for num in lst:
            total += num
        return total
    list1_sum = sum_list(list1)
    list2_sum = sum_list(list2)
    return list1_sum, list2_sum

sum1, sum2 = sum_lists([1,2,3,4,5], [0,10,20,30,40])
print(sum1, sum2) #15 100
