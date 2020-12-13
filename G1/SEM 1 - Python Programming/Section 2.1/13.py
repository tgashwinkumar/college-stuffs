k = int(input("Enter an arbitrary number: "))
n = 1
lst = [1]
print("n = 1")
for _ in range(k):
    n = (n + 1) % 100
    lst.append(n)
    print("n = {0}".format(n))
print("The largest number assigned to n is {0}".format(max(lst)))

# For k < 100, the largest number is k, while for k >= 100, the largest number assigned to n is 99.