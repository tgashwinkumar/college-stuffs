def getMatrix(matrixNo, order):
    matrix = []
    for i in range(order):
        matrix.append([])
        for j in range(order):
            inputStr = "\nEnter a value at Matrix No: {0} row={1} ,column={2}: ".format(matrixNo, i+1, j+1)
            n = int(input(inputStr))
            matrix[i].append(n)
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()
    return None

def addMatrix(matrix1, matrix2):
    order = len(matrix1)
    result = []
    print(result)
    for i in range(order):
        result.append([])
        for j in range(order):
            result[i].append(matrix1[i][j] + matrix2[i][j])
    return result

def subMatrix(matrix1, matrix2):
    order = len(matrix1)
    result= [[0]*order]*order
    for i in range(order):
        result.append([])
        for j in range(order):
            result[i].append(matrix1[i][j] - matrix2[i][j])
    return result

order = int(input("\nEnter order of the matrix: "))
matrix1 = getMatrix(1, order)
print("\n\n")
matrix2 = getMatrix(2, order)
print("Matrix 1 :")
printMatrix(matrix1)
printMatrix(matrix2)
printMatrix(addMatrix(matrix1, matrix2))
