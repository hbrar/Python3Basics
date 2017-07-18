# The parameter names in the function 
# definition behave like local variable

# When we use the assignment operator (=) inside 
#a function, its default behaviour is to create a new 
# local variable – unless a variable with the 
# same name is already defined in the local scope.

#http://python-textbok.readthedocs.io/en/1.0/Variables_and_Scope.html

# it is usually very bad practice to access global variables from inside 
# functions, and even worse practice to modify them. 

# If a function needs to access some external value, we should pass the value 
# into the function as a parameter. 
# If the function is a method of an object, it is sometimes appropriate to make 
# the value an attribute of the same object

#If we use the global keyword, the assignment statement will create the variable
# in the global scope if it does not exist already
a = 0

def my_function():
    #global b = 6 invalid
    global b
    b = 6
    a = 3
    print('--inside fn--')
    print(a)
    print(globals()['a'])
    print(b)

my_function()
print('--outside fn--')
print(a)
print(b)