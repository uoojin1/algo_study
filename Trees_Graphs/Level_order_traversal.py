# binary tree node definition

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        answer = []
        currLevel = [root]

        while currLevel:
            answer.append([node.val for node in currLevel])
            nextLevel = []
            for node in currLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            currLevel = nextLevel;
        return answer;
