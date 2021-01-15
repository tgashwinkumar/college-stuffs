# Add two matrices

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

res = matrix1

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        res[i][j] += matrix2[i][j]

print("The addition of the matrices is: [")
for row in res:
    print(row)
print("]")