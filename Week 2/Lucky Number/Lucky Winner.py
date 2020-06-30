from copy import deepcopy

inp = input().split(" ")
n, k = int(inp[0]), int(inp[1])
matrix = []
for i in range(n):
    row = input().split(" ")
    matrix.append([int(x) for x in row])
res = 0

def go(matrix,n,k,res):
    matrix1 = deepcopy(matrix)
    # print(matrix,res)
    if k == 0:
        return res
    hor = []
    col = []
    for row in matrix:
        hor.append(row[0] + row[1])
        hor.append(row[1] + row[2])
    max_hor = max(hor)
    for c in range(3):
        for i in range(1, n):
            col.append(matrix[i][c] + matrix[i - 1][c])
    max_col = max(col)
    #if greedily takes horizontal
    index = hor.index(max_hor)
    m = index // 2
    mm = index % 2
    if mm:
        hor[m*2] -= matrix[m][1]
        matrix[m][2] = 0
        if m == 0:
            col[n] = 0
            col[n*2] = 0
    else:
        hor[m*2+1] -= matrix[m][1]
        matrix[m][0] = 0
    matrix[m][1] = 0
    hor[index] = 0
    # if greedily takes vertical
    index = col.index(max_col)
    m = index // (n-1)
    mm = index % (n-1)
    if mm == 0:
        col[m*2+1] -= matrix1[mm+1][m]
    elif mm == n-2:
        col[m*2+mm-1] -= matrix1[mm][m]
    else:
        col[m*2+mm-1] -= matrix1[mm][m]
        col[m*2+mm+1] -= matrix1[mm+1][m]
    matrix1[mm+1][m] = 0
    matrix1[mm][m] = 0
    col[index] = 0
    return max(go(matrix,n,k-1,res+max_hor),go(matrix1,n,k-1,res+max_col))

print(go(matrix,n,k,res))