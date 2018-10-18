import datetime
import time

class CustDict:
    # datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)¶
    
    # timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    # Only days, seconds and microseconds are stored internally. Arguments are converted to those units:

    # A millisecond is converted to 1000 microseconds.
    # A minute is converted to 60 seconds.
    # An hour is converted to 3600 seconds.
    # A week is converted to 7 days.
    
    def __init__(self):
        self.d = {}
        
    def custget(self, key):
        
        datastack = self.d.get(key) #[(val1,expiry1),(val2,expiry2)]
        
        if datastack is None:
            return None
        else:
            return self.validdata(key, datastack)
            
           
    def validdata(self, key, datastack):
        
        while True and len(datastack) > 0:
            top = datastack[-1] # top = (val1,expiry1)
            
            if top == None:
                return None
            elif datetime.datetime.now() < top[1]:
                self.d[key] = datastack
                return top[0]
            else:
                datastack.pop()
            
        return None
        
        
    
    def custset(self,key, val, duration):
        if self.d.get(key) is None:
            self.d[key] = [(val, datetime.datetime.now() + datetime.timedelta(milliseconds = duration))]
        else:
            self.d[key].append((val,datetime.datetime.now() + datetime.timedelta(milliseconds = duration)))

myD = CustDict()

print(myD.custget(1))
myD.custset(1,25,8000)  #FOR KEY =  1 @12:00 [(25,12:08)]
print(myD.custget(1))   # @12:00 RETURNS 25
myD.custset(1,50,3000)  #FOR KEY =  1 @12:00 [(25,12:08),(50,12:03)]
time.sleep(1)           # @12:01 
print(myD.custget(1))   # @12:01 RETURNS 50
time.sleep(4)           # @12:05
print(myD.custget(1))   # @12:05 RETURNS 25
time.sleep(4)           # @12:09
print(myD.custget(1))   # @12:09 RETURNS None
