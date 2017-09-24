from x07deque import Deque

def isPalindrome(inpt):
    isPalin = True
    inptDeque = Deque()
    
    for i in inpt:
        inptDeque.addRear(i)
    
    while not inptDeque.isEmpty or inptDeque.size() > 1:
        if inptDeque.removeFront() != inptDeque.removeRear():
            isPalin = False
            break
    return isPalin
    
print(isPalindrome("lsdkjfskf"))
print(isPalindrome("radar"))
print(isPalindrome("raar"))



