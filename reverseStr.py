def rev(str1):
    rev = ""
    for i in range(len(str1)):
        rev = rev + str1[len(str1) - 1 - i]
    return rev
 
# python way >>>"".join(sorted("edcba"))

print(rev("abcde"))