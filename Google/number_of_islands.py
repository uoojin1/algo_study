''' number of islands

given 2d array of 1s (land) and 0s (water), count the number of islands
the four edges of the array are surrounded by water

ex...

1 0 0
0 1 0
0 0 1  ==> 3 islands
'''

## solution
'''
basic idea is that I start from one point, and explore all areas of that island
after exploring each part of the land, put a flag that says i've explored this area
after recursively doing this, if there are no more land on this island, increment the # of islands by 1

iterate through the map untilL i see a land that I haven't explored yet. repeat the same thing
'''
def numberOfIslandsHelper(point, map):

    return None

def numberOfIslands(map):
    if not map:
        return 0
    rows = len(map)
    cols = len(map[0])
    if rows <= 0 or cols <= 0:
        return 0
    
    exploredLand = set()

    def explore(row, col):
        if (row, col) in exploredLand:
            return
        exploredLand.add((row, col))
        if row-1 >= 0 and map[row-1][col] == 1: 
            explore(row-1, col)
        if row+1 < rows and map[row+1][col] == 1:
            explore(row+1, col)
        if col-1 >= 0 and map[row][col-1] == 1:
            explore(row, col-1)
        if col+1 < cols and map[row][col+1] == 1:
            explore(row,col+1)
    landCount = 0

    for row in range(0,rows):
        for col in range(0,cols):
            if map[row][col] == 1 and (row, col):
                explore(row, col)
                landCount += 1

    return landCount
    

SouthAmerica = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
print 'count is ', numberOfIslands(SouthAmerica)