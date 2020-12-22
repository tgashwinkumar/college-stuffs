num = int(input("Enter a number: "))
i= 21
if num <= 1:
    print("{0} is not a Prime Number.".format(num))
else:
    while(i <= num/2):
        if(num % i == 0):
            print("{0} is not a Prime Number.".format(num))
            break
        i = i + 1
    else:
        print(num, " is a Prime Number.")
    
# Enter a number = 45
# 45 is not a Prime Number

# Enter a number =67
# 67 is a Prime Number