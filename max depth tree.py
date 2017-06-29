from TreeNode import TreeNode
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            return max([self.maxDepth(root.left),self.maxDepth(root.right)])+1

if __name__ == '__main__':
    sol = Solution()
    p = TreeNode(2)

    p.insertLeft(1)
    p.insertRight(9)
    p.insertRight(3)
    print(sol.maxDepth(p))

