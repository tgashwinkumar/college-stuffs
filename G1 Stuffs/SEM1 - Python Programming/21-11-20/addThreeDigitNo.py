a = int(input("Enter a three digit no."))
b = int(input("Enter another third digit no."))
residue = 0
ans = 0
while(a!=0 or b!=0):
    temp1 = a%10
    temp2 = b%10
    sum = temp1 + temp2
    if sum>9:
        residue = 1
        sum = sum % 10
    else:
        residue = 0
    ans = ans*10 + sum
    a = a/10
    b = b/10
if residue==1:
    ans = residue *1000 + ans
print(ans)
