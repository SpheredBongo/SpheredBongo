def Startup():
    Loop = 0
    print("Hello user and welcome to Astoria")
    while Loop == 0:
        Account_Check = input("Do you already have an account with us? ")
        Account_Check = Account_Check.lower()
        if Account_Check == "no" or Account_Check == "yes":
            break
        else:
            print("Unrecognised input, please try again")
    if Account_Check == "no":
            Account_Setup()
    elif Account_Check == "yes":
        Account_Login()

def Account_Setup():
    import os.path
    from os import path
    global User
    global Setup
    global LNum
    Count = 0
    print("Let's get your account set up shall we?")
    while Count == 0:
        User = input("Enter a username: ")
        Password = input("Enter your password: ")
        First_Name = input("Now can I get your first name: ")
        Surname = input("And finally your surname: ")
        if path.exists((User)+".txt") == True:
            print("Username is already taken, please try again")
        elif path.exists((User)+".txt") == False:
            print("Username Available! Creating account now")
            myfile = open((User)+".txt","w")
            print(Password, file = myfile)
            print("First Name: ",First_Name, file = myfile)
            print("Surname: ",Surname, file = myfile)
            print("", file = myfile)
            print("0", file = myfile)
            print("0", file = myfile)
            print("0", file = myfile)
            print(" ", file = myfile)
            print("Leader ", file = myfile)
            myfile.close()
            myfile = open("UserLog.txt","a+")
            print(User, file = myfile)
            myfile.close()
            Count = 1
            UpdateNum = open("AstoriaDetails.txt", "r")
            all_lines = UpdateNum.readlines()
            LeaderboardNumber = all_lines[1]
            LeaderboardNumber = LeaderboardNumber.strip()
            LeaderboardNumber = int(LeaderboardNumber)
            NewLeaderBoardNumber = (LeaderboardNumber + 1)
            NewLeaderBoardNumber = str(NewLeaderBoardNumber)
            all_lines[1] = (NewLeaderBoardNumber+"\n")
            UpdateNum = open("AstoriaDetails.txt","w")
            UpdateNum.writelines(all_lines)
            UpdateNum.close()
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[8] = (NewLeaderBoardNumber+"\n")
            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close()
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            Gold = all_lines[6]
            Gold = Gold.strip()
            myfile.close()
            Total = "\n"+Gold, User
            y = " ".join(Total)
            GoldScore = open("GoldScore.txt", "r")
            Lines = GoldScore.readlines()
            Results = []
            for i in Lines:
                Results.append(i)
            print(Results)
            Results.append(y)
            str1 = "".join(str(e) for e in Results)
            print(str1)
            GoldScore = open("GoldScore.txt", "w")
            print(str1, file = GoldScore)
            GoldScore.close()

def Account_Login():
    global User
    import os.path
    from os import path
    print("Time for you to login")
    User = input("Please enter your username: ")
    Password = input("Now please enter your password: ")
    if path.exists((User)+".txt") == True:
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        PasswordCheck = all_lines[0]
        PasswordCheck = PasswordCheck.strip()
        myfile.close()
        if Password == PasswordCheck:
            "Access granted"
            Player_Data()
        elif path.exists((User)+".txt") == False:
            print("Username not recognised")
            Choice = input("""Would you like to "Try Again" or "Setup" an account""")
            Choice = Choice.lower()
            if Choice == "try again":
                Account_Login()
            elif Choice == "setup":
                Account_Setup()
            else:
                print("Unrecognised input, sending you back to the beginning")
                print("")
                Startup()
        else:
            print("I have literally no idea how you got here")
            print("Sending you back to Startup")
            print("")
            Startup()

def Player_Data():
    global User
    global Level
    global Exp
    global Gold
    global Leaderboard_Value
    myfile = open((User)+".txt","r")
    all_lines = myfile.readlines()
    Level = all_lines[4]
    Exp = all_lines[5]
    Gold = all_lines[6]
    Leaderboard_Value = all_lines[8]
    myfile.close()
    Level = Level.strip()
    Exp = Exp.strip()
    Gold = Gold.strip()
    Leaderboard1()

def Leaderboard1():
    global Gold
    global User
    UpdateNum = open((User)+".txt", "r")
    all_lines = UpdateNum.readlines()
    Gold = all_lines[6]
    NewNumber = all_lines[8]
    NewNumber = NewNumber.strip()
    NewNumber = int(NewNumber)
    UpdateNum.close()
    Gold = Gold.strip()
    Total = Gold, User
    X = " ".join(Total)
    UpdateNum.close()
    GoldScore = open("GoldScore.txt", "r")
    all_lines = GoldScore.readlines()
    all_lines[NewNumber] = X
    GoldScore = open("GoldScore.txt", "w")
    GoldScore.writelines(all_lines)
    GoldScore.close()

    Leaderboard2()

