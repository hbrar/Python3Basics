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

# simple & better

def isbalancedNew(st):
    brackets = {'(':')','{':'}','[':']'}
    # opening = '({['
    # closing = ')}]'
    stack = []
    
    for s in st: #O(n)
        # if s in brackets.keys(): #O(3) Avoid this  loop ...complex is O(n) in general but here it's a constant since there are only 3 keys
        if brackets.get(s) != None: #complexity of get() is O(1) little faster
        # if s in opening:
            stack.append(s)
        else:
            if len(stack) != 0 and brackets[stack[len(stack)-1]] == s: # O(1) + O(3) => O(4)
            # if len(stack) != 0 and s in closing: => must be a pair..this wont work
                stack.pop()
            else:
                return False
                
    if len(stack) == 0:
        return True
    else:
        return False
    
print(isbalancedNew('{{((){})[{}]}}'))
print(isbalancedNew('{{}}'))
print(isbalancedNew('}}'))
print(isbalancedNew('(('))

# using dictionary ...more memory efficient

def isbalancedDict(st):
    brackets = {'(':0,'{':0,'[':0,')':0,'}':0,']':0,}
    opening = '({['
    closing = ')}]'
    
    for s in st:# O(n)
        if s in opening: # O(3)
            brackets[s] += 1
        if s in closing: # O(3)
            brackets[s] -= 1
    if brackets['('] +brackets['{'] +brackets['['] +brackets[')'] +brackets['}'] +brackets[']'] == 0:
        return True
    else:
        return False
        
print(isbalancedDict('{{((){})[{}]}}'))
print(isbalancedDict('{{}}'))
print(isbalancedDict('}}'))
print(isbalancedDict('(('))