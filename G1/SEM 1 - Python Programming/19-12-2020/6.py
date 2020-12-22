upp = int(input("Enter the upper bound value: "))
i = 2
while i <= upp:
    j = 2
    while j <= i/2:
        if i % j == 0:
            break
        j += 1
    else:
        print(i)
    i += 1


# Enter the upper bound value: 50
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47