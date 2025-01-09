def rotate_image(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and j < i:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix_len = len(matrix)
    p1 = 0
    p2 = matrix_len - 1
    while p1 < p2:
        i = 0
        for _ in range(matrix_len):
            matrix[i][p1], matrix[i][p2] = matrix[i][p2], matrix[i][p1]
            i += 1
        p1 += 1
        p2 -= 1
    return matrix


# TODO: TRY WITH REAL IMAGE
image = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_image(image))
