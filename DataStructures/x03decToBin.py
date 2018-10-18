from x01stack import Stack

def decToBinary(num):
    s = Stack()
    output = ''
    while num > 0:
        s.push(num % 2)
        num //= 2
        
    while not s.isEmpty():
        output += str(s.pop())
    
    return output
    
print(decToBinary(7))

def decToBase(num,base):
    s = Stack()
    output = ''
    digits = '0123456789ABCDEF'
    
    while num > 0:
        s.push(num % base)
        num //= base
        
    while not s.isEmpty():
        output += str(digits[s.pop()])
    
    return output
    
print(decToBase(27,16))

# NEW
def DecToBin(num):
    stack = []
    while num > 0:
        stack.append(num%2)
        num //= 2 # augmented assignment is faster
    
    bin=""
    while len(stack) > 0:
        bin += str(stack.pop())
        
    return bin
    
print(DecToBin(4))
print(DecToBin(8))
print(DecToBin(15))


def decToBaseN(num,base):
    digits = '0123456789ABCDEF'
    stack = []
    while num > 0:
        stack.append(num%base)
        num //= base # augmented assignment is faster
    
    bin=""
    while len(stack) > 0:
        bin += str(digits[stack.pop()])
        
    return bin
    
print(decToBaseN(4,2))
print(decToBaseN(8,8))
print(decToBaseN(15,16))