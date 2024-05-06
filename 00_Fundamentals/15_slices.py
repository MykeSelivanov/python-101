my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# new_list = my_list[start:stop:step]
new_list = my_list[0:5:2]
print(new_list) # [0, 2, 4]

new_list_2 = my_list[:2]
print(new_list_2) # [0, 1]

new_list_3 = my_list[8:0:-1]
print(new_list_3) # [8, 7, 6, 5, 4, 3, 2, 1]
