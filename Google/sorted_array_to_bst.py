class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
    def inOrderTraverse(self):
        node = self.root
        def helper(node):
            if not node:
                return
            helper(node.left)
            print node.val
            helper(node.right)
        helper(node)
    def BFS(self):
        currLvl = [self.root]
        while currLvl:
            print '\n', [node.val for node in currLvl]
            nextLvl = []
            for node in currLvl:
                if node.left:
                    nextLvl.append(node.left)
                if node.right:
                    nextLvl.append(node.right)
            currLvl = nextLvl
        

# [0,1,2,3,4]
''' example
length = 5
length / 2 = 2

# [0,1,2,3,4,5]
length = 6
length / 2 = 3
'''

def sortedArrayToBST(numberList):
    if not numberList:
        return None
    if len(numberList) == 1:
        return Node(numberList[0])
    node = Node(numberList[len(numberList)/2])
    node.left = sortedArrayToBST(numberList[:len(numberList)/2])
    node.right = sortedArrayToBST(numberList[len(numberList)/2+1:])
    return node

root = sortedArrayToBST([1,2,3,4,5,6,7,8,9,10])

myTree = Tree(root)

# print myTree.root.val
print myTree.inOrderTraverse()
myTree.BFS()