def Leaderboard2():
    from operator import itemgetter
    a_file = open("GoldScore.txt", "r")
    SCORE = []
    for line in a_file:
      stripped_line = line.strip()
      line_list = stripped_line.split()
      SCORE.append(line_list)
    a_file.close()
    myfile = open("GoldScore.txt","r")
    read = myfile.readlines()
    length = len(read)
    myfile.close()
    Sorted = sorted(list(SCORE), key = lambda x: int(x[0]), reverse  = True)
    myfile = open("Leaderboard.txt", "w")
    x = 0
    while x < length:
        y = " ".join(Sorted[x])
        print(y, file = myfile)
        x += 1
    myfile.close()
    Level_Data()

def Level_Data():
    global Exp
    global MaxExp
    global Level
    global LevelCap
    LevelCap = 10
    Level = str(Level)
    if Level == "0":
        MaxExp = 10
    elif Level == "1":
        MaxExp = 25
    elif Level == "2":
        MaxExp = 50
    elif Level == "3":
        MaxExp = 75
    elif Level == "4":
        MaxExp = 100
    elif Level == "5":
        MaxExp = 150
    elif Level == "6":
        MaxExp = 200
    elif Level == "7":
        MaxExp = 250
    elif Level == "8":
        MaxExp = 300
    elif Level == "9":
        MaxExp = 400
    elif Level == "10":
        MaxExp = 500
    elif Level == "Max":
        MaxExp = "Max"
    else:
        print("Error, Retrying")
        Level_Data()
    Main_Hub()

def Main_Hub():
    global Level
    global Exp
    global MaxExp
    global Gold
    MaxExpStr = str(MaxExp)
    print("Welcome to the main hub user!")
    print("Stats:")
    print("Level:",Level)
    if Level != "Max":
        print("Exp:",Exp+"/"+MaxExpStr)
    else:
        print("Exp: Max")
    print("Gold:",Gold)
    print("Current Tasks Available")
    print("- Daily Challenges")
    print("- Leaderboard")
    print("- Games")
    print("- Shop")
    print("- Exit")
    Ans = input("")
    Ans = Ans.lower()
    if Ans == "daily challenges":
        print("Sending you to the daily challenges now")
        Daily_Challenges()
    elif Ans == "leaderboard":
        print("Sending you to the leaderboard section now")
        Leaderboard()
    elif Ans == "games":
        print("Sending you to the games section now")
        Games()
    elif Ans == "shop":
        print("Sending you to the shop now")
        Shop()
    elif Ans == "exit":
        print("Signing out now, goodbye")
        quit()

def Daily_Challenges():
    import time
    global User
    if User == "Admin":
        Command = input("Read, Write or reset? ")
        Command = Command.lower()
        if Command == "read":
            myfile = open("Challenges.txt","r")
            all_lines = myfile.readlines()
            Challenge1 = all_lines[0]
            Challenge2 = all_lines[1]
            Challenge3 = all_lines[2]
            myfile.close
            Challenge1 = Challenge1.strip()
            Challenge2 = Challenge2.strip()
            Challenge3 = Challenge3.strip()
            print(Challenge1)
            print(Challenge2)
            print(Challenge3)
            time.sleep(5)
            while Run == 0:
                Input = input("""Would you like to go back to the "Hub" or "Sign Out" """)
                Input = Input.lower()
                if Input == "hub":
                    Run = 1
                elif Input == "sign out":
                    Run = 1
                else:
                    print("Unknown Input, try again")
            if Input == "hub":
                print("")
                Main_Hub()
            elif Input == "sign out":
                quit()
        elif Command == "write":
            Run = 0
            myfile = open("Daily_Challenges.txt","a+")
            while Run == 0:
                Input = input("What Challenge would you like to add? ")
                print(Input, file = myfile)
                Check = input("would you like to add another challenge? ")
                Check = check.lower()
                if Check == "yes":
                    print("Okay")
                elif Check == "no":
                    print("Okay Boss")
                    Run = 1
                else:
                    print("Unknown Input, please try again")
        elif Command == "reset":
            import random
            min = 0
            max = 7
            C1 = random.randint(min,max)
            C2 = random.randint(min,max)
            C3 = random.randint(min,max)
            myfile = open("Daily_Challenges.txt","r")
            all_lines = myfile.readlines()
            if C1 == 0:
                Challenge1 = all_lines[0]
            elif C1 == 1:
                Challenge1 = all_lines[1]
            elif C1 == 2:
                Challenge1 = all_lines[2]
            elif C1 == 3:
                Challenge1 = all_lines[3]
            elif C1 == 4:
                Challenge1 = all_lines[4]
            elif C1 == 5:
                Challenge1 = all_lines[5]
            elif C1 == 6:
                Challenge1 = all_lines[6]
            elif C1 == 7:
                Challenge1 = all_lines[7]
            else:
                print("Unknown Error")
            if C2 == 0:
                Challenge2 = all_lines[0]
            elif C2 == 1:
                Challenge2 = all_lines[1]
            elif C2 == 2:
                Challenge2 = all_lines[2]
            elif C2 == 3:
                Challenge2 = all_lines[3]
            elif C2 == 4:
                Challenge2 = all_lines[4]
            elif C2 == 5:
                Challenge2 = all_lines[5]
            elif C2 == 6:
                Challenge2 = all_lines[6]
            elif C2 == 7:
                Challenge2 = all_lines[7]
            else:
                print("Unknown Error")
            if C3 == 0:
                Challenge3 = all_lines[0]
            elif C3 == 1:
                Challenge3 = all_lines[1]
            elif C3 == 2:
                Challenge3 = all_lines[2]
            elif C3 == 3:
                Challenge3 = all_lines[3]
            elif C3 == 4:
                Challenge3 = all_lines[4]
            elif C3 == 5:
                Challenge3 = all_lines[5]
            elif C3 == 6:
                Challenge3 = all_lines[6]
            elif C3 == 7:
                Challenge3 = all_lines[7]
            else:
                print("Unknown Error")
            myfile.close
            Challenge1 = Challenge1.strip()
            Challenge2 = Challenge2.strip()
            Challenge3 = Challenge3.strip()
            myfile = open("Challenges.txt","w")
            print(Challenge1,file = myfile)
            print(Challenge2, file = myfile)
            print(Challenge3, file = myfile)
            myfile.close
            print("The new challenges are:")
            print(Challenge1)
            print(Challenge2)
            print(Challenge3)

    elif User != "Admin":
        Run = 0
        myfile = open("Challenges.txt","r")
        all_lines = myfile.readlines()
        Challenge1 = all_lines[0]
        Challenge2 = all_lines[1]
        Challenge3 = all_lines[2]
        Challenge1 = Challenge1.strip()
        Challenge2 = Challenge2.strip()
        Challenge3 = Challenge3.strip()
        myfile.close
        print("The new challenges are:")
        print(Challenge1)
        print(Challenge2)
        print(Challenge3)
        time.sleep(5)
        while Run == 0:
            Input = input("""Would you like to go back to the "Hub" or "Sign Out" """)
            Input = Input.lower()
            if Input == "hub":
                Run = 1
            elif Input == "sign out":
                Run = 1
            else:
                print("Unknown Input, try again")
        if Input == "hub":
            print("")
            Main_Hub()
        elif Input == "sign out":
            quit()
    else:
        print("Who are you?!")

