# printing
print("hi")

# Taking input from user
usr_input = input('Enter your name: ')
print(usr_input)

# using print to write to a file

with open('input.txt', 'w') as myfile:
    print("this will be written in the file", file=myfile)

# write doesn't add a new line like print

with open('input.txt', 'w') as myfile2:
    myfile2.write("Some Text")
    
with open('input.txt', 'r') as myfile2:
    print(myfile2.read())
    
# strings are immuatable - lower fn returns a copy of string
# we can’t modify a string once it has been created. However, 
# we can assign a new string value to an existing variable name.
name = 'HARMAN'
print(name)
print(name.lower())
print(name)



