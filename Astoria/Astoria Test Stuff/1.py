User = "20louist"
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
print(X)
UpdateNum.close()
GoldScore = open("GoldScore.txt", "r")
all_lines = GoldScore.readlines()
all_lines[NewNumber] = X
GoldScore = open("GoldScore.txt", "w")
GoldScore.writelines(all_lines)
GoldScore.close()
