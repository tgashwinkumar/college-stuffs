# Python program to find N largest elements from a list

lst = [23, 45, 67, 34, 12, 0, 67, 12, 23, 23, -67]
print("The original list is: ", lst)

## Sorts the list
for i in range(len(lst)):
    min = i
    for j in range(i+1, len(lst)):
        if lst[min] > lst[j]:
            min = j
    lst[i], lst[min] = lst[min], lst[i]

## Input the value of n
n = int(input("Enter value of n: "))
print(lst[-1:-n-1:-1])
