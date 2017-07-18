#//////////////////////////////////////////////#
# --------------- VARIABLES -------------------#
#//////////////////////////////////////////////#

 # Mutable and Immutable Types

    # Some values in python can be modiﬁed, and some cannot. This does not ever mean that we can’t change the value of a variable but if a variable contains a value of an immutable type,we can only assign it a new value (using the assignment operator). We cannot alter the existing value in any way.
 
    # Integers, ﬂoating-point numbers, strings, Ranges and Tuples are all immutable types 

    # Lists and dictionaries are mutable, and so are most object

# Type Converison: implicit and explicit
    
    #Implicit  : Integert to Float as there is no loss of precision
            
        # Boolean Expr: 
            # non-zero numbers are True values and zero is False
                # if(3): evaluates to True
            # the empty string is treated as False, but any other string is True – even "0" and "False"!
            # Remember that all non-zero numbers and all non-empty strings are True and zero and the empty string ("") are False. Other built-in data types that can be considered to be “empty” or “not empty” follow the same pattern.
            # None is False.

    #Explicit  : sometimes also called casting

        # Float to Integer (It always rounds down the float): int(6.7)
            # Note that although int can convert a ﬂoat to an integer it can’t convert a string containing a ﬂoat to an integer directly!


        # To and From Strings
            #  If we pass a single number (or any other value) to the print function, it will be converted to a string automatically – but if we try to add a number and a string, we will get an error

            # To convert numbers to strings, we can use string formatting

            # If we want to convert a single number to a string, we can also use the str function explicitly

# Value vs identity
    # When comparing variables using ==, we are doing a value comparison
    # In contrast to this, we might want to know if two objects such as lists, dictionaries or custom objects that we have created ourselves are the exact same object. This is a test of identity.
    # Two objects might have identical contents, but be two different objects. We compare identity with the IS operator
    # It is generally the case (with some caveats) that if two variables are the same object, they are also equal. The reverse is not true – two variables could be equal in value, but not the same object.
    # In many cases, variables of built-in immutable types which have the same value will also be identical. In some cases this is because the Python interpreter saves memory (and comparison time) by representing multiple values which are equal by the same object.
    # a = 9; b = 9; a IS b #True

# The None Value

    #In Python, None is a special value which means “nothing”. Its type is called NoneType, and only one None value exists at a time – all the None values we use are actually the same object

# The conditional operator
    # Syntax: true expression if condition else false expression

    # r = "True" if (4 < 3) else "False"
    # print(r) # False

    # print("True" if (4 < 3) else "False") # False

#//////////////////////////////////////////////#
# --------------- COLLECTIONS -----------------#
#//////////////////////////////////////////////#

# LISTS

    # a = [1,2,3]
    # a[:]
    # a.append(4)
    # a[0:3]
    # a[::2]
    # a[-1:]
    # a[-2:]
    # del a[0]
    # range(0,10)
    # range(2,10,2) # even numbers
    # 6 in range(2,10,2) # True

    # animals = ['cat', 'dog', 'goldfish', 'canary'] 
    # pets = animals # now both variables refer to the same list object
    # animals.append('aardvark') 
    # print(pets) # pets is still the same list as animals
    # animals = ['rat', 'gerbil', 'hamster'] 
    # # now we assign a new list value to animals 
    # print(pets) # pets still refers to the old list
    # pets = animals[:] # assign a *copy* of animals to pets 
    # animals.append('aardvark') 
    # print(pets) # pets remains unchanged, because it refers to a copy, not the original list

    # List methods and functions
        # built-in functions which we can use on lists and other sequences
            # len(a)
            # sum(a)
            # sum(range(2,11,2)) # sum of even numbers till 10
            # any(a) # True is any value in a sequence is True i.e Non-Zero/Non-empty string, not None
            # any([None,"",0]) # Returns False
            # all(a) # Returns TRue is all are True in a sequence

        # List object Methods
            # a.append(3)
            # a.count() #counts how many times a value appears in a list
            # append several values at once to the end 
            # numbers.extend([56, 2, 12] 
            # if the value appears more than once, we will get the index of the first one 
            # numbers.index(2)
            # numbers.index(2,-1) # gets index of first occurence from end of the list
            # numbers.insert(0, 45) # insert 45 at the beginning of the list
            # # remove an element by its index and assign it to a variable 
            # my_number = numbers.pop(0)
            # remove an element by its value 
            # numbers.remove(12) 
            # # if the value appears more than once, only the first one will be removed 
            # numbers.remove(5)

            ## these return a modified copy, which we can print 
            # print(sorted(numbers)) 
            # print(list(reversed(numbers))))
            # the original list is unmodified 
            # print(numbers)

            # now we can modify it in place 
            # numbers.sort() 
            # numbers.reverse()

        # Arithmetics with list
            # a = a + b
            # a += b
            # a += 2 # ERROR
            # a *= b # ERROR
            # a *= 2

# TUPLES

    # similar to lists but immutable
    # Syntax: fruits = ('orange', 'apple', 'mango')

    #Tuples can be used in much the same way as lists except we can modify them
    # fruits[0]
    # fruits[:]
    # fruits.count('apple')
    # fruits.index('apple')
    
    # We can use them to create a sequence of values that we don’t want to modify. Forexample, the list of weekday names is never going to change.
    # fruits[0] = 'kiwi' # ERROR, Can't modify
    # fruits.append('kiwi') # ERROR
    # fruits.insert(0) = 'kiwi' # ERROR
    # fruits.remove(-1) # ERROR
    # fruits.pop() # ERROR
    # fruits.sort() # ERROR, it's trying to modify original tuple
    # 
    # Tuple with a single value
    # a = (9) # it will act as an int and not tuple
    # a = (9,) # add a Trailing comma 

