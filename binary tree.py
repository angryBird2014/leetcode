class BinaryTree:

    def __init__(self,rootObj):
        self.root = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
            t.rightChild = None

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            t.leftChild = None

    def findKTree(self,tree,k):
        que = []
        count = 0
        if tree == None:
           return None
        else:
            que.append(tree)
        while len(que) > 0:

            root = que.pop(0)
            count += 1
            if count == k:
                return root
            if count <= k and root != None:
                if root.getLeftChild != None:
                    que.append(root.getLeftChild())
                if root.getRightChild != None:
                    que.append(root.getRightChild())
            else:
                return None
        return None



    def insertLeftFromKPosition(self,root,position,value):
        tree = self.findKTree(root,position)
        if tree != None:
            node = BinaryTree(value)
            if tree.leftChild == None:
                tree.leftChild = node
            else:
                node.leftChild = tree.leftChild
                tree.leftChild = node
        else:
            return None




    def inssertRightFromKPosition(self,position,root,value):
        tree = self.findKTree(root, position)
        if tree != None:
            node = BinaryTree(value)
            if tree.rightChild == None:
                tree.rightChild = node
            else:
                node.rightChild = tree.rightChild
                tree.rightChild = node
        else:
            return None


    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def getRootVal(self):
        return self.root

    def setRootVal(self,obj):
        self.root = obj

class Solution():
    def buildTree(self,preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        rootValue = preorder[0]
        root = BinaryTree(rootValue)
        rootValueIndex = inorder.index(rootValue)
        root.leftChild = self.buildTree(preorder[1:1 + rootValueIndex], inorder[:rootValueIndex])
        root.rightChild = self.buildTree(preorder[rootValueIndex + 1:], inorder[rootValueIndex + 1:])
        return root




nodelist = []

def preorder(tree):


    if tree:
        nodelist.append(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
    return nodelist


def inorder(tree):

    if tree:
        inorder(tree.getLeftChild())
        nodelist.append(tree.getRootVal())
        inorder(tree.getRightChild())
    return nodelist

def postorder(tree):

    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        nodelist.append(tree.getRootVal())
    return nodelist


def levelTravel(tree):
    que = []

    if tree == None:
        print("null tree")
    else:
        que.append(tree)
    while len(que) > 0 :
        root = que.pop(0)
        if root != None:
            print(root.getRootVal())
            if root.getLeftChild != None:
                que.append(root.getLeftChild())
            if root.getRightChild != None:
                que.append(root.getRightChild())

if __name__ == '__main__':
    '''
    r = BinaryTree('a')
    #print(r.getRootVal())
    #print(r.getLeftChild())
    #print(r.getRightChild())
    r.insertLeft('b')
    #print(r.getRightChild())
    #print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    #print(r.getRightChild().getRootVal())
    r.insertLeft('d')
    #print(r.getLeftChild().getLeftChild().getRootVal())
    r.getLeftChild().setRootVal('hello world')
    #print(r.getLeftChild().getRootVal())
    #print('****',postorder(r))
    print("*************")
    levelTravel(r)
    '''
    ''''
    if r.findKTree(r,5) != None:
        print(r.findKTree(r,5).getRootVal())
    else:
        print("null")
    '''
    '''
    r.insertLeftFromKPosition(r,4,'d')
    print("---")
    levelTravel(r)
    '''
    sol = Solution()
    preorder = [ 'G','D','A','F','E','M','H','Z']
    inorder = ['A','D','E','F','G','H','M','Z']
    root = sol.buildTree(preorder,inorder)
    levelTravel(root)