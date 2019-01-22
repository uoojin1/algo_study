''' sum of left leaves

find the sum of all left leaves in a given binary tree
left leaf == no children, curr = left child of parent
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
        currLevel = [self.root]
        while currLevel:
            print [node.val for node in currLevel]
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel
    def sumOfLeftChilds(self):
        print 'sum of left childs'
        node = self.root
        sumOfLefts = 0
        def helper(node, parent):
            if not node:
                return 0
            if not node.left and not node.right and (parent and parent.left.val == node.val):
                return node.val
            return helper(node.left, node) + helper(node.right, node)
        return helper(node, None)
        # return sumOfLefts

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5
n5.left = n6

myTree = Tree(n1)

myTree.levelOrderPrint()
print myTree.sumOfLeftChilds()