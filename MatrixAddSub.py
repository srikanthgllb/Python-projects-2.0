row = int(input("enter the row number"))
col = int(input("enter the col number"))

print("Enter value for Matrix1: ")
matrix1 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix 1 : ")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j], "<3"), end="")
    print()

print("Enter value for Matrix2: ")
matrix2 = [[int(input()) for i in range(col)] for j in range(row)]
print("Matrix 2: ")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j], "<3"), end="")
    print()

#RESULT
result = [[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
print("The sum of matrices is : ")
#PrintResult
for i in range(row):
    for j in range(col):
        print(format(result[i][j], "<3"), end="")
    print()

