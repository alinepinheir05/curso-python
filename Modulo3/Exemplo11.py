my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
to_find1 = 2
to_find2 = 4
to_find3 = 1

for to_find1 in my_list:
    del my_list[to_find1]
    break
for to_find2 in my_list:
    del my_list[to_find2]
    break
for to_find3 in my_list:
    del my_list[to_find3]
    break
print(my_list)