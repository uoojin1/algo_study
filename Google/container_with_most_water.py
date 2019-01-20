''' container with most water

given n non-negative integers, a1,a2....,an (these form vertical lines on a graph)
find two lines which together with x-axis forms a container, such that the container
contains the most water
'''

''' my solution

area = width * height
-- so i'm aiming to have the most width and the most height possible for the
-- largest area

a brute force approach would be just doing a double for loop, and calculating
the area each time. This would work but it would take O(n^2), so it is not very
time efficient
'''

def maxArea(heights):
    maxArea = 0
    for i in range(0, len(heights)):
        for j in range(i+1, len(heights)):
            minHeight = min(heights[i], heights[j])
            maxArea = max(minHeight*(j-i), maxArea)
    return maxArea

# print maxArea([3,0,2,3,1,6,2])

''' O(n) solution
basically, the maximum width is when i = 0 and j = len(heights)-1
so if there is an area greater than this, then the height must be greater
than the min(hegihts[i], heights[j]), b/c the width decreases everytime we move
to the center. Thus we increment the one which ever is lower.
'''
def optimizedMaxArea(heights):
    maxArea = 0
    i = 0
    j = len(heights) - 1
    while i < j:
        maxArea = max((j-i)*min(heights[i],heights[j]), maxArea)
        print '\nmaxArea: ', maxArea
        print 'i, j: ', i,j
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    return maxArea

print optimizedMaxArea([3,0,2,3,1,6,2,7,3,2,5,1,7,8,12,4,2,6,5,8,2,1,3])