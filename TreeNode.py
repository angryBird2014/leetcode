class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.left = self.left
            self.left = t

    def insertRight(self, newNode):
        if self.right == None:
            self.right = TreeNode(newNode)
        else:
            t = TreeNode(newNode)
            t.right = self.right
            self.right = t
    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.root

    def setRootVal(self,obj):
        self.root = obj

