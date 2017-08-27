# Factory function
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    
p1 = polynomial_creator(2, 3, 4)

#print(p1(1))
    
#decorators    
def dec_print(func):
    def func_wrapper(x):
        print(func(x))
    return func_wrapper

@dec_print    
def square(y):
    return y*y

square(9)