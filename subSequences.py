inpt = 'hackerrank'

def subsequences(inpt):
    """A subsequence is a sequence that can be derived from
    another sequence by deleting some elements without changing the order of the remaining elements."""
    inptsize = len(inpt)
    #x = 1
    #y = 1
    for i in range(1,pow(2,inptsize)):
        # Generating all binaries equal to total no. of possible combinations in 'filtr'
        # print(y)
        # y = x<<i | y
        result = []
        filtr = "{:0{size}}".format(int(bin(i)[2:]),size = inptsize ) 
        for j in range(0, inptsize):
            
            # using 'filtr', filter the actual input e.g. for input of size 3, fitr = 010, inpt = 'abc', filtered will be '0b0'
            filtered = str(int(filtr[j]) and inpt[j])
            
            #changing '0b0' to 'b'
            if filtered == '0':
                result.append('')
            else:
                result.append(filtered)
        print(''.join(result))
        
#print(subsequences(inpt))
subsequences(inpt)