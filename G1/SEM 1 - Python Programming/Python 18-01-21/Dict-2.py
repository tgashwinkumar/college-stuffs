# Convert key-value list to flat dictionary

lst = [("Tamilnadu", "Chennai"), ("Kerala", "Thiruvananthapuram"), ("Karnataka", "Bangalore"), ("Telangana", "Hyderabad")]
print("The original key-value list is: ", lst)
dct = dict()
for el in lst: 
    dct.update({el[0]: el[1]})
print("The result dictionary: ", dct)