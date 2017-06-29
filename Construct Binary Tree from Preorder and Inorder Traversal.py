from TreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        rootValue = preorder[0]
        root = TreeNode(rootValue)
        rootValueIndex = inorder.index(rootValue)
        root.left = self.buildTree(preorder[1:1+rootValueIndex],inorder[:rootValueIndex])
        root.right = self.buildTree(preorder[rootValueIndex+1:],inorder[rootValueIndex+1:])
        return root
if __name__ == '__main__':

    sol = Solution()
    p = TreeNode(2)
    q = TreeNode(1)
    p.insertLeft(1)
    q.insertRight(2)
    print(sol.isSameTree(p,q))

