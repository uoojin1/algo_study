'''
Given N x N matrix, write a method that rotates this image by 90 degrees clockwise
'''

'''

N = even case, chunk it in even n/2 by n/2 and rotate+swap these ==> could do it with n/2 n/2 temporary storage or just 1
'''

def rotateMatrix(image, N):
    temp = None
    N_is_odd = N % 2 == 1
    if N == 1:
        return image
    if N_is_odd:
        for row in range(N/2):
            for col in range(N/2+1):
                temp = image[row][col]
                image[row][col] = image[N-1-col][row] 
                image[N-1-col][row] = image[N-1-row][N-1-col]
                image[N-1-row][N-1-col] = image[col][N-1-row]
                image[col][N-1-row] = temp
    else:
        for row in range(N/2):
            for col in range(N/2):
                temp = image[row][col]
                image[row][col] = image[N-1-col][row] 
                image[N-1-col][row] = image[N-1-row][N-1-col]
                image[N-1-row][N-1-col] = image[col][N-1-row]
                image[col][N-1-row] = temp
    return image

image_4_4 = [
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4],
    [1,2,3,4]
]
image_5_5 = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]

print(rotateMatrix(image_5_5, 5))
print(rotateMatrix(image_4_4, 4))