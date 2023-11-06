# Michelle Oteri
#2252197
input_list = input().split()

input_list = [int(x) for x in input_list]


non_negatives = [x for x in input_list if x >= 0]


sorted_list = sorted(non_negatives)


for num in sorted_list:
    print(num, end=' ')