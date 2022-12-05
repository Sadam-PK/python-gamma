import math
import random

options = ['r', 'p', 's']


def play():
    user = input('Choose "r" for rock, "p" for paper, "s" for scissors: ')
    computer = random.choice(options)

    if user == computer:
        return 0, user, computer

    if is_win(user, computer):
        return 1, user, computer
    return -1, user, computer


def is_win(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True
    return False


def best_of(n):
    player_win = 0
    computer_win = 0
    wins_necessary = math.ceil(n / 2)
    while player_win < wins_necessary and computer_win < wins_necessary:
        result, user, computer = play()
        if result == 0:
            print(f'Its a tie. You and computer choose {user}')
        elif result == 1:
            print(f'You won. You choose {user}, and computer choose {computer}')
            player_win += 1
        else:
            print(f'Computer won. You choose {user}, and computer choose {computer}')
            computer_win += 1

    if player_win > computer_win:
        print(f'\nYou have won the best of {n}.')
    else:
        print(f'\nComputer have won the best of {n}.')


if __name__ == '__main__':
    best_of(3)
