# All recursive algorithms must obey three important laws:
            
#       1.      A recursive algorithm must have a base case.
#       2.      A recursive algorithm must change its state and move toward the base case.
#       3.      A recursive algorithm must call itself, recursively.
    
def listsum(numlist):
    if numlist != []:
        return numlist[0] + listsum(numlist[1:]) 
    else:
        return 0

print(listsum([1,2,3,4,5]))