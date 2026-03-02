import random

#Functions game
def play_game(count_x,count_O):
    #-----Values-----
    bording = ['1','2','3','4','5','6','7','8','9']
    used_bording = []
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    player = f"{RED}⨉{RESET}"

    #------Functions------
    def bording_game():
        print(f"\n{YELLOW}Score -> {RED}⨉{YELLOW}: {count_x} | {GREEN}◯{YELLOW}: {count_O}{RESET}\n")
        for index, val in enumerate(bording):
            match index :
                case 0 | 1 | 3 | 4 | 6 | 7:
                    print(f' {val} |', end='')
                case 2 | 5:
                    print(f' {val} \n---+---+---')
                case 8:
                    print(f" {val} ")

    def make_move(choise, display_number):
        choise = int(choise)
        if display_number == 1:
            bording[choise - 1] = player
            bording_game()
        else:
            bording[choise - 1] = player
            print("After computer move")
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
            return player
        else:
            print(f"{GREEN}Tie!{RESET}")
            return None

    def switch_player(user):
        if user == f"{RED}⨉{RESET}":
            user = f"{GREEN}◯{RESET}"
            return user
        else:
            user = f"{RED}⨉{RESET}"
            return user

    def rest_the_game(count_x, count_O):
        print("do you want to play again?")
        input("if yes, press enter")
        play_game(count_x,count_O)

    def welcome_to_tic_tac_toe():
        while True:
            print(f"{YELLOW}____welcome to tic-tac-toe____{RESET}\n")
            user_input = input(f"\tPress{RED}'1'{RESET} for {GREEN}2{RESET} players...\n\t\t\tor\n\tPress {RED}'2'{RESET} for computer player...\n\t\t\tor\n\tPress {RED}'3'{RESET} for exit\n")
            if not user_input.isdigit():
                user_input = input(f"{RED}press again only numbers{RESET}")
            else:
                user_input = int(user_input)
                if user_input > 3 or user_input < 1:
                    print(f"{RED}invalid input{RESET}")
                    continue
                return user_input

    def get_move(display_number):
        if display_number == 1 or display_number == 2 and player == f"{RED}⨉{RESET}":
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
        elif display_number == 2 and player == f"{GREEN}◯{RESET}":
            while True:
                computer_choice = random.randint(1, 9)
                if computer_choice in used_bording:
                    continue
                else:
                    return computer_choice

    def counter(count_x, count_O, result):
        if result == f"{RED}⨉{RESET}":
            count_x += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_x} points,player '{GREEN}◯{YELLOW}' have {count_O} points{RESET}")
        elif result == f"{GREEN}◯{RESET}":
            count_O += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_x} points,player '{GREEN}◯{YELLOW}' have {count_O} points{RESET}")
        return count_x, count_O
    #-----game code-----

    #-----game------
    display_choise = welcome_to_tic_tac_toe()
    if display_choise == 1 or display_choise == 2:
        bording_game()
        for _ in bording:
            users_choice = get_move(display_choise)
            make_move(users_choice, display_choise)
            if check_winner():
                break
            player = switch_player(player)
        result = is_tie()
        count_x, count_O = counter(count_x, count_O, result)
        rest_the_game(count_x, count_O)

    else:
        pass

play_game(0,0)
print("\tgood bye")