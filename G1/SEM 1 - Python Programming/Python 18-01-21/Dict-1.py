# Ways to remove a key from dictionary

dict = {
    "Tamilnadu": "Chennai",
    "Kerala": "Thiruvananthapuram", 
    "Karnataka": "Bangalore",
    "Telangana": "Hyderabad"
}

print("The original dictionary: ", dict)
key = input("Enter a key: ")
del dict[key]
print("The result dictionary: ", dict)
