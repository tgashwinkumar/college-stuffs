first_lst = ['a', 's', 'h', 'w', 'i', 'n', 'k', 'u', 'm', 'a', 'r']
second_lst = [1 , 2, 0, 3, 4, 1, 0, 3, 2, 2, 0]

zip_lst = [(first_lst[i], second_lst[i]) for i in range(len(first_lst))]
print("The zipped list of original given lists: ", zip_lst)
for i in range(len(zip_lst)):
    min = i
    for j in range(i+1, len(zip_lst)):
        if zip_lst[min][1] > zip_lst[j][1]:
            min = j
    zip_lst[i], zip_lst[min] = zip_lst[min], zip_lst[i]
print("The sorted list ", zip_lst)
