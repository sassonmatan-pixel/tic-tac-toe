import time

# colors for printing
red = '\033[31m'  # for
orange = '\033[38;5;208m'
dark_orange = '\033[38;5;166m'
yellow = '\033[93m'
light_purple = '\033[38;2;179;136;255m'
forest_green = '\033[38;2;46;139;87m'
bright_white = '\033[97m'
reset_color = '\033[0m'

def play_game():
# Welcome message
    line = f'{light_purple}{'─' * 54}{reset_color}'
    print(line)
    print(f'{forest_green}    ✨  WELCOME TO THE GAME OF TIC TAC TOE  ✨{reset_color}')
    print(f'{forest_green}    ✨  Crafted with care by: Liran Martefl ✨{reset_color}')
    print(f'{forest_green}               I hope you enjoy😇                      ')
    print(line)
    player_1_name = input(f'{reset_color}What is your name? \n')
    player_2_name = None

# showing the rules of the game to the players if they choose to
    def game_rules():
        rules_of_game = (f'Hello {player_1_name} Nice to meet you!😊 the rules of the game are:\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n1.Two players game: one is X, the other is O.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n2.Players take turns placing their mark in an empty square.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n3.The first player to get 3 in a row (horizontal, vertical, or diagonal) wins.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n4.If there is no possible way for either player to get three in a row, the game is a draw.\n{forest_green}{'─' * 60}{reset_color}'
                         f'\n5. You need to press the number in order to replace him and pick the spot\n{forest_green}{'─' * 60}{reset_color}')
        return rules_of_game

# player's choosing options
    def game_options():
        choose: str = (input(f'Hey {player_1_name}, Those are your options:\nTo see the rules of the game press {light_purple}"1"{reset_color}\n'
                       f'for Player vs Player press {light_purple}"2"{reset_color}\nTo exit press {light_purple}"3"{reset_color}\n'))
        choose = choose.lower()
        if choose == '1':
            print(f'{forest_green}loading....{reset_color}')
            time.sleep(1)
            print(rules)
            return '1'
        elif choose == '2':
            return '2'
        else:
            return '3'
    rules = game_rules()
    counter_of_wins = [0, 0]

# picking marks for the game
    def player_pick():
        player_1: str = (input(f'{player_1_name}, please pick your mark:\npress X for X or O for O: ''\n'))
        player_1 = player_1.lower()
        if player_1 == 'x':
            player_1 = '❌'
            player_2 = '⭕️'
            print(f'{player_1_name} is: {player_1} {player_2_name} is: {player_2} GOOD LUCK😄')
            return player_1, player_2
        else:
            player_1 = '⭕️'
            player_2 = '❌'
            print(f'{player_1_name} is: {player_1} {player_2_name} is: {player_2} GOOD LUCK😄')
            return player_1, player_2
    _board_ = [' 1', '2', '3',
               ' 4', '5', '6',
               ' 7', '8', '9']
# rules of the board of the game
    def board(current_board):
        for row in range(len(current_board)):
            print(current_board[row], end=' ')
            match row:
                case 2 | 5:
                    print()
                    print('----+-----+----')
                case 8:
                    print()
                case _:
                    print(' | ', end=' ')
        return current_board

# players pick their spot to play :)
    def pick_spot(sign):
        # each player move
        while True:
            choose = input('\nplayer, What is your move? press the number you want to replace: ')
            if choose.isdigit():
                player_action = int(choose)
                if 1 <= player_action <= 9:
                    if board_of_game[player_action - 1] != '❌' and board_of_game[player_action - 1] != '⭕️':
                        board_of_game[player_action - 1] = sign
                        board(game_board)
                        return sign
                    else:
                        print('this place is taken🥲')
                        continue
        return player_action

    def play_flow(checking_board,sign):
        for turn in range (9):
            if turn % 2 == 0:
                name = player_1_name
                mark = sign[0]
                i = 0
            else:
                name = player_2_name
                mark = sign[1]
                i = 1
            pick_spot(mark)
            check_draw = draw(sign)
            if check_draw == 'reset':
                return 'reset'
            elif (winning_by_row(checking_board, mark) or winning_by_col(checking_board,mark)
                    or winning_by_diagonal(checking_board,mark)):
                print ()
                print(f'{yellow}-----{name} is the winner🥳-----{reset_color}\n')
                counter_of_wins[i] += 1
                return counter_of_wins
            elif check_draw == True:
                print('its a draw🤝🏼')
                break
# letting the game_flow know that we sent him a reset option, if True, send it out.
            if draw == 'reset':
                return 'reset'
        return counter_of_wins

    def winning_by_row(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0:3] == winning_sign or current_board[3:6] == winning_sign or current_board[
            6::] == winning_sign:
            return True
        else:
            return False

    def winning_by_col(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0::3] == winning_sign or current_board[1::3] == winning_sign or current_board[
            2::3] == winning_sign:
            return True
        else:
            return False

    def winning_by_diagonal(current_board, sign):
        winning_sign = [sign, sign, sign]
        if current_board[0::4] == winning_sign or current_board[2:7:2] == winning_sign:
            return True
        else:
            return False

    def draw(marks_on_board):
        winning_ways = [
# row
            board_of_game[0:3], board_of_game[3:6], board_of_game[6:9],
# col
            board_of_game[0:9:3], board_of_game[1:9:3], board_of_game[2:9:3],
# diagonal
            board_of_game[0:9:4], board_of_game[2:7:2]]
        cant_win = 0
# restarting mid game
        for path in winning_ways:
            if marks_on_board[0] in path and marks_on_board[1] in path:
                cant_win += 1
                if cant_win == 6:
                    print(f'{dark_orange}it is close to a tie, would you like to reset?')
                    asking_for_reset = input(f'(y/n): {reset_color}')
                    if asking_for_reset == 'y':
                        print('restarting the game....')
                        time.sleep(0.5)
                        for i in range(9):
                            game_board[i] = _board_[i]
                        return 'reset'
                    else:
                        continue
        if cant_win == 8:
            return True
        return False

# to create a loop so a reset will be possible, and for counting score
    while True:
        choice = game_options()
        if choice == '3':
            print('Thank you for playing, goodbye!')
            break
        if choice == '1':
            continue
        elif choice == '2':
            player_2_name = input(f'{player_1_name}, {red}Who is your opponent?{reset_color} ')
            counter_of_wins = [0, 0]
        while True:
            _board_ = [' 1', '2', '3',
                       ' 4', '5', '6',
                       ' 7', '8', '9']
            player_picking = player_pick()
            game_board = _board_.copy()
            board_of_game = board(game_board)
            signs = player_picking
            result = play_flow(game_board,signs)
            if result == 'reset':
                continue
# printing the final score after each game
            print(f'{orange}the score is:\nplayer 1: {counter_of_wins[0]}\nplayer 2: {counter_of_wins[1]}')
            restart = input(f'Do you want to play again? press (y/n): {reset_color}\n')
            restart = restart.lower()
            if restart != 'y':
                print(f'{light_purple}Thank you for playing!{reset_color}\n')
                if counter_of_wins[0] > counter_of_wins[1]:
                    print(f'{yellow}The winner is: {player_1_name}🎉🥇🎉{reset_color}\n')
                    break
                elif counter_of_wins[1] == counter_of_wins[0]:
                    print(f'{bright_white}Its a draw! 🤝🏼 good job!{reset_color}\n')
                    break
                else:
                    print(f'{yellow}The winner is: {player_2_name}🎉🥇🎉{reset_color}\n')
                    break
            else:
                continue
play_game()