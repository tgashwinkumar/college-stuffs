def ordered(n1,n2):
    return n1 < n2
num1 = int(input("Enter brother 1's age:"))
num2 = int(input("Enter brother 2's age:"))
if ordered(num1,num2):
    print("Brother 2 is the older brother")
elif ordered(num2,num1):
    print("Brother 1 is the older brother")
else:
    print("They are twins.")