def Leaderboard():
    import time
    myfile = open("Leaderboard.txt","r")
    all_lines = myfile.readlines()
    x = 0
    while x < len(all_lines):
        all_lines[x] = all_lines[x].strip()
        print(all_lines[x])
        x+= 1
    time.sleep(5)
    print("")
    Loop = 0
    while Loop == 0:
        print("would you like to....")
        print("1. Go to the main hub")
        print("2. Exit")
        Input = input("")
        if Input == "1":
            Loop = 1
        elif Input == "2":
            Loop = 2
        else:
            print("Unknown input, please try again")
    if Input == "1":
        Main_Hub()
    elif Input == "2":
        quit()

def Games():
    global Level
    GTN = 0
    NTS = 0
    BG = 0
    HM = 0
    RPS = 0
    BLJA = 0
    HR = 0
    ROU = 0
    FAC = 0
    MQ = 0
    CG = 0
    Level = Level.strip()
    Run = 0
    print("Current Games Available:")
    if Level == "0":
        print("-Guess the number")
    elif Level == "1":
        print("-Guess the number")
        print("-Name the song")
    elif Level == "2":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
    elif Level == "3":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
    elif Level == "4":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
    elif Level == "5":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
    elif Level == "6":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
        print("-Horse race")
    elif Level == "7":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
        print("-Horse race")
        print("-Roulette")
    elif Level == "8":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
        print("-Horse race")
        print("-Roulette")
        print("-Flip a coin")
    elif Level == "9":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
        print("-Horse race")
        print("-Roulette")
        print("-Flip a coin")
        print("-Maths quiz")
    elif Level == "10" or Level == "Max":
        print("-Guess the number")
        print("-Name the song")
        print("-Board game")
        print("-Hangman")
        print("-Rock, Paper, Scissors")
        print("-Blackjack")
        print("-Horse race")
        print("-Roulette")
        print("-Flip a coin")
        print("-Maths quiz")
        print("-Champions Game")
    if Level != "Max":
        Level = int(Level)
    while Run == 0:
        Input = input("What game would you like to play? ")
        Input = Input.lower()
        if Input == "guess the number" and (Level == "Max" or Level >= 0):
            GTN = 1
            Run = 1
        elif Input == "name the song" and Level >= 1 or Level == "Max":
            NTS = 1
            Run = 1
        elif Input == "board game" and Level >= 2 or Level == "Max":
            BG = 1
            Run = 1
        elif Input == "hangman" and Level >= 3 or Level == "Max":
            HM = 1
            Run = 1
        elif Input == "rock paper scissors" and Level >= 4 or Level == "Max":
            RPS = 0
            Run = 1
        elif Input == "blackjack" and Level >= 5 or Level == "Max":
            BLJA = 1
            Run = 1
        elif Input == "horse race" and Level >= 6 or Level == "Max":
            HR = 1
            Run = 1
        elif Input == "roulette" and Level >= 7 or Level == "Max":
            ROU = 1
            Run = 1
        elif Input == "flip a coin" and Level >= 8 or Level == "Max":
            FAC = 1
            Run = 1
        elif Input == "maths quiz" and Level >= 9 or Level == "Max":
            MQ = 1
            Run = 1
        elif Input == "champions game" and Level == 10 or Level == "Max":
            CG = 1
            Run = 1
        else:
             print("Unknown Input, please try again")

    if Input == "guess the number" and GTN == 1:
        print("Loading...")
        guess_the_number()
    elif Input == "name the song" and NTS == 1:
        print("Loading...")
        name_the_song()
    elif Input == "board game" and BG == 1:
        print("Loading...")
        Board_game()
    elif Input == "hangman" and HM == 1:
        print("Loading...")
        Hangman()
    elif Input == "rock paper scissors" and RPS == 1:
        print("Loading...")
        rock_paper_scissors()
    elif Input == "blackjack" and BLJA == 1:
        print("Loading...")
        blackjack()
    elif Input == "horse race" and HR == 1:
        print("Loading...")
        horse_race()
    elif Input == "roulette" and ROU == 1:
        print("Loading...")
        roulette()
    elif Input == "flip a coin" and FAC == 1:
        print("Loading...")
        flip_a_coin()
    elif Input == "maths quiz" and MQ == 1:
            maths_quiz()
    elif Input == "champions game" and CG == 1:
        print("Loading...")
        champions_game()

