''' FLOOD FILL!
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
'''

'''
Input: 
image = [
    [1,1,1],
    [1,1,0],
    [1,0,1]
    ]
sr = 1, sc = 1, newColor = 2

Output: [[2,2,2],[2,2,0],[2,0,1]]
'''
def floodFill(self, image, sr, sc, newColor):
    def floodFillHelper(image, sr, sc, newColor):
        image[sr][sc] = newColor
        if image[sr-1][sc]: # top need to add index checks as well, and need to add visited
            floodFillHelper(image, sr-1, sc, newColor)
        if image[sr+1][sc]: # bottom
            floodFillHelper(image, sr+1, sc, newColor)
        if image[sr][sc-1]: # left
            floodFillHelper(image, sr, sc-1, newColor)
        if image[sr][sc+1]: # right
            floodFillHelper(image, sr, sc+1, newColor)
        