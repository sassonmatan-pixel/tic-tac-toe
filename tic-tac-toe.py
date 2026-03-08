def play_game(count_x,count_o):
    import random
    #-----Values-----
    boarding = ['1','2','3','4','5','6','7','8','9']
    used_boarding = []
    # noinspection PyPep8Naming
    RED = "\033[31m"
    # noinspection PyPep8Naming
    GREEN = "\033[32m"
    # noinspection PyPep8Naming
    YELLOW = "\033[33m"
    # noinspection PyPep8Naming
    RESET = "\033[0m"

    #player s the 'x' or 'o'
    if (count_x + count_o) % 2 == 0:
        player = f"{RED}⨉{RESET}"
    else:
        player = f"{GREEN}◯{RESET}"

    #------Functions------
    def boarding_game():
        print(f"\n{YELLOW}Score -> {RED}⨉{YELLOW}: {count_x} | {GREEN}◯{YELLOW}: {count_o}{RESET}\n")
        for index, val in enumerate(boarding):
            match index :
                case 0 | 1 | 3 | 4 | 6 | 7:
                    print(f' {val} |', end='')
                case 2 | 5:
                    print(f' {val} \n---+---+---')
                case 8:
                    print(f" {val} ")

    def make_move(choice, display_number):
        choice = int(choice)
        if display_number == 1:
            boarding[choice - 1] = player
            boarding_game()
        else:
            boarding[choice - 1] = player
            print("Computer move...")
            boarding_game()

    def check_winner():
        #This line check if row
        return (boarding[0] == boarding[1] == boarding[2] or boarding[3] == boarding[4] == boarding[5] or boarding[6] == boarding[7] == boarding[8] or

        #This line check if column
            boarding[0] == boarding[3] == boarding[6] or boarding[1] == boarding[4] == boarding[7] or boarding[2] == boarding[5] == boarding[8] or

        #This line check if diagonal
            boarding[0] == boarding[4] == boarding[8] or boarding[2] == boarding[4] == boarding[6])

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

    def rest_the_game(count_a, count_b):
        print("do you want to play again?")
        input("if yes, press enter")
        play_game(count_a,count_b)

    def welcome_to_tic_tac_toe():
        while True:
            print(f"{YELLOW}____welcome to tic-tac-toe____{RESET}\n")
            user_input = input(f"\tPress{RED}'1'{RESET} for {GREEN}2{RESET} players...\n\t\t\tor\n\tPress {RED}'2'{RESET} for computer player...\n\t\t\tor\n\tPress {RED}'3'{RESET} for exit\n")
            if not user_input.isdigit():
                print(f"{RED}press again only numbers{RESET}")
            else:
                user_input = int(user_input)
                if user_input > 3 or user_input < 1:
                    print(f"{RED}invalid input{RESET}")
                    continue
                return user_input

    def get_move(display_number):
        if display_number == 1 or display_number == 2 and player == f"{RED}⨉{RESET}":
            while True:
                choice = input(f"Player {player} choose a spot (1-9)\n")
                if choice.isdigit():
                    choice = int(choice)
                    if choice in used_boarding:
                        print(f'{RED}This spot is already taken{RESET}')
                        continue
                    elif choice > 9 or choice < 1:
                        print(f"{RED}Please choose a number between 1 and 9{RESET}")
                        continue
                    else:
                        used_boarding.append(choice)
                        choice = str(choice)
                        return choice
                else:
                        print(f"{RED}Please choose a number between 1 and 9 not str{RESET}")
                        continue
        else : #display_number == 2 and player == f"{_GREEN}◯{_RESET}"
            while True:
                computer_choice = random.randint(1, 9)
                if computer_choice in used_boarding:
                    continue
                else:
                    used_boarding.append(computer_choice)
                    return computer_choice

    def counter(count_a, count_b, _result):
        if _result == f"{RED}⨉{RESET}":
            count_a += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_a} points,player '{GREEN}◯{YELLOW}' have {count_b} points{RESET}")
        elif _result == f"{GREEN}◯{RESET}":
            count_b += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_a} points,player '{GREEN}◯{YELLOW}' have {count_b} points{RESET}")
        return count_a, count_b

    #-----game------
    display_choice = welcome_to_tic_tac_toe()
    if display_choice == 1 or display_choice == 2:
        boarding_game()
        for _ in boarding:
            users_choice = get_move(display_choice)
            make_move(users_choice, display_choice)
            if check_winner():
                break
            player = switch_player(player)
        result = is_tie()
        count_x, count_o = counter(count_x, count_o, result)
        rest_the_game(count_x, count_o)

    else:
        print("\tgood bye")

if __name__ == '__main__':
    play_game(0, 0)
