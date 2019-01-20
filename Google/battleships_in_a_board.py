''' given a 2d board, count how many battleships are in it

the battleships are represented with 'X', and water is just '.'

- battleships can only be placed horizontally or vertically
- at least one horizontal or vertical cell separates between two battleships
- there are no adjacent battleships

ex)
X...
X...
X..X ==> 2 battle ships

'''
# def sink(board, i, j):
#     if i < 0 or j < 0 or i >= len(board) or j >= len(board) or board[i][j] == '.':
#         return
#     board[i][j] = '.'
#     sink(board, i-1, j)
#     sink(board, i+1, j)
#     sink(board, i, j-1)
#     sink(board, i, j+1)

# def countBattleShips(board):
#     count = 0
#     for i in range(0, len(board)):
#         for j in range(0, len(board[0])):
#             if board[i][j] == 'X':
#                 count += 1
#                 sink(board, i, j)
#     return count
    
''' optimal solution
so basically since we know that the ship is only going to be horizontal or
vertical, if we are iterating from top left, and to the right, we know that
when we land on a 'X' and if the left or the top is a X, this is not the first time
that we are encountering this specific ship. Thus we will just continue on at this
point
'''
def countBattleShips(board):
    count = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == 'X':
                if i-1 >= 0 and board[i-1][j] == 'X':
                    continue
                if j-1 >= 0 and board[i][j-1] == 'X':
                    continue
                count += 1
    return count

board = [
    ['.','X','X'],
    ['X','.','.'],
    ['X','.','X']
]

print countBattleShips(board)