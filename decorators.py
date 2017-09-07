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

#third party functions can't be decorated using @ sign

from math import sin, cos

def our_decorator(func):
    def function_wrapper(*args, **kwargs):
        """Generalized function wrapper"""
        print("Before calling " + func.__name__)
        res = func(*args, **kwargs)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper
sin = our_decorator(sin)
cos = our_decorator(cos)

#Decorators with Parameters

def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("ÎºÎ±Î»Î·Î¼ÎµÏÎ±")
def foo(x):
    print(42)

foo("Hi")

# if @ symbol can't be used

def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


def foo2(x):
    print(42)

greeting2 = greeting("ÎºÎ±Î»Î·Î¼ÎµÏÎ±")
foo2 = greeting2(foo2)
# above 2 statements can be combined: foo2 = greeting("ÎºÎ±Î»Î·Î¼ÎµÏÎ±")(foo2)
foo2("Hi")

# The way we have defined decorators so far hasn't taken into account that the attributes
# __name__ (name of the function),
# __doc__ (the docstring) and
# __module__ (The module in which the function is defined)
# of the original functions will be lost after the decoration. 

# They can be saved as below

def greeting3(func):
    def function_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper
# Fortunately, we don't have to add all this code to our decorators 
# to have these results. We can import the decorator "wraps" from 
#functools instead and decorate our function in the decorator with it:

from functools import wraps

def greeting4(func):
    @wraps(func)
    def function_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper
    
# Classes instead of Functions
# The __call__ method
# The __call__ method is called, if the instance is 
# called "like a function", i.e. using brackets.

class demo:
    def __init__(self):
        print('instance initialised')
        
    def __call__(self, *args, **kwargs):
        print('args are:', args, kwargs)

d = demo()
d(3,4,t=6,l=2)

# to create a decorator, 
# 1. you pass reference to original function
# 2. you return modified function

# function as a decorator

def dec(func): # passing reference of origianal
    def func_wrapper(*args):
        print('i am a decorator')
        func(*args)
        
    return func_wrapper # returning modified function

@dec
def fooby(*args):
    print('I am fooby')
    print('Fooby args are:', args)

fooby(4,5)

# class as a decorator

class Dec2:
    
    def __init__(self, func): # passing reference to original
        self.func = func
    
    def __call__(self, *args): #same a func_wrapper above
        print('i am a decorator')
        self.func(*args)
        # here nothing is returned as wrapper/decorated function is executed by __call__
        
@Dec2
def fooby2(*args):
    print('I am fooby2')
    print('Fooby2 args are:', args)

fooby2(6,7)        
        
# instead of using @ symbol, below code can be used

def fooby3(*args):
    print('I am fooby3')
    print('Fooby3 args are:', args)
    
fooby3 = Dec2(fooby3)
fooby3(8,9)