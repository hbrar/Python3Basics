

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper
    
@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib = memoize(fib)

print(fib(5))

# using a class decorator for memoization

class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
        
    def __call__(self, *args):
        if args not in self.memo:
	        self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fibnew(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibnew(n-1) + fibnew(n-2)
        
print(fibnew(5))