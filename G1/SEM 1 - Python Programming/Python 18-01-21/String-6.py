# Replace duplicate Occurrence in String

string = "Gandhi was one of the important political leaders in the world . Gandhi was born in India . India is the one of the developing world powers ."
print("The original string: \"", string, "\"")
repl = [("Gandhi", "Mandela"), ("India", "South Africa")]
lst = string.split(" ")
for i in range(len(lst)):
    for j in repl:
        if lst[i] == j[0]:
            lst[i] = j[1]
result = " ".join(lst)
print("The replaced string: \"", result, "\"")
