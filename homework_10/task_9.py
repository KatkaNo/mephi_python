hard_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
norm_list= [i for inner in hard_list for last in inner for i in last]
print(norm_list)
