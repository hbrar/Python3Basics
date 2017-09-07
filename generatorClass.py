# https://www.programiz.com/python-programming/iterator
# https://www.oreilly.com/ideas/2-great-benefits-of-python-generators-and-how-they-changed-me-forever
# http://intermediatepythonista.com/python-generators

# A Generator is just a function with a yield in it which returns a generator object/iterator

# Actual generator

def num_gen():
    max = 4
    out = 0
    while out < 4:
        yield out
        out += 1
        
nums = num_gen()

# using FOR loop
# FOR loop internally calls next()

for num in nums:
    print(num)
    
# using next() function of generator object

# since generators exhaust themselves once used so creating a new one

nums = num_gen()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums,'To avoid exception, you can send a customized msg'))

# Using an iterator class in case yield is not available
# Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

class Num_gen:
    
    def __init__(self):
        self.max = 4
        self.current = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        next_val =  self.current
        self.current += 1
        if next_val >= self.max:
            raise StopIteration
        return next_val
            
nums =  Num_gen()

print('#'*20,'using iterator class and a for loop', '#'*20)

for num in nums:
    print(num)

print('#'*20,'using iterator class & next', '#'*20)

num =  Num_gen() # iter() is called during  initialisation
print(type(iter(num)))

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num,'cust msg'))

# Num_gen is a customized range() function in essence
# let's modify it

class CustRange:
    
    def __init__(self,max):
        self.max = max
        self.current = 0
        
    def __iter__(self):
        return self
        
    def __next__(self):
        next_val =  self.current
        if next_val >= self.max:
            raise StopIteration
        self.current += 1
        return next_val
        
print('#'*20,'CustomizedRange function', '#'*20)

for i in CustRange(10):
    print(i)
        
        