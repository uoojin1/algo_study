''' Binary Search Tree

BST is a tree like structure, where left child is less than the center node
and the right child is greater than the center node.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def printLevelOrder(self):
        if not self.root:
            print 'nothing is in the tree :('
        else:
            currentLevel = [self.root]
            while currentLevel:
                print [item.val for item in currentLevel]
                nextLevel = []
                for node in currentLevel:
                    if node.left:
                        nextLevel.append(node.left)
                    if node.right:
                        nextLevel.append(node.right)
                currentLevel = nextLevel
    def insert(self, item):
        def insertHelper(node, item):
            if item.val <= node.val:
                if node.left:
                    insertHelper(node.left, item)
                else:
                    node.left = item
            else:
                if node.right:
                    insertHelper(node.right, item)
                else:
                    node.right = item
        if not self.root:
            self.root = item
        else:
            insertHelper(self.root, item)
    def remove(self, item):
        def removeHelper(node, item):
            if item.val == node.val: # remove this item
                
            elif item.val <= node.val:
                if node.left:
                    removeHelper(node.left, item)
            elif:
                if node.right:
                    removeHelper(node.right, item)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
myBST = BinarySearchTree()
myBST.insert(node2)
myBST.insert(node1)
myBST.insert(node3)
        
myBST.printLevelOrder()            
        