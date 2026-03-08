#RED = "\033[31m"

#print(RED+"⨉")
#if user == f"{RED}⨉{RESET}":
#    user = f"{GREEN}◯{RESET}"


"""       # 1. בדיקה: האם המחשב יכול לנצח?
    for win in win_list:
        # בודקים כמה מהתאים בשורה הזו כבר תפוסים על ידי המחשב (O)
        count_o = sum(1 for cell in win if bording[int(cell) - 1] == f"{GREEN}◯{RESET}")
        # בודקים כמה תאים עדיין פנויים (לא X ולא O)
        count_empty = sum(1 for cell in win if bording[int(cell) - 1].isdigit())

        if count_o == 2 and count_empty == 1:
            for cell in win:
                if bording[int(cell) - 1].isdigit():
                    used_bording.append(int(cell))
                    return cell

    # 2. בדיקה: האם צריך לחסום את השחקן? (אותה לוגיקה רק ל-X)
    for win in win_list:
        count_x = sum(1 for cell in win if bording[int(cell) - 1] == f"{RED}⨉{RESET}")
        count_empty = sum(1 for cell in win if bording[int(cell) - 1].isdigit())

        if count_x == 2 and count_empty == 1:
            for cell in win:
                if bording[int(cell) - 1].isdigit():
                    used_bording.append(int(cell))
                    return cell

    # 3. אם אין מה לחסום ואין איך לנצח - בחר באקראי
    available_spots = [s for s in bording if s.isdigit()]
    choice = random.choice(available_spots)
    used_bording.append(int(choice))
    return choice"""