def Shop():
    print("Shop")

def guess_the_number():
    global Gold
    import random
    Gold = int(Gold)
    Play_again = 0
    Win = False
    Run = 0
    Guess = 0
    Count = 0
    print("")
    Input = input("Difficulty: Easy, Medium or Hard? ")
    Input = Input.lower()
    while Run == 0:
        if Input == "easy":
            print("Range is between 1 - 100")
            min = 1
            max = 100
            Number = random.randint(min,max)
            while Guess != Number:
                try:
                    Guess = int(input("Enter a number: "))
                except ValueError:
                    print("Integers only please: ")
                    Guess = -1
                if Guess == Number:
                    print("You got it! The number was:", Number)
                    Run = 1
                    Win = True
                elif Guess == -1:
                    print("")
                elif Guess > 100:
                    print("Too high! Out of range!")
                    print("")
                    Count += 1
                elif Guess < 1:
                    print("Too low! Out of range!")
                    print("")
                    Count += 1
                elif Guess < Number:
                    print("Your guess is below the number")
                    print("")
                    Count += 1
                elif Guess > Number:
                    print("Your guess is above the number")
                    print("")
                    Count += 1
                else:
                    print("How?!")
                    print("")
                    Count += 1
        elif Input == "medium":
            print("Range is between 1 - 500")
            min = 1
            max = 500
            Number = random.randint(min,max)
            while Guess != Number:
                try:
                    Guess = int(input("Enter a number: "))
                except ValueError:
                    print("Integers only please: ")
                    Guess = -1
                if Guess == Number:
                    print("You got it! The number was:", Number)
                    Run = 1
                    Win = True
                elif Guess == -1:
                    print("")
                elif Guess > 500:
                    print("Too high! Out of range!")
                    print("")
                    Count += 1
                elif Guess < 1:
                    print("Too low! Out of range!")
                    print("")
                    Count += 1
                elif Guess < Number:
                    print("Your guess is below the number")
                    print("")
                    Count += 1
                elif Guess > Number:
                    print("Your guess is above the number")
                    print("")
                    Count += 1
                else:
                    print("How?!")
                    Count += 1
        elif Input == "hard":
            print("Range is between 1 - 1000")
            min = 1
            max = 1000
            Number = random.randint(min,max)
            while Guess != Number:
                try:
                    Guess = int(input("Enter a number: "))
                except ValueError:
                    print("Integers only please: ")
                    Guess = -1
                if Guess == Number:
                    print("You got it! The number was:", Number)
                    Run = 1
                    Win = True
                elif Guess == -1:
                    print("")
                elif Guess > 1000:
                    print("Too high! Out of range!")
                    print("")
                    Count += 1
                elif Guess < 1:
                    print("Too low! Out of range!")
                    print("")
                    Count += 1
                elif Guess < Number:
                    print("Your guess is below the number")
                    print("")
                    Count += 1
                elif Guess > Number:
                    print("Your guess is above the number")
                    print("")
                    Count += 1
                else:
                    print("How?!")
                    Count += 1
    if Win == True:
        PossibleWin = 1000
        Score = Count * 100
        GoldWon = PossibleWin - Score
        if GoldWon < 100:
            GoldWon = 50
        GoldWon = Gold + GoldWon
        Gold = GoldWon
        GoldWon = str(GoldWon)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (GoldWon+"\n")
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        while Play_again == 0:
            print("Play again?, y/n")
            INP = input("")
            INP = INP.lower()
            if INP == "y":
                break
            elif INP == "n":
                break
            else:
                print("Unknown Input, please try again")
        if INP == "y":
                guess_the_number()
        elif INP == "n":
            print("Okay sending you back to the main hub")
            print("")
            Leaderboard1()


