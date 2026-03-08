def play_game(count_x,count_o,count_games):
    import random
    #-----Values-----
    boarding: list = ['1','2','3','4','5','6','7','8','9']
    used_boarding: list = []
    # noinspection PyPep8Naming
    RED: str = "\033[31m"
    # noinspection PyPep8Naming
    GREEN: str = "\033[32m"
    # noinspection PyPep8Naming
    YELLOW: str = "\033[33m"
    # noinspection PyPep8Naming
    RESET: str = "\033[0m"

    #player s the 'x' or 'o'
    if count_games % 2 == 0:
        player = f"{RED}⨉{RESET}"
    else:
        player = f"{GREEN}◯{RESET}"

    #------Functions------
    def boarding_game() -> None:
        """
        This  Function printing the boarding game on the terminal
        """
        print(f"\n{YELLOW}Score -> {RED}⨉{YELLOW}: {count_x} | {GREEN}◯{YELLOW}: {count_o}{RESET}\n")
        for index, val in enumerate(boarding):
            match index :
                case 0 | 1 | 3 | 4 | 6 | 7:
                    print(f' {val} |', end='')
                case 2 | 5:
                    print(f' {val} \n---+---+---')
                case 8:
                    print(f" {val} ")

    def make_move(choice, display_number) -> None:
        """
        This Function change a spot from the boarding game and used function get_move what the user choose a spot and change it to ⨉ or ◯
        This Function do the move for computer too
        :param choice: It's the user choice on the boarding game on the terminal 1 - 9
        :param display_number: It's the user choice on the start screen 0 - 4
        """
        choice = int(choice)
        if display_number == 1 or (display_number == 2 and player == f"{RED}⨉{RESET}"):
            if choice == 0:
                play_game(0,0,0)
            else:
                boarding[choice - 1] = player
                boarding_game()
        else:
            boarding[choice - 1] = player
            print("Computer move...")
            boarding_game()

    def check_winner() -> bool:
        """
        this function check if any one win
        :return: True or False
        """
        #This line check if row
        return (boarding[0] == boarding[1] == boarding[2] or boarding[3] == boarding[4] == boarding[5] or boarding[6] == boarding[7] == boarding[8] or

        #This line check if column
            boarding[0] == boarding[3] == boarding[6] or boarding[1] == boarding[4] == boarding[7] or boarding[2] == boarding[5] == boarding[8] or

        #This line check if diagonal
            boarding[0] == boarding[4] == boarding[8] or boarding[2] == boarding[4] == boarding[6])

    def is_tie() -> bool:
        """
        This Function check if draw or not
        :return: True or False
        """
        if not check_winner():
            #print(f"{GREEN}Tie!{RESET}")
            return True
        else:
            #print(f"{GREEN}The winner is {player}!{RESET}")
            return False

    def switch_player(user) -> str:
        """
        This Function switch the player ⨉ or ◯
        :param user: user it's the player ⨉ or ◯
        :return: user
        """
        if user == f"{RED}⨉{RESET}":
            user = f"{GREEN}◯{RESET}"
            return user
        else:
            user = f"{RED}⨉{RESET}"
            return user

    def rest_the_game(count_a, count_b) -> None:
        """
        This Function start the game and remember the point's
        :param count_a: is count_x points
        :param count_b: is count_o points
        :return: None
        """

        print("do you want to play again?")
        input("if yes, press enter")
        play_game(count_a,count_b,count_games)

    def welcome_to_tic_tac_toe() -> int | None:
        """
        This Function Shows the display screen and a number to choose.
        :return:  int display choice
        """
        while True:
            print(f"{YELLOW}_____welcome to tic-tac-toe______\n{RESET}")
            user_input = input(f"\tPress{RED} '0'{RESET} reset the game points\n\t\t\tor\n\tPress {RED}'1'{RESET} for {GREEN}2{RESET} players...\n\t\t\tor\n\tPress {RED}'2'{RESET} to play with the computer...\n\t\t\tor\n\tPress {RED}'3'{RESET} switch {player} \n\t\t\tor\n\tPress {RED}'4'{RESET} for exit\n")
            if not user_input.isdigit():
                print(f"{RED}press again only numbers{RESET}")
            else:
                user_input = int(user_input)
                if user_input > 4 or user_input < 0:
                    print(f"{RED}invalid input{RESET}")
                    continue
                return user_input

    def get_move(display_number, _count_x, _count_o) -> str | None:
        """
        This Function take from the user spot where do you put ⨉ or ◯
        This Function do too random computer choice
        :param display_number: It's the user choice on the start screen 0 - 4
        :param _count_x: it's counting ⨉ win
        :param _count_o: it's counting ◯ win
        :return: user choices or computer choice
        """
        if display_number == 1 or (display_number == 2 and player == f"{RED}⨉{RESET}"):
            while True:
                choice = input(f"Player {player} choose a spot (1-9)\nYou can reset the game if you click {RED}'0'{RESET}\n")
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 0:
                        if player ==  f"{RED}⨉{RESET}":
                            _count_o +=1
                            play_game(count_x,count_o,count_games)
                        else:
                            _count_x +=1
                            play_game(count_x,count_o,count_games)
                    elif choice in used_boarding:
                        print(f'{RED}This spot is already taken{RESET}')
                        continue
                    elif choice > 9 or choice < 0:
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
                    return str(computer_choice)

    def counter(count_a, count_b, win_player) -> tuple[int, int]:
        """
        This Function count thr points and how many games we do
        :param count_a: is count_x points
        :param count_b: is count_o points
        :param win_player: is count games and help to switch '3' in the screen
        :return: count_x, count_o
        """
        if win_player == f"{RED}⨉{RESET}":
            count_a += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_a} points,player '{GREEN}◯{YELLOW}' have {count_b} points{RESET}")
        elif win_player == f"{GREEN}◯{RESET}":
            count_b += 1
            print(f"{YELLOW}player '{RED}⨉{YELLOW}' have {count_a} points,player '{GREEN}◯{YELLOW}' have {count_b} points{RESET}")
        return count_a, count_b

    #-----game------
    #Reset Game points
    display_choice = welcome_to_tic_tac_toe()
    if display_choice == 0:
        play_game(0, 0, 0)

    #game players and computer
    elif display_choice == 1 or display_choice == 2:
        boarding_game()
        for _ in boarding:
            users_choice = get_move(display_choice, count_x, count_o)
            make_move(users_choice, display_choice)
            if check_winner():
                break
            player = switch_player(player)
        count_games += 1
        if not is_tie():
            count_x, count_o = counter(count_x, count_o, player)
            print(f"{GREEN}The winner is {player}!{RESET}")
        else:
            print(f"{GREEN}Tie!{RESET}")
        rest_the_game(count_x, count_o)

    # switch symbol
    elif display_choice == 3:
        count_games += 1
        play_game(count_x, count_o, count_games)

    # end system
    else:
        print("\t_____Good Bye_____")

#The function of the game
if __name__ == '__main__':
    play_game(0,0,0)
