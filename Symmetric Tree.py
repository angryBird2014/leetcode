from TreeNode import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isSymmetrucLeftRight(root.left,root.right)

    def isSymmetrucLeftRight(self,left,right):
        if left == None and right == None:
            return True
        if (left != None and right == None) or (left == None and right != None) or (left != None and right != None and left.value != right.value):
            return False
        return  self.isSymmetrucLeftRight(left.left,right.right) and self.isSymmetrucLeftRight(left.right,right.left)


if __name__ == '__main__':
    sol = Solution()
    p = TreeNode(1)
    p.insertRight(2)
    print(sol.isSymmetric(p))