def Name_the_song():
    print("Name the song")

def Board_game():
    import random
    global Gold
    Gold = int(Gold)
    Tile = -1
    while Tile == -1:
        print("Begin? y/n")
        Input = input("")
        if Input == "y":
            Roll = True
            Tile += 1
        elif Input == "n":
            Roll = False
            Tile += 1
        else:
            print("Unknown Input, please try again")
    while Tile <= 100:
        Loop = 0
        while Loop == 0:
            print("press enter to roll")
            Input = input("")
            if Input == "":
                break
            else:
                print("Unknown Input, please try again")
        DiceRoll = random.randint(1,6)
        Tile = Tile + DiceRoll
        print("Tile:", Tile)
        Div = Tile % 5
        if Div != 0:
            print("+5 Gold")
            Gold += 5
        else:
            print("-15 Gold")
            Gold -= 15
        if Tile == 100:
            print("Tile:", Tile)
            Gold += 15
            break
    while Tile > 100 or Tile < 100:
        Tile = Tile - DiceRoll
        print("Rolled over Tile 100. went back to Tile:", Tile)
        print("press enter to roll again")
        Input = input("")
        if Input == "":
            DiceRoll = random.randint(1,6)
            Tile = Tile + DiceRoll
            if Tile == 100:
                break
        else:
            print("Unknown Input, please try again")
    if Tile == 100:
        print("You reached Tile 100 you win")
        if Gold < 0:
            Gold = 0
        print("Your new gold score:", Gold)
        Gold = str(Gold)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (Gold+"\n")
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        print("Saving Gold now and sending you back to the Main Hub")
        print("")
        Leaderboard1()


def Hangman():
    End = False
    import sys
    import random
    TextWords = open("HangmanWords.txt", "r")
    Words = TextWords.readlines()
    TextWords.close()
    Loop = 0
    while Loop == 0:
        print("Would you like the:")
        print("1. Astoria Category")
        print("2. Colours Category")
        print("3. Superheroes Category")
        print("4. Python Category")
        Category = input("")
        if Category == "1":
            min = 0
            max = 4
            Loop = 1
        elif Category == "2":
            min = 6
            max = 17
            Loop = 1
        elif Category == "3":
            min = 19
            max = 25
            Loop = 1
        elif Category == "4":
            min = 27
            max = 36
            Loop = 1
        else:
            print("Unknown Input, please try again")
            print("")
    wordnum = random.randint(min,max)
    word = Words[wordnum]
    word = word.strip()
    word = word.lower()
    guesses = " "
    turns = 10
    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char)
            else:
                print("_")
                failed += 1
        if failed == 0:
            print("You win!")
            choice = input("Would you like to play again? y/n: ")
            if choice == "y":
                Hangman()
            elif choice == "n":
                End = True
                break
            else:
                print("Something went wrong, type y or n.")
        guess = input("Guess a character: ")
        guesses += guess
        if guess not in word:
          turns -= 1
          print("Wrong!")
          print(f"You have {turns} more guesses.")
          if turns == 0:
            print("You lose!")
            choice = input("Would you like to play again? y/n: ")
            if "y" in choice:
              Hangman()
            elif "n" in choice:
              End = True
              turns = 0
            else:
              print("Unknown Input,please type y or n.")
    if End == True:
        Main_Hub()
def rock_paper_scissors():
    import random
    global Gold
    global User
    Win = False
    Lose = False
    UserRock = False
    UserPaper = False
    UserScissors = False
    CompRock = False
    CompPaper = False
    CompScissors = False
    Loop = 0
    while Loop == 0:
        print("Do you choose....")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        UserInput = input("")
        if UserInput == "1":
              UserRock = True
              Loop = 1
        elif UserInput == "2":
            UserPaper = True
            Loop = 1
        elif UserInput == "3":
            UserScissors = True
            Loop = 1
        else:
            print("Error: 1")
    CompGuess = random.randint(1,3)
    if CompGuess == 1:
          CompRock = True
    elif CompGuess == 2:
        CompPaper = True
    elif CompGuess == 3:
        CompScissors = True
    if UserRock == True and CompRock == True:
        print("Draw")
    elif UserRock == True and CompPaper == True:
        print("You lose")
        Lose = True
    elif UserRock == True and CompScissors == True:
        print("You win")
        Win = True
    elif UserPaper == True and CompRock == True:
        print("You win")
        Win = True
    elif UserPaper == True and CompPaper == True:
        print("Draw")
    elif UserPaper == True and CompScissors == True:
        print("You lose")
        Lose = True
    elif UserScissors == True and CompRock == True:
        print("You lose")
        Lose = True
    elif UserScissors == True and CompPaper == True:
        print("You win")
        Win = True
    elif UserScissors == True and CompScissors == True:
        print("Draw")
    else:
            print("Error: 2")
    if Win == True:
        Gold = int(Gold)
        GoldWon = 10
        TotalGold = Gold + GoldWon
        TotalGold = str(TotalGold)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (TotalGold+"\n")
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        print("You won", GoldWon, "Gold")
        print("Gold added to your balance! Sending you back to the hub now")
        print("")
        Leaderboard1()
    elif Lose == True:
        Gold = int(Gold)
        GoldLost = 10
        TotalGold = Gold - GoldLost
        TotalGold = str(TotalGold)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (TotalGold+"\n")
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        print("You lost", GoldLost, "Gold")
        print("Gold removed from your balance! Sending you back to the hub now")
        print("")
        Leaderboard1()

