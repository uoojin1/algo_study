class Tree:
    def __init__(self, root):
        self.root = root
    def preOrderTraversal(self):
        print '\npreOrderTraversal!'
        def preOrderHelper(node):
            if not node:
                return
            print node.val
            preOrderHelper(node.left)
            preOrderHelper(node.right)
        preOrderHelper(self.root)
    def inOrderTraversal(self):
        print '\ninOrderTraversal!'
        def inOrderHelper(node):
            if not node:
                return
            inOrderHelper(node.left)
            print node.val
            inOrderHelper(node.right)
        inOrderHelper(self.root)
    def postOrderTraversal(self):
        print '\npostOrderTraversal!'
        def postOrderHelper(node):
            if not node:
                return
            postOrderHelper(node.left)
            postOrderHelper(node.right)
            print node.val
        postOrderHelper(self.root)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

'''
        5
    3        8
1     4   6     9
  2         7     10  
'''

n5.left = n3
n5.right = n8
n3.left = n1
n3.right = n4
n1.right = n2
n8.left = n6
n8.right = n9
n6.right = n7
n9.right = n10

myTree = Tree(n5)

# myTree.preOrderTraversal()
# myTree.inOrderTraversal()
# myTree.postOrderTraversal()