# SETS

    # A set is a collection of unique elements. If we add multiple copies of the same element to a set, theduplicateswill beeliminated, andwe will be left with one of each element. 

    # Syntax: fruits = { 'apple', 'orange', 'kiwi', 'apple' }
    # We can perform various set operations on sets
    # 
    # numbers = {1,2,3,4,5,6,7,8,9,10}
    # even_numbers = {2,4,6,8}
    # odd_numbers = numbers - even_numbers # subtraction
    # odd_numbers | even_numbers # union
    # odd_numbers & numbers # intersection
    # odd_numbers ^ numbers # union - intersection

    #It is important to note that unlike lists and tuples sets are not ordered. When we print a set, the order of the elements will be random. If we want to process the contents of a set in a particular order, we will ﬁrst need to convert it to a list or tuple and sort it:
    # this is an empty dictionary 
    # a = {}
    # this is how we make an empty 
    # set b = set()

# RANGES
    
    # immutable sequence
    # also called generators
    # the numbers in the range are generated one at a time as they are needed,and not all at once

# Dictionary
    
    # Thekeysofadictionarydon’thavetobestrings–theycanbeanyimmutabletype,includingnumbersandeventuples. We can mix different types of keys and different types of values in one dictionary. Keys are unique – if we repeat a key, we will overwrite the old value with the new value. When we store a value in a dictionary, the key doesn’t have to exist – it will be created automatically
    # a = { "fruit": "mango", 1:"car", (2,3):False, :"something" }
    # Like sets, dictionaries are not ordered – if we print a dictionary, the order will be random. 
    
    # Dictionary MEthods
        # Access: 
            #  a['key']; 
            #  a.get('key') # returns None if doesnt exist; 
            #  a.get('key','n/a') # returns n/a if nothing exists

        # a = { "fruit": "mango", 1:"car", (2,3):False }
        # a.update( {'fruit':'apple', 'state':'ca'} )
        # a.keys()
        # a.values()
        # a.items()
        # The last three methods return special sequence types which are read-only views of various properties of the dictionary. We cannot edit them directly, but they will be updated when we modify the dictionary. We most often access these properties because we want to iterate over them, but we can also convert them to other sequence types if we need to. 

        # We can check if a key is in the dictionary using in and not in
        # 'key' in my_dict
        # We can also check if a value is in the dictionary using in in conjunction with the values method
        # 'apple' in a.values()
        # AVOID using 'key' in a.keys() # less efficient(sequential search) than 'key' in my_dict
        # in Python 2, keys, values and items return list copies of these sequences, iterkeys, itervalues and iteritems return iterator objects, and viewkeys, viewvalues and viewitems return the view objects whicharethedefaultinPython3(but these are only available in Python2.7 and above).
      
# Converting between collection types
    
    # Implicit conversions
        #  we try to iterate over a collection in a for loop, Python will try to convert it into something that we can iterate over if it knows how to.
    # Explicit
        # We can convert between the different sequence types quite easily by using the type functions to cast sequences to the desired types
        # animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']
        # animals_set = set(animals)
        # animals_unique_list = list(animals_set)
        # animals_unique_tuple = tuple(animals_unique_list)
        # careful when converting a dictionary to a sequence
        # marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29 }
        # colours = list(marbles) # the keys will be used by default
        # counts = tuple(marbles.values()) # but we can use a view to get the values
        # marbles_set = set(marbles.items()) # or the key-value pairs
        # If we convert the key-value pairs of a dictionary to a sequence, each pair will be converted to a tuple containing the key followed by the value
        # We can also convert a sequence to a dictionary, but only if it’s a sequence of pairs – each pair must itself be a sequence with two values:

# Strings
    # Strings are also a kind of sequence type – they are sequences of characters, and share some properties with other sequences
    # s = "abracadabra"
    # print(len(s))
    # print(s.index("a"))
    
    # print(s[0])
    # print(s[3:5])
    # strings are immutable
    # # this will give us an error
    # s[0] = "b"
    #     print('a' in 'abcd') # True
    # print('ab' in 'abcd') # also True
    
    # # this doesn't work for lists
    # print(['a', 'b'] in ['a', 'b', 'c', 'd']) # False
    # convert string into a list of characters
    # lst = list('asdfsghh')
    # converting a list of characters into a string....str() won't work
    # "".join(lst)
    # join is not a function or a sequence method – it’s a string method which takes a sequence of strings as a parameter. 
    #  When we call a string’s join method, we are using that string to glue the strings in the sequence together.
    # We can use any string we like to join a SEQUENCE of strings together
    # animals = ('cat', 'dog', 'fish') # tuple - a sequence
    # a space-separated list
    # print(" ".join(animals))
    
    # # a comma-separated list
    # print(",".join(animals))
    
    # # a comma-separated list with spaces
    # print(", ".join(animals))
    
    # The opposite of joining is splitting. We can split up a string into a list of strings by using the split method. If called without any parameters, split divides up a string into words, using any number of consecutive whitespace characters as a delimiter. We can use additional parameters to specify a different delimiter as well as a limit on the maximum number of splits to perform
    
    # print("cat    dog fish\n".split())
    # print("cat|dog|fish".split("|"))
    # print("cat, dog, fish".split(", "))
    # print("cat, dog, fish".split(", ", 1))
    
#//////////////////////////////////////////////#
# --------------- Loop Contrl -----------------#
#//////////////////////////////////////////////#