def blackjack():
    global Gold
    global User
    import random
    Win = False
    Lose = False
    Run = 0
    while Run == 0:
        try:
            Bet = int(input("Enter a bet: "))
        except ValueError:
            print("Integers only bets please: ")
            blackjack()
        if Bet == int(Bet):
            Run = 1
    Run = 1
    Gold = int(Gold)
    if Gold - Bet < 0:
        print("You don't have enough gold for that bet")
        blackjack()
    DC1 = random.randint(1,11)
    DC2 = random.randint(1,10)
    DTotal = DC1 + DC2
    print("Dealer Card 1:", DC1)
    print("Dealer Card 2:", DC2)
    print("Dealer Total:", DTotal)

    if DTotal == 21:
        print("Dealer has 21, you lose")

    UC1 = random.randint(1,11)
    UC2 = random.randint(1,10)
    UTotal = UC1 + UC2
    print("Your Card 1:", UC1)
    print("Your Card 2:", UC2)
    print("Your Total", UTotal)

    if UTotal == 21:
        print("You have 21, you win")
        Win = True

    print("""Would you like to.....
1. Double Down
2. Pick up another card
3. Stand""")
    INP = input("")
    while INP == "1":
        DoubleBet = Bet * 2
        if Gold - DoubleBet < 0:
            Bet = Bet / 2
            INP = 3
            break
        else:
            DealerDraw =  False
            UC3 = random.randint(1,11)
            UTotal = UTotal + UC3
            print("Your card 3:", UC3)
            print("Your Total:", UTotal)
            if UTotal > 21:
                print("Over 21! you lose!")
                Lose = True
            elif UTotal == 21:
                print("Score is 21, you win!")
                Win = True
            elif UTotal <= 21 and UTotal > DTotal:
                DealerDraw = True

            while DealerDraw == True:
                DC3 = random.randint(1,11)
                DTotal = DTotal + DC3
                if DTotal > 21:
                    print("Dealer got over 21, you win!")
                    Win = True
                    break
                elif DTotal == 21:
                    print("Dealer got 21, you lose!")
                    Lose = True
                    break
        INP = 0

    while INP == "2":
        Another_Card = True
        while Another_Card == True:
            AUC = random.randint(1,11)
            UTotal = UTotal + AUC
            print("Picked up:", AUC)
            print("Your Total:", UTotal)
            if UTotal > 21:
                print("Over 21, you lose!")
                Lose = True
                Another_Card = False
                Loop = 1
                break
            elif UTotal == 21:
                print("Score is 21, you win")
                Win = True
                Another_Card = False
                Loop = 1
                break
            Loop = 0
            while Loop == 0:
                Another = input("Pick up another card? ")
                Another = Another.lower()
                if Another == "yes":
                    print("Drawing another card.....")
                    break
                elif Another == "no":
                    while DTotal <= UTotal:
                        DC3 = random.randint(1,11)
                        DTotal = DTotal + DC3
                        print("Dealer picked up:", DC3)
                        print("Dealer Total:", DTotal)
                        if DTotal > 21:
                            print("Dealer got over 21, you win!")
                            Win = True
                            Another_Card = False
                            Loop = 1
                            break
                        elif DTotal == 21:
                            print("Dealer got 21, you lose!")
                            Lose = True
                            Another_Card = False
                            Loop = 1
                            break
                        elif DTotal < UTotal and UTotal <= 21:
                            print("You got higher than the dealer, you win!")
                            Win = True
                            Another_Card = False
                            Loop = 1
                            break
                        elif DTotal > UTotal and DTotal <= 21:
                            print("Dealer got higher, you lose")
                            Lose = True
                            Another_Card = False
                            Loop = 1
                            break
        INP = 0
    while INP == "3":
        DealerDraw =  False
        if UTotal > 21:
            print("Over 21! you lose!")
            Lose = True
        elif UTotal == 21:
            print("Score is 21, you win!")
            Win = True
        elif UTotal <= 21 and UTotal > DTotal:
            DealerDraw = True

        while DealerDraw == True:
            DC3 = random.randint(1,11)
            DTotal = DTotal + DC3
            if DTotal > 21:
                print("Dealer got over 21, you win!")
                Win = True
                break
            elif DTotal == 21:
                print("Dealer got 21, you lose!")
                Lose = True
                break
            elif DTotal < UTotal and UTotal <= 21:
                print("You got higher than the dealer, you win!")
                Win = True
                break
            elif DTotal > UTotal and DTotal <= 21:
                print("Dealer got higher, you lose")
                Lose = True
                break
        INP = 0
    if Win == True:
        TotalWon = Bet
        print("You won", TotalWon)
        TotalGold = Gold + TotalWon
        Gold = TotalGold
        TotalGold = str(TotalGold)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (TotalGold+"\n")
        myfile.close()
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        Play_again = 0
        while Play_again == 0:
            Play_Again = input("Play again? y/n ")
            Play_Again = Play_Again.lower()
            if Play_Again == "y":
                break
            elif Play_Again == "n":
                break
            else:
                print("Unknown Input, Please try again")
        if Play_Again == "y":
            blackjack()
        elif Play_Again == "n":
            Leaderboard1()
    elif Lose == True:
        TotalLost = Bet
        print("You lost", TotalLost)
        TotalGold = Gold - TotalLost
        TotalGold = str(TotalGold)
        myfile = open((User)+".txt","r")
        all_lines = myfile.readlines()
        all_lines[6] = (TotalGold+"\n")
        myfile = open((User)+".txt","w")
        myfile.writelines(all_lines)
        myfile.close()
        Play_again = 0
        while Play_again == 0:
            Play_Again = input("Play again? y/n ")
            Play_Again = Play_Again.lower()
            if Play_Again == "y":
                break
            elif Play_Again == "n":
                break
            else:
                print("Unknown Input, Please try again")
        if Play_Again == "y":
            blackjack()
        elif Play_Again == "n":
            Leaderboard1()

