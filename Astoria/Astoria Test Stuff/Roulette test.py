Gold = 999
User = "Tayler"
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
    green = [0]
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
    elif GreenChosen == True:
        if spin in green:
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

roulette()
