def game():
    player1 = int(input('Enter 1 for Rock, 2 for Scissors, 3 for Paper: '))
    player2 = int(input('Enter 1 for Rock, 2 for Scissors, 3 for Paper: '))

    if player2 > player1:
        print('Player 2 wins.')
    elif player1 > player2:
        print('Player 1 wins.')
    else:
        print('It is a tie.')


while True:
    _input = input('Enter Y starting the game: ')
    if _input == 'Y' or _input == 'y':
        game()
    else:
        exit(0)
