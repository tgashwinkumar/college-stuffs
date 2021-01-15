# Remove empty tuples from a list

lst = [(), ('a'), ('a', 'b'), (), (1, 2), (12312)]
print("The original list is: ", lst)

res = []
for x in lst:
    if x: res.append(x)
print("List with empty tuples removed is ", res)