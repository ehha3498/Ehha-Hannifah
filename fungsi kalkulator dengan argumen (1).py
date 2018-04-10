my_list = [1, 5, 4, 6, 8, 11, 3, 12]

# filter out only the even items from a list
new_list = list(filter(lambda x: (x%2 == 0) , my_list))

#output: [4, 6, 8, 12]
print(new_list)

# double each item in a list using map()
new_list = list(map(lambda x: x * 2 , my_list))

# 0utput: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)
