# https://leetcode.com/problems/rotate-image/

# You are given an n x n 2D matrix representing an image,
# rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to
# modify the input 2D matrix directly. DO NOT allocate another 2D matrix
# and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# %%


# NOTE: rotation boils down to
# 1. symetrical horizontal flip
# 2. transposition


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    edge_length = len(matrix)

    top = 0
    bottom = edge_length - 1

    while top < bottom:
        for col in range(edge_length):
            temp = matrix[top][col]
            matrix[top][col] = matrix[bottom][col]
            matrix[bottom][col] = temp
        top += 1
        bottom -= 1

    for row in range(edge_length):
        for col in range(row + 1, edge_length):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

    return matrix


# %%

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

# %%
rotate(matrix)

# %%
