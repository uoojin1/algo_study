'''
check if tree t, is a subtree of s
'''

def isIdentical(self, s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and isIdentical(s.left, t.left) and isIdentical(s.right, t.right)

def isSubtree(self, s, t):
    if not s:
        return False
    if not t:
        return True
    if isIdentical(s,t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)