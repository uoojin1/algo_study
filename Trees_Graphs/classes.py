'''
class definition for Trees and graphs
'''

class Node:
    def __init__(self, value=None):
        self.value = value

class TreeNode(Node):
    def __init__(self, value=None):
        Node.__init__(self, value)
        self.leftNode = None;
        self.rightNode = None;        

class GraphNode(Node):
    def __init__(self, value=None):
        Node.__init__(self, value)
        self.adjacentNodes = []
        self.visited = False
    def printAdjacentNodes(self):
        print ''.join(node.value for node in self.adjacentNodes)

class Tree:
    def __init__(self, root=None):
        self.rootNode = root
    def levelPrintTree(self):
        currentLevel = [self.rootNode]
        while currentLevel:
            print [node.value for node in currentLevel]
            nextLevel = []
            for node in currentLevel:
                if node.leftNode:
                    nextLevel.append(node.leftNode)
                if node.rightNode:
                    nextLevel.append(node.rightNode)
            currentLevel = nextLevel

class Graph:
    def __init__(self, node):
        self.startNode = node
        self.path = ''
    def dfsPrint(self):
        def dfsPrintHelper(node):
            if not node:
                return
            else:
                self.path += ' -> ' + str(node.value)
                node.visited = True;
                for adjNode in node.adjacentNodes:
                    if not adjNode.visited:
                        dfsPrintHelper(adjNode)
        dfsPrintHelper(self.startNode)
        print self.path
                

                



node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7) 

node0.leftNode = node1
node0.rightNode = node2
node1.leftNode = node3
node1.rightNode = node4
node2.leftNode = node5
node2.rightNode = node6
node3.rightNode = node7

# myTree = Tree(node0)
# myTree.levelPrintTree() # print tree

gNode1 = GraphNode(1)
gNode2 = GraphNode(2)
gNode3 = GraphNode(3)
gNode4 = GraphNode(4)
gNode5 = GraphNode(5)
gNode6 = GraphNode(6)
gNode7 = GraphNode(7)
gNode8 = GraphNode(8)
gNode9 = GraphNode(9)

gNode1.adjacentNodes = [gNode2, gNode4]
gNode2.adjacentNodes = [gNode1, gNode5, gNode3]
gNode3.adjacentNodes = [gNode2, gNode6]
gNode4.adjacentNodes = [gNode1, gNode5, gNode7]
gNode5.adjacentNodes = [gNode2, gNode4, gNode6, gNode8]
gNode6.adjacentNodes = [gNode3, gNode5, gNode9]
gNode7.adjacentNodes = [gNode4, gNode8]
gNode8.adjacentNodes = [gNode5, gNode7, gNode9]
gNode9.adjacentNodes = [gNode6, gNode8]

# myGraph = Graph(gNode1)
# myGraph.dfsPrint()



