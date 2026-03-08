#RED = "\033[31m"

#print(RED+"⨉")
#if user == f"{RED}⨉{RESET}":
#    user = f"{GREEN}◯{RESET}"
print("┏━━━━━━━┓")
print("┃   ⨉   ┃")
print("┗━━━━━━━┛")


"""        else : #display_number == 2 and player == f"{_GREEN}◯{_RESET}"
            win_list = [
                ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],  # שורות
                ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # עמודות
                ['1', '5', '9'], ['3', '5', '7']  # אלכסונים
            ]
            # 1. בדיקה: האם המחשב יכול לנצח?
            for win in win_list:
                # בודקים כמה מהתאים בשורה הזו כבר תפוסים על ידי המחשב (O)
                count_o = sum(1 for cell in win if boarding[int(cell) - 1] == f"{GREEN}◯{RESET}")
                # בודקים כמה תאים עדיין פנויים (לא X ולא O)
                count_empty = sum(1 for cell in win if boarding[int(cell) - 1].isdigit())

                if count_o == 2 and count_empty == 1:
                    for cell in win:
                        if boarding[int(cell) - 1].isdigit():
                            used_boarding.append(int(cell))
                            return cell

            # 2. בדיקה: האם צריך לחסום את השחקן? (אותה לוגיקה רק ל-X)
            for win in win_list:
                count_x = sum(1 for cell in win if boarding[int(cell) - 1] == f"{RED}⨉{RESET}")
                count_empty = sum(1 for cell in win if boarding[int(cell) - 1].isdigit())

                if count_x == 2 and count_empty == 1:
                    for cell in win:
                        if boarding[int(cell) - 1].isdigit():
                            used_boarding.append(int(cell))
                            return cell

            # 3. אם אין מה לחסום ואין איך לנצח - בחר באקראי
            available_spots = [s for s in boarding if s.isdigit()]
            choice = random.choice(available_spots)
            used_boarding.append(int(choice))
            return choice       """