class Stack2:
    
    def __init__(self):
        self.items = []
        self.length = 0
    
    def push(self,item):
        # self.items.append(item)
        # for a =[1,2,3], python does not allow a[4] = 4...Index out of range Error
        # hence only options are a += [4] or a.append(4)
        # self.items[self.length] = item 
        self.items += [item]
        self.length += 1
        
    def pop(self):
        # return self.items.pop()
        self.length -= 1
        return self.items[self.length]
    
    def peek(self):
        return self.items[self.length - 1]
        
    def __str__(self):
        str_rep = ""
        for i in range(self.length):
            str_rep +=  "|"+str(self.items[self.length-1-i]) +"|"+"\n"
        str_rep += "==="
        return str_rep
        
s = Stack2()
s.push(3)
s.push(7)
s.push(2)
print("peek:"+ str(s.peek()))
print(s)
print("popped:" +str(s.pop()))
print("peek:"+ str(s.peek()))
print(s)
print("popped:" +str(s.pop()))
print("peek:"+ str(s.peek()))
print(s)