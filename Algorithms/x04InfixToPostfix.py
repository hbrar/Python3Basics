from x01stack import Stack

def infixToPostfix(inpt):
    # Stack maintains list of low precedence operators all time
    opstack = Stack()
    ops = '(*/+-)'
    # Holds precedence of various operators, 3 being the highest
    prec = {'(':3,')':3,'*':2,'/':2,'+':1,'-':1}
    outpt = []

    for token in inpt:
        if token not in ops:
            # append literal tokens to output
            outpt.append(token)
        else:
            # perform operator push pop decisions
            if opstack.isEmpty():
                opstack.push(token)
            else:
                if token == ')':
                    while opstack.peek() != '(':
                        outpt.append(opstack.pop())
                    opstack.pop()
                else:
                    while not opstack.isEmpty() and prec[opstack.peek()] >= prec[token]:
                        # Placing peek() after 'and' prevents 'index out of range' exception due to short circuiting
                        # Perform POP until you encounter '('
                        if opstack.peek() != '(':
                            outpt.append(opstack.pop())
                        else:
                            break
                    opstack.push(token)
                    
    while not opstack.isEmpty():    
        outpt.append(opstack.pop())
    return ''.join(outpt)
      
print(infixToPostfix("A+B"))
print(infixToPostfix("A * B + C * D"))
print(infixToPostfix('( A + B ) * C - ( D - E ) * ( F + G )'))
