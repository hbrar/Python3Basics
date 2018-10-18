from OOBinTree import BinaryTree

def buildParseTree(expr):
    tokens = list(expr)
    operators = '+-/*'
    
    tree = BinaryTree('')
    currentNode = tree.getRootVal()
    
    for token in tokens: # O(n)
        if token == '(':
            currentNode.insertLeft('') #create a new left node
            currentNode = currentNode.getLeftChild()    # move to newly created node so that the operand can be inserted
        elif token not in operators and token != ')':
            currentNode.setRootVal(token)
            currentNode = currentNode
            