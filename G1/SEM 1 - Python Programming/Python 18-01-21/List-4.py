# Break a list into chunks of size of N 

lst = [23, 45, 67, 34, 12, 0, 67, 12, 23, 23, -67]
print("The original list is: ", lst)

n = int(input("Enter a value of n: "))
for i in range(0, len(lst), n):
    print(lst[i:i+n])

