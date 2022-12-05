import random

options = ['r', 'p', 's']


def play():
    user = input('Choose "r" for rock, "p" for paper, "s" for scissors: ')
    computer = random.choice(options)

    if user == computer:
        return f'its a tie. You and computer choose same option {computer}'

    if is_win(user, computer):
        return f'You won. You choose {user}, and computer choose {computer}'
    return f'You lost. You choose {user}, and computer choose {computer}'


def is_win(player, opponent):
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True
    return False


if __name__ == '__main__':
    print(play())
