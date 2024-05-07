my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# new_list = my_list[start:stop:step]
new_list = my_list[0:5:2]
print(new_list) # [0, 2, 4]

new_list_2 = my_list[:2]
print(new_list_2) # [0, 1]

new_list_3 = my_list[8:0:-1]
print(new_list_3) # [8, 7, 6, 5, 4, 3, 2, 1]

new_list_4 = my_list[7:]
print(new_list_4) # [7, 8, 9, 10, 11, 12]

new_list_5 = my_list[:4]
print(new_list_5) # [0, 1, 2, 3]

new_list_6 = my_list[::3] # every third
print(new_list_6) # [0, 3, 6, 9, 12]

new_list_7 = my_list[::-1] # reverse a list
print(new_list_7) # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

str = "hello world"
print(str[0:11:2]) # hlowrd

tup = (1, True, "hello", 4, 5)
print(tup[0:6:2]) # (1, 'hello', 5)
