def create_matrix(size=3, up_fill=0, down_fill=0):
    matrix=[[0]*size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if i==j:
                matrix[i][i]=i+1
            elif i<j:
                matrix[i][j]=up_fill
            else:
                matrix[i][j] = down_fill

    return matrix

print(create_matrix(up_fill=7, down_fill=9))