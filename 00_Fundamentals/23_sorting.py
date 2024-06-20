lst = [2, 1, 3, 4, 3, 2, 3, 4, 1]
lst.sort()
print(lst)

lst2 = [4, 7, 11, 8, 3, 6, 2]
new_list = sorted(lst2)
print(lst2) # [4, 7, 11, 8, 3, 6, 2]
print(new_list) # [2, 3, 4, 6, 7, 8, 11]

lst.sort(reverse=True)
print(lst) # [4, 4, 3, 3, 3, 2, 2, 1, 1]

tup = (2, 1, 3, 4, 2, 3, 4, 1, 4, 3, 2)