def horse_race():
    global Gold
    global User
    import random
    H1S = False
    H2S = False
    H3S = False
    Gen1 = random.randint(2,10)
    Gen2 = random.randint(2,10)
    Gen3 = random.randint(2,10)
    Loop = 0
    while Loop == 0:
        print("Welcome to Horse Race!")
        print("Would you like to:")
        print("1. Play")
        print("2. View the horses")
        print("3. Test Game")
        print("4. Hub")
        print("5. Quit")
        Input = input("")
        if Input == "1":
            print("Horse 1: 1 in", Gen1, "chance")
            print("Horse 2: 1 in", Gen2, "chance")
            print("Horse 3: 1 in", Gen3, "chance")
            Loop = 1
            while Loop == 1:
                Horse_Select = input("1, 2 or 3? ")
                if Input == "1":
                    H1S = True
                    print("Horse 1 selected")
                    Loop = 2
                elif Input == "2":
                    H2S = True
                    print("Horse 2 selected")
                    Loop = 2
                elif Input == "3":
                    H3S = True
                    print("Horse 3 selected")
                    Loop = 2
                else:
                    print("Unknown Input, Please Try Again")
            
def roulette():
    global Gold
    global User
    import random
    RedChosen = False
    BlackChosen = False
    GreenChosen = False
    OddChosen = False
    EvenChosen = False
    Gold = int(Gold)
    if Gold < 5:
        print("You don't have enough Gold, sorry")
        print("Sending you back to the main hub")
        print("")
        Main_Hub
    Run = 0
    Loop = 0
    red = [1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
    black = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
    green = 0
    even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
    odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]

    print("Red = 1")
    print("Black = 2")
    print("Green = 3")
    print("Odd = 4")
    print("Even = 5")
    while Run == 0:
        try:
            Guess = int(input("Place your bet: "))
        except ValueError:
            print("Integers only bets please: ")
        Bet = int(input("How much would you like to bet, min bet is 5 gold, max is 50 gold "))
        if Gold - Bet < 0:
            print("You don't have enough gold for that bet, try again")
        elif Gold - Bet >= 0:
            print("Placing bet...")
            print("Bet placed")
            Run = 1
    if Guess == 1:
        RedChosen = True
    elif Guess == 2:
        BlackChosen = True
    elif Guess == 3:
        GreenChosen = True
    elif Guess == 4:
        OddChosen = True
    elif Guess == 5:
        EvenChosen = True

    spin = random.randint(1,36)
    print("Landed on:", spin)

    if RedChosen == True:
        if spin in red:
            Winnings = Bet * 2
            TotalWon = Winnings - Bet
            print("You won:", TotalWon)

            TotalGold = Gold + TotalWon
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
        else:
            print("You lost:", Bet)
            TotalGold = Gold - Bet
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
    elif BlackChosen == True:
        if spin in black:
            Winnings = Bet * 2
            TotalWon = Winnings - Bet
            print("You won:", TotalWon)

            TotalGold = Gold + TotalWon
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
        else:
            print("You lost:", Bet)
            TotalGold = Gold - Bet
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
    elif GreenChosen == True:
        if spin == 0:
            Winnings = Bet * 35
            TotalWon = Winnings - Bet
            print("You won:", TotalWon)

            TotalGold = Gold + TotalWon
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
        else:
            print("You lost:", Bet)
            TotalGold = Gold - Bet
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
    elif EvenChosen == True:
        if spin in even:
            Winnings = Bet * 2
            TotalWon = Winnings - Bet
            print("You won:", TotalWon)

            TotalGold = Gold + TotalWon
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
        else:
            print("You lost:", Bet)
            TotalGold = Gold - Bet
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
    elif OddChosen == True:
        if spin in Odd:
            Winnings = Bet * 2
            TotalWon = Winnings - Bet
            print("You won:", TotalWon)

            TotalGold = Gold + TotalWon
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()
        else:
            print("You lost:", Bet)
            TotalGold = Gold - Bet
            TotalGold = str(TotalGold)
            myfile = open((User)+".txt","r")
            all_lines = myfile.readlines()
            all_lines[6] = (TotalGold+"\n")

            myfile = open((User)+".txt","w")
            myfile.writelines(all_lines)
            myfile.close
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    break
                elif Play_Again == "n":
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                roulette()
            elif Play_Again == "n":
                Leaderboard1()

