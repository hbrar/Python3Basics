iterable = [4,5,6,7] # here iterable is a list

for element in iterable:
    # do something with element
    print(element)
    
#Is actually implemented as.

# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
        print(element)
    except StopIteration:
        # if StopIteration is raised, break from loop
        break