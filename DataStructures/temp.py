class BinaryTree:
    
    def __init__(self,rootObj):
        self.root = rootObj
        self.left = None
        self.right = None
        
    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left =  t
    
    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t
    
    def getLeftChild(self):
        return self.left
        
    def getRightChild(self):
        return self.right
    
    def getRootVal(self):
        return self.root
        
    def setRootVal(self,val):
        self.root = val
        
tree = BinaryTree('a')
print("root:" , tree.getRootVal())
print("left:" , tree.getLeftChild())
print("right:" , tree.getRightChild())

tree.insertLeft('b')
print("left:" , tree.getLeftChild().getRootVal())

tree.insertLeft('x')
print("left:" , tree.getLeftChild().getRootVal())
print("left:" , tree.getLeftChild().getLeftChild().getRootVal())


    