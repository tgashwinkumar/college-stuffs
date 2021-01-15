# Program to print the duplicates from the list

lst = [23, 45, 67, 34, 12, 0, 67, 12, 23, 23, -67]
print("The original list is: ", lst)

repeated = []
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] == lst[j] and lst[j] not in repeated:
            repeated.append(lst[j])

print("The duplicates in the given list are ", repeated)