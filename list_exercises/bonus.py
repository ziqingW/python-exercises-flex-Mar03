# create a function to calculate the value in each child-list in final multiply matrix
# arg m1row is each child-list in matrix1
# arg m2 is matrix2
# arg m1size is the size of matrix1
# this function can be applied for any matrix mutiplication(m1.row == m2.column)
def rowmulti(m1row, m2, m1size):
# mrow is the childlist for newly multiplied matrix
    mrow = []
    for i in range(m1size):
# rowresult to calculate each value of new childlist in final matrix
        rowresult = 0
        for j in range(len(m2)):
            rowresult += m1row[j] * m2[j][i]
        mrow.append(rowresult)
    return mrow

matrix1 = [[2,3], [4,5]]
matrix2 = [[2,7], [1,6]]
finalmatrix = []
for item in matrix1:
    finalmatrix.append(rowmulti(item, matrix2, len(matrix1)))
print(finalmatrix)