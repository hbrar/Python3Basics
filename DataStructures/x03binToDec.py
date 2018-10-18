def baseNtoDec(numstr,base):
    numstr = numstr.upper()
    # digits = '0123456789ABCDEF'
    digitsdict = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
    stack = []
    for d in numstr:
        stack.append(d)
    res = 0
    i = 0
    while len(stack) > 0:
        # res += int(digits.index(stack.pop())) * (base**i) #index() => O(n) 
        res += int(digitsdict.get(stack.pop())) * (base**i) #get() => O(1)
        i += 1
    return res
    
print(baseNtoDec('10',8))
print(baseNtoDec('ff',16))
print(baseNtoDec('100',2))
print(baseNtoDec('111',2))