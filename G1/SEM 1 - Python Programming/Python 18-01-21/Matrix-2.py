# Program to multiply two matrices

matrix1 = [
    [1, 4, 5],
    [4, 5, 6],
    [0, 1, 0]
]

matrix2 = [
    [5, 6, 7],
    [0, 1, 0],
    [-1, 3, 2]
]

res = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        for k in range(len(matrix1)):
            res[i][j] += matrix1[i][k] * matrix2[k][j]

print("The multiplication of the matrices is: [")
for row in res:
    print(row)
print("]")