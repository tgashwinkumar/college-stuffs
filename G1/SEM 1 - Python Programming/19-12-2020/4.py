num = int(input("Enter a number: "))
i = 2
while i <= num/2:
    if num % i == 0 :
        print(i)
    i += 1


# Enter a number: 24
# 2
# 3
# 4
# 6
# 8
# 12