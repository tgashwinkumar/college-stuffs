# (a) What is the value of variables num1 and num2 after the following instructions are executed?
num = 0
k = 5
num1 = num + k * 2
num2 = num + k * 2
print(num1)
print(num2)
# num1 = num2 = 10

# (b) Are the values id(num1) and id(num2) equal after the last statement is executed?
print(id(num1))
print(id(num2))
# YES, The values of id(num1) and id(num2) are equal, and it is 140719476258880
