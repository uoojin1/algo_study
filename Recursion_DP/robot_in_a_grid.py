''' Robot in a grid

imagin robit sitting on the upper left corner of grid with
r rows and c columns
the robot can only move down or right
but certain cells, the robot cannot step on them
design an algorithm to find a path for the robot form the top
left to the bottom right
'''


'''
backtracking
'''

map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

def robotInAGrid(map):
    memo = {}
    def helper(i,j):
        print i,j
        if i==1 and j==0:
            return 1
        if i==0 and j==1:
            return 1
        sum = 0
        if 0 <= j-1 < 5 and map[i][j-1] == 0:
            if (i, j-1) in memo:
                sum += memo[(i, j-1)]
            else:
                memo[(i, j-1)] = helper(i, j-1)
                sum += memo[(i, j-1)]
        if 0 <= i-1 < 5 and map[i-1][j] == 0:
            if (i-1,j) in memo:
                sum += memo[(i-1,j)]
            else:
                memo[(i-1,j)] = helper(i-1,j)
                sum += memo[(i-1,j)]
        return sum
    return helper(2,2)

print robotInAGrid(map)
