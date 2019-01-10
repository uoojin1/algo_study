''' random node from BST

Implement a bst with a method getRandomNode() from scratch
that returns a random node
      4
  2       6
1   3   5   7
'''
# solution1: brute force way
'''
traverse the tree, put every element in an array
do math.random() between 0 ~ array length
time: O(n), space: O(n) // extra array
'''
# actually you don't even need an array, just generate the random number and do a dfs N steps

# solution2: little better. Storing the number of childern at each node
'''
so at the top (4), 4.childeren = 6
2.children = 2
6.children = 2
so by recursion @ 4, current item + left children + right children = 7
1/7 chance, choose 7. 3/7 chance, go left, 3/7 chance, go right (recurse...)
time: O(n), space: O(1)
'''

class Node:
    def __init__(self, val):
        self.val = val;
        self.left = None;
        self.right = None;
        self.children = 0
    
class BST:
    def __init__(self):
        self.root = None;
    def levelOrderPrint(self):
        currentLevel = [self.root]
        while currentLevel:
            print [item.val for item in currentLevel]
            print [item.children for item in currentLevel]
            nextLevel = []
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currentLevel = nextLevel
    def insertNode(self, inputNode):
        def insertNodeHelper(node, inputNode):
            node.children += 1
            if inputNode.val <= node.val:
                if not node.left:
                    node.left = inputNode
                else:
                    insertNodeHelper(node.left, inputNode)
            else:
                if not node.right:
                    node.right = inputNode
                else:
                    insertNodeHelper(node.right, inputNode)
        if not self.root:
            self.root = inputNode
        else:
            insertNodeHelper(self.root, inputNode)
        
myBinarySearchTree = BST()
root = Node(4)
node2 = Node(2)
node6 = Node(6)
node1 = Node(1)
node3 = Node(3)
node5 = Node(5)
node7 = Node(7)

myBinarySearchTree.insertNode(root)
myBinarySearchTree.insertNode(node2)
myBinarySearchTree.insertNode(node6)
myBinarySearchTree.insertNode(node1)
myBinarySearchTree.insertNode(node3)
myBinarySearchTree.insertNode(node5)
myBinarySearchTree.insertNode(node7)

myBinarySearchTree.levelOrderPrint()