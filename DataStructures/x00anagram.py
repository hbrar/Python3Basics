# References: https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/AnAnagramDetectionExample.html#solution-4-count-and-compare
# https://docs.python.org/3/library/functions.html#ord

# Assumptions:
    # All characters are 26 lowecase alphabetic charaters
    # Both strings are of equal length
    # Function should return boolean value

def isAnagram(in1,in2):
    """ this function has complexity of O(n2)"""
    _isAnagram = True
    
    for i in range(0,len(in1)):
        _found = False
        
        for j in range(0,len(in2)):
            if in1[i] == in2[j]:
                _found = True
                
        if _found == False:
            _isAnagram = False
            
    return _isAnagram

print(isAnagram('abcd','bcda'))
print(isAnagram('fds','dfc'))
###################################################
#################Using built in 'IN' ###########
###################################################
# def isAnagram(in1,in2):
#     _isAnagram = True
#     for i in in1:
#         if i not in in2:
#             _isAnagram = False
#     return _isAnagram
    


###################################################
#################Using built in sort()###########
###################################################

def isAnagramSort(in1, in2):
    # strings are immutable in Python
    in1 = list(in1)
    in2 = list(in2)
    in1.sort()
    in2.sort()
    _isAnagram = True
    for i in range(0, len(in1)):
        if in1[i] != in2[i]:
            _isAnagram = False
            break
    return _isAnagram

print(isAnagramSort('abcd','bcda'))
print(isAnagramSort('fds','dfc'))

###################################################
#################Using count and compare###########
###################################################

# ord() could also be used instead of dictionary

def isAnagramCC(in1, in2):
    """ this function has complexity of O(n)"""
    
    _isAnagram = True
    alphabetsDict = {'a': 0, 'b':1, 'c':2, 'd': 3, 'e': 4 , 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15,
    'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25 }
    count_in1 = [0]*26
    count_in2 = [0]*26
    
    for i in range(0, len(in1)):
        count_in1[alphabetsDict[in1[i]]] += 1
        
    for i in range(0, len(in1)):
        count_in2[alphabetsDict[in2[i]]] += 1
        
    #print(count_in1)
    #print(count_in2)
    for i in  range(0,26):
        if count_in1[i] != count_in2[i]:
            _isAnagram = False
            break
    return _isAnagram
 
# simple & better
def isAnagramNew(str1, str2):
    if len(str1) != len(str2):
        return False
        
    for i in range(len(str1)):
        if str1[i] == str2[len(str2)-1-i]:
            continue
        else:
            return False
    return True

    #One liner
    #  "".join(sorted(list("abc"))) == "".join(sorted(list("cba")))
print(isAnagramCC('abcd','bcda'))
print(isAnagramCC('fds','dfc'))
    