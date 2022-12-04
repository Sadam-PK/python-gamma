import random

roll = 'y'
while roll == 'y':
    print('Rolling the dice..')
    print(random.randint(1, 6))
    print(random.randint(1, 6))

    roll_again = input('Press Y to roll again: ')
    roll = roll_again
