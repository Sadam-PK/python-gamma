num = int(input('Enter a number: '))
if num % 2 == 0:
    print('You entered an even number')
    if num % 4 == 0:
        print('It is a prime number.')
else:
    print('You entered an odd number')
