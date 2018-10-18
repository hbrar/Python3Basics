def countAlp(st):
    dictCount = {}
    for c in st:
        if dictCount.get(c) == None:
            dictCount[c] = 1
        else:
            dictCount[c] += 1
    return dictCount

print(countAlp("abcdabfgc"))
        