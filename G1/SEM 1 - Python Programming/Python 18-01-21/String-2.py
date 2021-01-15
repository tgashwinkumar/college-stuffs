# Even length words in a string

sentence = "Here is the best program in the world"
print("The given string is \"", sentence, "\"")
words = sentence.split(" ")
res= [word for word in words if len(word)%2 == 0]
print("Even length words in the given string are ", res)