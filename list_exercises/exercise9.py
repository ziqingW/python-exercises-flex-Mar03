matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
resultMatrix = []
for i in range(len(matrix1)):
    matrixadd = []
    for j in range(len(matrix1[i])):
        addnumber = matrix1[i][j] + matrix2[i][j]
        matrixadd.append(addnumber)
    resultMatrix.append(matrixadd)
print(resultMatrix)