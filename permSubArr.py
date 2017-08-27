C = []

# non distinct
print([C[i:i+j+1] for i in range(len(C)) for j in range(len(C)-i)])
#distinct
print([list(i) for i in list(set([tuple(C[i:i+j+1]) for i in range(len(C)) for j in range(len(C)-i) ]))])
x = 1
y = 2
print(len([pair for pair in [C[i:i+j+1] for i in range(len(C)) for j in range(len(C)-i)] if pair.count(x)== pair.count(y)]))

k = 10000000000
def pandig(a):
  return all([True if a.count(str(i))>0 else False for i in range(10)])
  
def stepnum(a):
  return all([True if int(a[i]) - int(a[i+1]) in (1,-1) else False for i in range(len(a)-1)])

count = 0
for i in range(int(9e9),k):
    print(i)
    if pandig(str(i)):
        if stepnum(str(i)):
            count+=1
            print(i)
    
print(count)

