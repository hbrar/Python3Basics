from x01stack import Stack

def isParBalanced(in_str):
    _isBalanced  = True
    s = Stack()
    for i in in_str:
        if i == '(':
            s.push('(')
        else:
            if s.isEmpty():
                _isBalanced = False
            else:
                s.pop()
    if not s.isEmpty():
        _isBalanced = False
    return _isBalanced
    
print(isParBalanced('(())'))

def isSymbBalanced(in_str):
    symbols = {'(':')', '[':']', '{':'}'}
    _isBalanced  = True
    s = Stack()
    for i in in_str:
        if i in symbols:
            s.push(i)
        else:
            if s.isEmpty():
                _isBalanced = False
            else:
                if symbols[s.peek()] == i:
                    s.pop()
                else:
                    _isBalanced = False
    if not s.isEmpty():
        _isBalanced = False
    return _isBalanced
print(isSymbBalanced('(({[)]}))'))
print(isSymbBalanced('(({[]}))('))