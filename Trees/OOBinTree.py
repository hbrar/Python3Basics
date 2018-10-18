class Node:
    
    def __init__(self,nodeValue):
        self.value = nodeValue
        self.left = None
        self.right = None
        self.parent = None
        
class BinaryTree:
    
    def __init__(self,rootVal):
        self.root = Node(rootVal)
        
        
    def setLeftChild(self, nodeValue):
        if self.left == None:
            self.left = Node(nodeValue)
            self.left.parent = self
        else:
            t = Node(nodeValue)
            self.left.parent = t
            t.left = self.left
            self.left =  t
            self.left.parent = self
        
    def setRightChild(self,nodeValue):
        if self.right == None:
            self.right = BinaryTree(nodeValue)
            self.right.parent = self
        else:
            t = BinaryTree(nodeValue)
            self.right.parent = t
            t.right = self.right
            self.right = t
            self.right.parent = self
    
    def getLeftChild(self):
        return self.left
        
    def getRightChild(self):
        return self.right
    
    def getValue(self):
        return self.value
        
    def setValue(self,val):
        self.value = val
    
    def getParent(self):
        return self.parent
        
tree = BinaryTree('a')
# print("value:" , tree.getValue())
# print("left:" , tree.getLeftChild())
# print("right:" , tree.getRightChild())


currentLeftNode = tree.getLeftChild()
while  currentLeftNode != None:
    print(currentLeftNode.getValue())
    currentLeftNode = currentLeftNode.getLeftChild()
    
tree.setLeftChild('b')
# print("left:" , tree.getLeftChild().getValue())

currentLeftNode = tree.getLeftChild()
while  currentLeftNode != None:
    print(currentLeftNode.getValue(),"parent:=>",currentLeftNode.getParent().getValue())
    currentLeftNode = currentLeftNode.getLeftChild()
print("-"*10)    
tree.setLeftChild('x')
# print("left:" , tree.getLeftChild().getValue())
# print("left:" , tree.getLeftChild().getLeftChild().getValue())

currentLeftNode = tree.getLeftChild()
while  currentLeftNode != None:
    print(currentLeftNode.getValue(),"parent:=>",currentLeftNode.getParent().getValue())
    currentLeftNode = currentLeftNode.getLeftChild()
print("-"*10)

firstLeftChild = tree.getLeftChild()
firstLeftChild.setLeftChild('y')
# tree.setLeftChild('y')

currentLeftNode = tree.getLeftChild()
while  currentLeftNode != None:
    print(currentLeftNode.getValue(),"parent:=>",currentLeftNode.getParent().getValue())
    currentLeftNode = currentLeftNode.getLeftChild()
print("-"*10)