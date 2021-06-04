##count1 = len(open("GoldScore.txt").readlines())
##count2 = len(open("UserLog.txt").readlines())
##with open("GoldScore.txt") as f1, open("Userlog.txt") as f2:
##    all_lines1 = f1.readlines()
##    all_lines2 = f2.readlines()

##with open("GoldScore.txt", "w") as myfile:
##    while x < count:
##        Y = str(converted_list[x])
##        print(Y, file = myfile)
##        x+= 1
##    print("Done")

##count1 = len(open("GoldScore.txt").readlines())
##count2 = len(open("UserLog.txt").readlines())
##with open("GoldScore.txt") as f:
##    converted_list = []
##    content_list = f.readlines()
##    for element in content_list:
##        converted_list.append(element.strip())
##        converted_list = list(map(int, converted_list))
##        converted_list = sorted(converted_list, reverse = True)
##y = 0
##with open("UserLog.txt") as Users:
##    Lines = Users.readlines()
##    while y < count2:
##        for x in range(count2):
##            globals()['User%s' % x] = Lines[y]
##            y+= 1
from operator import itemgetter
UList = []
SList = []
a_file = open("Tests.txt", "r")

SCORE = []
for line in a_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  SCORE.append(line_list)
  SCORE_tuples = SCORE

a_file.close()
count = len(open("Tests.txt").readlines())
x = 0
myfile = open("GoldScore.txt", "w")
while x < count:
    Scores = (SCORE[x][0])
    Users = (SCORE[x][1])
    UList.append(Users)
    SList.append(Scores)
    Item = SList[x]
    print(Item, file = myfile)
    x += 1
myfile.close()
SList.clear()
with open("GoldScore.txt") as myfile:
    Read = myfile.readlines()
    for element in Read:
        SList.append(element.strip())
        SList = list(map(int, SList))
        SList = sorted(SList, reverse = True)
print(SCORE)
print("")
Sorted = sorted(SCORE, key=itemgetter(0), reverse = True)
print(Sorted)
##A = 0
##B = 0
##C = 0
##D = count - 1
##myfile = open("Leaderboard.txt","w")
##while C < count:
##    print(list((str(SList[A]), UList[B])))
##    print(list_of_lists[D])
##    print(A)
##    print(B)
##    print(C)
##    print(D)
##    if list((str(SList[A]), UList[B])) == list_of_lists[D]:
##        print(list_of_lists[D], file = myfile)
##        A += 1
##        D = D - 1
##        C += 1
##        B = 0
##        print("-----------------------------------------------")
##    else:
##        if B < count:
##            B += 1
##        elif B >= count:
##            B = 0
##myfile.close()
