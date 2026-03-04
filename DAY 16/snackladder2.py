import random
import sys  # to terminate the program

def dice():
    return random.randint(1, 6)


player_1 = input("enter the player_1 game: ").title()
player_2 = input("enter the player_2 game: ").title()

player1_score, player2_score = 0, 0
winning_point = 100

snacks = {16: 8, 32: 20, 43: 4, 50: 27, 73: 32, 87: 49, 98: 6, 92: 77}
ladders = {7: 24, 14: 40, 25: 89, 37: 42, 57: 76, 79: 83}


def player1_turn():
    global player1_score
    player1_status = input(f"{player_1}, you want to [c]ontinue or [q]uit: ").lower()

    if player1_status == 'q':
        sys.exit()

    if player1_status == 'c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')
        player1_score += cur_dic

        if player1_score in snacks:
            player1_score = snacks[player1_score]
            print(f'Board position after snake bite: {player1_score} -------')

        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f'Board position after ladder: {player1_score} +++++++++++')

        else:
            print(f'board position: {player1_score}')

        if player1_score >= winning_point:
            print(f'congrats {player_1}, you won the game!!')
            sys.exit()


def player2_turn():
    global player2_score
    player2_status = input(f"{player_2}, you want to [c]ontinue or [q]uit: ").lower()

    if player2_status == 'q':
        sys.exit()

    if player2_status == 'c':
        cur_dic = dice()
        print(f'Dice: {cur_dic}')
        player2_score += cur_dic

        if player2_score in snacks:
            player2_score = snacks[player2_score]
            print(f'Board position after snake bite: {player2_score} -------')

        elif player2_score in ladders:
            player2_score = ladders[player2_score]
            print(f'Board position after ladder: {player2_score} +++++++++++')

        else:
            print(f'board position: {player2_score}')

        if player2_score >= winning_point:
            print(f'congrats {player_2}, you won the game!!')
            sys.exit()


while player1_score < winning_point and player2_score < winning_point:
    player1_turn()
    player2_turn()

if player1_score > player2_score:
    print(f'congrats {player_1}, you won the game!!!')
else:
    print(f'congrats {player_2}, you won the game!!!')
