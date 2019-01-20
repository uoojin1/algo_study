''' Robot in Grid

imagine a robot sitting on the upper left corner of a grid with r rows and c columns

the robot can only move in 2 directions. right and down

robot cannot step on 1s, only on 0s
design an algorithm to find a path for the robot from top left to the bottom right
'''

def robotPaths(field):
    if not field:
        return []
    allPath = []
    def helper(singlePath, i, j):
        if (i<0) or (j<0) or (i>=len(field)) or (j>=len(field[0])) or field[i][j] == 1:
            return
        if i == len(field)-1 and j == len(field[0])-1:
            allPath.append(singlePath + [(i,j)])
            return
        helper(singlePath + [(i,j)], i+1, j)
        helper(singlePath + [(i,j)], i, j+1)
    helper([], 0, 0)
    return allPath

'''
basically allPath = all paths to top or left + current
'''
def recursive(field):
    if not field:
        return []
    allPaths = []
    memo = {}
    def helper(path, i, j):
        if i < 0 or j < 0 or i >= len(field) or j >= len(field[0]) or field[i][j] == 1:
            return
        if i == len(field) - 1 and j == len(field[0])-1:
            allPaths.append(path)
        helper(path + [(i,j+1)], i, j+1)
        helper(path + [(i+1,j)], i+1, j)
    helper([(0,0)], 0,0)
    return allPaths

field = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

print recursive(field)




# print robotPaths(field)