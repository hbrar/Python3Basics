def toStr(num,base):
    baseStr = '0123456789ABCDEF'
    
    if num < base:
        # Base case
        return baseStr[num]
    else:
        return toStr(num//base,base) + baseStr[num%base]

print(toStr(15,10))
print(type(toStr(15,10)))
print(toStr(15,16))
print(type(toStr(15,16)))
print(toStr(145,16))