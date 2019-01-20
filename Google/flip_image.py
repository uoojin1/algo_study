''' flipping an image

given a binary matrix A, we want to flip the image horizontally
then invert it, and then return the resulting image
'''

def flipAndInvertImage(A):
    for i in range(0, len(A)):
        left = 0
        right = len(A)-1
        # swapping
        while left < right:
            temp = A[i][right]
            A[i][right] = A[i][left]
            A[i][left] = temp
            left += 1
            right -= 1
        # inverting
        for index, value in enumerate(A[i]):
            A[i][index] = 0 if A[i][index] else 1
    return A

Image = [
    [0,0,1],
    [1,1,0],
    [0,0,1]
]

print flipAndInvertImage(Image)