import random

num = random.randint(1, 9)
print(num)
guess = ''
counter = 0
while guess != num:
    guess = input('Guess a number 1 - 9 or press e for exit: ')
    if guess == 'e':
        print(f'Total guesses = {counter}')
        exit(0)
    guess = int(guess)
    counter += 1
    if guess < num:
        print('Too low')
    elif guess == num:
        print('Correct.')
        break
    else:
        print('Too high')

print(f'Total guesses = {counter}')
