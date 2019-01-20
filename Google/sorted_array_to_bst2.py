''' given a list of sorted numbers, convert it to bst
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root
    def levelOrderPrint(self):
        current = [self.root]
        while current:
            print [node.val for node in current]
            nextLvl = []
            for node in current:
                if node.left:
                    nextLvl.append(node.left)
                if node.right:
                    nextLvl.append(node.right)
            current = nextLvl
    def dfsInorderPrint(self):
        root = self.root
        def helper(node):
            if not node:
                return
            helper(node.left)
            print node.val
            helper(node.right)
        helper(root)

# [1, 2, 3, 4, 5]
def sortedArray2BST(numbers):
    if not numbers:
        return
    node = Node(numbers[len(numbers)/2])
    node.left = sortedArray2BST(numbers[:len(numbers)/2])
    node.right = sortedArray2BST(numbers[len(numbers)/2+1:])
    return node

myTree = Tree(sortedArray2BST([1,2,3,4,5,6,7,8,9]))

myTree.levelOrderPrint()
myTree.dfsInorderPrint()