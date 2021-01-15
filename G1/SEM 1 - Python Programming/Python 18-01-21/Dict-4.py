# Sorting dictionary key values list

dct = {
    'foo': [1, 5, 3],
    'bar': [23,-12],
    'huh': [45],
    "omg": [],
}

print("The original dictionary is : ", dct)

res = dict()
for key in sorted(dct):
    res[key] = sorted(dct[key])

print("The sorted dictionary is : ", res)
