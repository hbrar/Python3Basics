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