# Modify toStr(num,base) to use stack instead of Recursion

#Importing files from different folder
import sys
sys.path.append('../')

from DataStructures.x01stack import Stack

def toStr(num,base):
    baseStr = '0123456789ABCDEF'
    s = Stack()
    reslt = ''
    
    while num > 0:
        if num < base:
            s.push(baseStr[num])
        else:
            s.push(baseStr[num%base])
        num = num//base
    
    while not s.isEmpty():
        reslt += s.pop()
        
    return reslt
    
print(toStr(15,10))
print(type(toStr(15,10)))
print(toStr(15,16))
print(type(toStr(15,16)))
print(toStr(145,16))
