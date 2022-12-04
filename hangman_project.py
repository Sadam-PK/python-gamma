import random

print('Welcome to hangman.')

word = ['python', 'game', 'winter', 'cold', 'fun', 'table tennis', 'cricket',
        'television', 'facebook', 'twitter', 'discord', 'github'
        ]
random_word = random.choice(word)

print(random_word)

for x in random_word:
    print('_', end=' ')


def print_word(guessed_letters):
    counter = 0
    right_letters = 0

    for i in random_word:
        if i in guessed_letters:
            print(random_word[i], end=' ')
            right_letters += 1
        else:
            print(' ', end=' ')
        counter += 1
    return right_letters