def flip_a_coin():
    import random
    import time
    Run = 0
    min = 1
    max = 2
    Flip = random.randint(min,max)
    if Flip == 1:
        Result = "heads"
    elif Flip == 2:
        Result = "tails"
    else:
        print("Unknown flip result, retrying")
        flip_a_coin()
    while Run == 0:
        Guess = input("Heads or tails: ")
        Guess = Guess.lower()
        if Guess == "heads":
            Run = 1
        elif Guess == "tails":
            Run = 1
        else:
            print("Unknown Input, please try again")
        if Guess == Result:
            print("Correct! The coin landed on",Result)
        elif Guess != Result:
            print("Sorry, the coin landed on",Result)

def maths_quiz():
    global Gold
    global User
    import random
    Gold = int(Gold)
    score = 0
    QNumber = 1
    print("""Choose your difficulty:
1. Easy
2. Medium
3. Hard""")
    INP = input("")
    if INP == "1":
        while QNumber <= 10:
            print("Question", QNumber)
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            symbol = random.randint(1,3)

            if symbol == 1:
                print("What is", num1, "+", num2, "? ")
                question = int(input(""))
                answer = num1 + num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1

            elif symbol == 2:
                print("What is", num1, "-", num2, "?")
                question = int(input(""))
                answer = num1 - num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1

            elif symbol == 3:
                print("What is", num1, "*", num2, "? ")
                question = int(input(""))
                answer = num1 * num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1
        if QNumber == 11:
            GoldWon = score * 10
            TotalGold = Gold + GoldWon
            Gold = TotalGold
            TotalGold = str(TotalGold)
            with open((User)+".txt","r") as myfile:
                all_lines = myfile.readlines()
                all_lines[6] = (TotalGold+"\n")
            with open((User)+".txt","w") as myfile:
                myfile.writelines(all_lines)
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    Play = True
                    break
                elif Play_Again == "n":
                    Play = True
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                maths_quiz()
            elif Play_Again == "n":
                Leaderboard1()
    elif INP == "2":
        while QNumber <= 10:
            print("Question", QNumber)
            num1 = random.randint(1, 15)
            num2 = random.randint(1, 15)
            symbol = random.randint(1,2)

            if symbol == 1:
                print("What is", num1, "-", num2, "?")
                question = int(input(""))
                answer = num1 - num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1

            elif symbol == 2:
                print("What is", num1, "*", num2, "? ")
                question = int(input(""))
                answer = num1 * num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1
        if QNumber == 11:
            GoldWon = score * 50
            TotalGold = Gold + GoldWon
            Gold = TotalGold
            TotalGold = str(TotalGold)
            with open((User)+".txt","r") as myfile:
                all_lines = myfile.readlines()
                all_lines[6] = (TotalGold+"\n")
            with open((User)+".txt","w") as myfile:
                myfile.writelines(all_lines)
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    Play = True
                    break
                elif Play_Again == "n":
                    Play = True
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                maths_quiz()
            elif Play_Again == "n":
                Leaderboard1()
    elif INP == "3":
        while QNumber <= 10:
            print("Question", QNumber)
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            symbol = 1

            if symbol == 1:
                print("What is", num1, "*", num2, "? ")
                question = int(input(""))
                answer = num1 * num2
                if question == answer:
                    print("Correct, the answer was", answer)
                    score = score + 1
                    QNumber += 1
                else:
                    print("Incorrect, correct answer is:", answer)
                    QNumber += 1
        if QNumber == 11:
            GoldWon = score * 100
            TotalGold = Gold + GoldWon
            Gold = TotalGold
            TotalGold = str(TotalGold)
            with open((User)+".txt","r") as myfile:
                all_lines = myfile.readlines()
                all_lines[6] = (TotalGold+"\n")
            with open((User)+".txt","w") as myfile:
                myfile.writelines(all_lines)
            Play_again = 0
            while Play_again == 0:
                Play_Again = input("Play again? y/n ")
                Play_Again = Play_Again.lower()
                if Play_Again == "y":
                    Play = True
                    break
                elif Play_Again == "n":
                    Play = True
                    break
                else:
                    print("Unknown Input, Please try again")
            if Play_Again == "y":
                maths_quiz()
            elif Play_Again == "n":
                Leaderboard1()
def champions_game():
    print("Champions game")

Startup()
