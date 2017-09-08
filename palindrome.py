def palindrome(rows):
    """
    1
    121
    12321
    1234321
    123454321
    """
    for i in range(1,rows+1):
        print(int(bin(pow(2,i) - 1)[2:])*int(bin(pow(2,i) - 1)[2:]))
        
palindrome(5)