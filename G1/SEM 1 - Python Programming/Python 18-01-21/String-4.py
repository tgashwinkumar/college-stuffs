string = "Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et."
print("The given string is \"", string, "\"")
lst = string.split(" ")
k = int(input("Enter length of the word: "))
words = [word for word in lst if len(word) > k]
print("The desired words are : ", words)

