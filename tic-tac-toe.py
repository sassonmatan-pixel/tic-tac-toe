def play_game():
    #-----Values-----
    player = "X"
    bording = ['1','2','3','4','5','6','7','8','9']
    used_bording = []
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    x = 0
    #------Functions------

    def bording_game():
        for index, val in enumerate(bording):
            match index :
                case 0 | 1:
                    print( " " + val + " " + "|", end='')
                case 2:
                    print( f' {val}', end = " ")
                    print(f"\n---+---+---")
                case 3 | 4:
                    print(" " + val + " " + "|", end='')
                case 5:
                    print( " " + val + " ", end='')
                    print(f"\n---+---+---")
                case 6 | 7:
                    print( " " + val + " " + "|", end='')
                case 8:
                    print( " " + val + " ")

    def get_move():
        while True:
            choise = input(f"Player {player} choose a spot (1-9)\n")
            if choise.isdigit():
                choise = int(choise)
                if choise in used_bording:
                    print(f'{RED}This spot is already taken{RESET}')
                    continue
                elif choise > 9 or choise < 1:
                    print(f"{RED}Please choose a number between 1 and 9{RESET}")
                    continue
                else:
                    used_bording.append(choise)
                    choise = str(choise)
                    return choise
            else:
                    print(f"{RED}Please choose a number between 1 and 9 not str{RESET}")
                    continue

    def make_move(choise):
        choise = int(choise)
        bording[choise - 1] = player
        bording_game()

    def check_winner():
        #This line check if row
        return (bording[0] == bording[1] == bording[2] or bording[3] == bording[4] == bording[5] or bording[6] == bording[7] == bording[8] or\

        #This line check if column
            bording[0] == bording[3] == bording[6] or bording[1] == bording[4] == bording[7] or bording[2] == bording[5] == bording[8] or\

        #This line check if diagonal
            bording[0] == bording[4] == bording[8] or bording[2] == bording[4] == bording[6])

    def is_tie():
        if check_winner():
            print(f"{GREEN}The winner is {player}!{RESET}")
        else:
            print(f"{GREEN}Tie!{RESET}")

    def switch_player(user):
        if user == "X":
            user = "O"
            return user
        else:
            user = "X"
            return user

    def rest_the_game():
        print("do you want to play again?")
        input("if yes, press enter")
        play_game()
    def welcome_to_tic_tac_toe():
        print("welcome to tic-tac-toe")
        input("Press enter to continue...")



#-----game code-----

    welcome_to_tic_tac_toe()
    bording_game()
    for i in bording:
            users_choice = get_move()
            make_move(users_choice)
            if check_winner():
                break
            player = switch_player(player)
    is_tie()
    rest_the_game()

play_game()



