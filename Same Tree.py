# Definition for a binary tree node.
class TreeNode(object):
        def __init__(self, x):
             self.val = x
             self.left = None
             self.right = None

        def insertLeft(self,newNode):
            if self.left == None:
                self.left = TreeNode(newNode)
            else:
                t = TreeNode(newNode)
                t.left = self.left
                self.left = t

        def insertRight(self,newNode):
            if self.right == None:
                self.right = TreeNode(newNode)
            else:
                t = TreeNode(newNode)
                t.right = self.right
                self.right = t

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if q== None and p == None:
            return True
        if q == None and p != None:
            return False
        if q != None and p == None:
            return False
        if q != None and p != None:
            if q.val == p.val:
                left = self.isSameTree(p.left, q.left)
                rigth = self.isSameTree(p.right, q.right)
                return left and rigth
            else:
                return False


if __name__ == '__main__':
    sol = Solution()
    p = TreeNode(2)
    q = TreeNode(1)
    p.insertLeft(1)
    q.insertRight(2)
    print(sol.isSameTree(p,q))



