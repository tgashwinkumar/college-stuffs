string = "i i am am a a programmer programmer programmer"
print("The given string is \"", string, "\"")
lst = string.split(" ")
res = []
for word in lst:
    if word not in res:
        res.append(word)
print("The string without duplicates: \""," ".join(res), "\"")
