# Count occurences of an element in a list

lst = [23, 45, 67, 34, 12, 0, 67, 12, 23, 23, -67]
print("The original list is: ", lst)

el = int(input("Enter an element from the list: "))

count = 0
for i in lst:
    if i == el:
        count += 1
print("The given element ", el, " occurs ", count, " time(s) in the given list")