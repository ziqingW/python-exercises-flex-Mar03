# create a function to calculate the value of one childlist in final multiply matrix
# argument m1row is the childlist of matrix1
# argument m2 is matrix2
# argument m1size is the size(row) of matrix1
# this function can be applied for any matrix mutiplication(if (m1.row == m2.column) == True)
def rowmulti(m1row, m2, m1size):
# mrow is the childlist for final multiplied matrix
    mrow = []
    for i in range(m1size):
# rowresult restores the value of childlist in final matrix
        rowresult = 0
        for j in range(len(m2)):
            rowresult += m1row[j] * m2[j][i]
        mrow.append(rowresult)
    return mrow

matrix1 = [[2,3], [4,5]]
matrix2 = [[2,7], [1,6]]
finalmatrix = []
for item in matrix1:
# by calling the function rowmulti, add items(rows) to final matrix     
    finalmatrix.append(rowmulti(item, matrix2, len(matrix1)))
print(finalmatrix)