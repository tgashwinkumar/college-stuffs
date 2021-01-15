def delbyrecur (string, substring):
    if len(string) == 0:
        return True
    if len(substring) == 0:
        return True
    while len(string) != 0:
        i = string.find(substring)
        if i == -1:
            return False
        string = string[:i] + string[i+len(substring):]
    return True

# String slicing in Python to check if a string can become empty by recursive deletion

string = "TTTTGGGG"
substring = "TG"

print("Result: ", delbyrecur(string, substring))