x = 24
y = 60
def myGcd(dvr, dvd):
    r = dvd % dvr
    if r == 0:
        return dvr
    else:
      return  myGcd(r, dvr)
    
print(myGcd(min(x,y),max(x,y)))

import math

x = 24
y = 60
# def gcd(dvr, dvd):
#     r = dvd % dvr
#     if r == 0:
#         return dvr
#     else:
#       return  gcd(r, dvr)
    
# print(gcd(min(x,y),max(x,y)))
B = [1,2,3,4,6,1000000]
A=  [5,6,7,8,2,99999]
# for i in range(4):
#     for j in range(4): print('[{},{}]'.format(A[i],B[j]))

# [ [pair,gcd())] for pair in [[x,y] for x in A for y in B] ]    


print([(math.gcd(pair[0],pair[1]), pair[0] + pair[1]) for pair in [(x,y) for x in A for y in B]])
print(max([ (math.gcd(pair[0],pair[1]), pair[0] + pair[1]) for pair in [(x,y) for x in A for y in B]])[1])