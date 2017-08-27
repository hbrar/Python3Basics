def foo(a,*l):
    """packing multiple arguments into one parameter"""
    print(l)
    #print(*l)
    print(type(l))

foo(3,44,5,6,7)
# foo(3,[4,5,7,8])

def bar(a,b,c):
    """Unpacking argument during a function call into different parameters"""
    print(a)
    print(b)
    print(c)
    
p = (3,4,5)

bar(*p)