class Node:
    
    def __init__(self,initdata):
        self.__data = initdata 
        self.__next = None # private to prevent access by List instance...e.g  mylist.head.next.next.data
    
    def setData(self,data):
        self.__data = data
        
    def getData(self):
        return self.__data
        
    def setNext(self,__next):
        self.__next =  __next
    
    def getNext(self):
        return self.__next
        
class UnorderedList:
    
    def __init__(self):
        self.__head = None
        self.__size = 0
    
    def __getitem__(self, inx):
        #square brackets are python's way of saying "call the __getitem__ (or __setitem__) method.
        #x = a[...]  #call a.__getitem__(...)
        #a[...] = x  #call a.__setitem__(...)
        if inx >= self.__size:
            raise IndexError("Index Out of Range")
        return self.at(inx)
    
    #def __setitem__(self,item):
        
    def __str__(self):
        
        __mylist = '['
        
        for i in range(self.__size):
            
            if i != self.__size - 1:
                # not the last element
                __mylist =   __mylist + str(self.at(i)) + ', '
            else:
                #last element
                __mylist =   __mylist + str(self.at(i))
        
        __mylist += ']'    
        
        return __mylist
        
    def toString(self):
        """created same as above but with different  name for unittest"""
        
        __mylist = '['
        
        for i in range(self.__size):
            
            if i != self.__size - 1:
                # not the last element
                __mylist =   __mylist + str(self.at(i)) + ', '
            else:
                #last element
                __mylist =   __mylist + str(self.at(i))
        
        __mylist += ']'    
        
        return __mylist
        
    def append(self, item):
        "Adds item to the end of the list"
        tempNode = Node(item)
        tempNode.setNext(self.__head) 
        self.__head = tempNode
        self.__size += 1
        
    def size(self):
        return self.__size
    
    def remove(self, item):
        """
            1. Removes last occurence of the item
            2. Updates Size
        """
        current = self.__head
        previous = self.__head
        size = self.__size # faster than using self.size()
        for i in range(size):
            if current.getData() == item:
                if i == 0:
                    self.__head = current.getNext()
                else:
                    previous.setNext(current.getNext())
                self.__size -= 1
                break
            current =  current.getNext()
            if i != 0:
                previous =  previous.getNext()
                
    def insert(self, inx, item = -1):
        
        if item == -1:
            raise TypeError("insert() takes exactly 2 arguments (1 given)")
         
        # Note that self.__head refers to the last element of the list and not the first    
        inx = self.__size - inx - 1
        
        # Create a new node
        newNode  = Node(item)
        
        if self.__size == 0:
            #list is empty
            self.__head = newNode
            
        elif inx == -1:
            # Insert at end of list
            newNode.setNext(self.__head)
            self.__head = newNode
        
        elif inx < self.__size:
            # insert in the middle or beginning
            current = self.__head
            currInx = 0
            
            # search for index where to insert new node
            while currInx != inx:
                current = current.getNext()
                currInx += 1
                
            newNode.setNext(current.getNext())
            current.setNext(newNode)
            
        else:
            raise IndexError("Index out of Range")
            
        self.__size += 1
        
    def search(self,item):
        current = self.__head
        isFound = False
        size = self.__size # faster than using self.size()
        
        for i in range(size):
            if current.getData() == item:
                isFound = True
                break
            current =  current.getNext()
        return isFound
        
    def isEmpty(self):
        return self.__head == None
        
    def at(self,lookupIndex):
     
        lookupIndex = self.__size - lookupIndex - 1
        current = self.__head
        i = 0
        
        """
        # Implementing without using __size property
        if lookupIndex >= self.__size:
            raise IndexError("Index out of Range")
        """
        while current.getNext() != None:
            if i == lookupIndex:
                break
            current =  current.getNext()
            i += 1
            
        if i == lookupIndex:
            return current.getData()
        else:
            return "Index out of Range"
       
        
# mylist = UnorderedList()
# print(mylist)
# mylist.append(23)
# print(mylist)
# mylist.append(45)
# print(mylist)
# mylist.append(89)
# print(mylist)

# #print(mylist.head.next.next.data)
# print("at() function from 0 to 4")
# print(mylist.at(0))
# print(mylist.at(1))
# print(mylist.at(2))
# print(mylist.at(3))
# print(mylist.at(4))

# print('removing and searching..')

# mylist.remove(23)
# print(mylist.search(23))
# print(mylist.size())

# print('search()..')

# print(mylist.search(45))
# print(mylist.search(5))
# print(mylist.search(23))
# print(mylist.search(-4))
# print(mylist.search(89))

# print('using square bracket syntax...')
# print(mylist[0])

# print('remove()and search()..')
# mylist.remove(45)
# print(mylist.search(45))
# print(mylist.size())
# mylist.remove(89)
# print(mylist.search(89))
# print(mylist.size())

# mylist.insert(0,22)
# mylist.insert(mylist.size(),44)
# mylist.insert(mylist.size(),55)
# mylist.insert(1,33)
# mylist.insert(0,11)
# mylist.insert(5,66)

# print(mylist.size())
# print(mylist)