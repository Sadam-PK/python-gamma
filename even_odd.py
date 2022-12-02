"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
Extras:
If the number is a multiple of 4, print out a different message. Ask the user for two numbers: one number to check (
call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not,
print a different appropriate message. """

# #----------- Solution -----------------------

num = int(input('Enter a number: '))
if num % 2 == 0:
    print('You entered an even number')
    if num % 4 == 0:
        print('It is a prime number.')
else:
    print('You entered an odd number')

check = int(input('Enter check: '))
if num % check == 0:
    print('Number is evenly divided by check.')
else:
    print('Number not evenly divided by check.')
