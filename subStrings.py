inpt = 'harman'

def substrs(inpt):
    """prints all possible substrings"""
    in_copy = inpt[:]
    print(in_copy)
    return {in_copy[i:j] for i in range(0,len(in_copy)) for j in range(i,len(in_copy)+1) if in_copy[i:j] != ''}
    
print(substrs(inpt))
