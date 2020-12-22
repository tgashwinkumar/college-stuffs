num = int(input("Enter a number ="))
fact = 1
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1, num + 1):
       fact = fact * i
   print("The factorial of", num, "is", fact)

   #Enter a number =7
   #('The factorial of', 7, 'is', 5040)
