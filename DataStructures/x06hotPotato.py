from x05queue import Queue

def hotPotato(nameList, num):
    namesQueue = Queue()
    
    for name in nameList:
        namesQueue.enqueue(name)
    
    while namesQueue.size() >1:
        
        for i in range(num):
            #Simulating circle
            namesQueue.enqueue(namesQueue.dequeue())
        
        namesQueue.dequeue()
        
    return namesQueue.dequeue()
    
print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))
