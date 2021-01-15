# Program to find transpose of a matrix

matrix = [
    [1, 4, 5],
    [3, 5, 6],
    [0, 1, 0]
]

for i in range(0, len(matrix)):
    for j in range(i+1, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("The transpose of the matrix is  is: [")
for row in matrix:
    print(row)
print("]")