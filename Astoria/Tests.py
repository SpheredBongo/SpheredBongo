def GAME():
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
            choice = input("Would you like to play again? y/n\n")
            if choice == "y":
                Hangman()
            elif choice == "n":
                End = True
                turns = 0
            else:
                print("Something went wrong, type y or n.")
        if End == True:
            Main_Hub()
        guess = input("Guess a character:")
        guesses += guess
        if guess not in word:
          turns -= 1
          print("Wrong!")
          print(f"You have {turns} more guesses.")
          if turns == 0:
            print("You lose!")
            choice = input("Would you like to play again? y/n\n")
            if "y" in choice:
              Hangman()
            elif "n" in choice:
              Main_Hub()
            else:
              print("Something went wrong, type y or n.")
    if End == True:
        Main_Hub()
GAME()
