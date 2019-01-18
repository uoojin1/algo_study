from classes import *

'''
        5
    3        8
1     4   6     9
  2         7     10  
'''


class DFS(Tree):
    def __init__(self, root):
        Tree.__init__(self, root)
    def iterDFSpreorder(self):
        path = [] # stack for the path
        visited = set() # memo which have been visited
        path.append(self.root)
        while path:
            node = path.pop()
            if node:
                print node.val
                visited.add(node)
                if node.right and node.right not in visited: # so that we pop left first
                    path.append(node.right)
                if node.left and node.left not in visited:
                    path.append(node.left)
    def iterDFSinorder(self):
        path = [self.root]
        # node = self.root
        while path:
            node = path.pop()
            while node:
                path.append(node)
                node = node.left
            if len(path) > 0:
                curr = path.pop()
                if curr:
                    print curr.val
                    path.append(curr.right)
    def iterDFSpostorder(self): # 2 stacks approach
        '''
        need to use 2 stacks for this
        1. put item in stack 1
        2. pop item from stack 1 and push to stack 2
        3. push pop.left and pop.right to stack 1
        repeat
        '''
        print '\n iter DFS post order!'
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            if node:
                print node.val


myDFSTree = DFS(n5)

# myDFSTree.iterDFSpreorder()
# myDFSTree.iterDFSinorder()
myDFSTree.iterDFSpostorder()