'''
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1
d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

       4
     /   \
    2     6
   / \   / 
  3   1 5   
'''

def addOneRow(root, v, d):
    # level order traversal
    currentLevel = [root]
    depth = 1
    while currentLevel:
        nextLevel = []
        for node in currentLevel:
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        currentLevel = nextLevel
        depth += 1
        