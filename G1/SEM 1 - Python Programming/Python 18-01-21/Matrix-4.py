# Displaying the kth element of a matrix

matrix = [
    [1, 4, 5],
    [3, 5, 6],
    [0, 1, 0]
]

k = int(input("Enter the column number (1-3): "))
column = []
for row in matrix:
    column.append(row[k])

print("The ", k, "th colummn is ", column)
