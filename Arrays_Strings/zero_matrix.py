'''
Write an algo such that if an element in M x N matrix is 0,
its entire row and column are set to 0
'''


'''
iterate through each element, record the row and col of the zero
using 2 sets, set of zero row, set of zero column
'''

def zero_filler(matrix, M, N):
    zero_rows = set()
    zero_cols = set()
    for row in range(M):
        for col in range(N):
            # iterating through each element
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)
                break
    for row in range(M):
        for col in range(N):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0
    return matrix


# M = 2, N = 3
example_matrix = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
]

print(zero_filler(example_matrix,4,5))