from classes import *

'''
        5
    3        8
1     4   6     9
  2         7     10  
'''

class BFS(Tree):
    def __init__(self, root):
        Tree.__init__(self,root)
    def BFSTraversal(self):
        def BFShelper(node):
            if not node:
                return
            currLevel = [node]
            while currLevel:
                nextLevel = []
                for node in currLevel:
                    print node.val
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
                currLevel = nextLevel
        BFShelper(self.root)
myBFSTree = BFS(n5)

myBFSTree.BFSTraversal()