mystring = input('Enter a string: ')
rev_string = mystring[::-1]
if mystring == rev_string:
    print('It is a palindrome.')
else:
    print('Not a palindrome string.')
