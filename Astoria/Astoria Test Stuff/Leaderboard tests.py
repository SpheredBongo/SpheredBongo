##myfile = open("example.txt","r")
##all_lines = myfile.readlines()
##count = len(open("example.txt").readlines(  ))
##myfile.close
##for x in range(count):
##    line = all_lines[x]
##    y = line.strip()
##    print(y)
##if x > count:
##    print("Done")
##with open("example.txt", "rt") as in_file:
##    for line in in_file:
##        n = int(line.strip())

##count = len(open("GoldScore.txt").readlines(  ))
##print(count)

##myfile = open("GoldScore.txt","r")
##all_lines = myfile.readlines()
##count = len(all_lines)
##myfile.close
##x = 0
##y = 0
##while x <= count:
##    all_lines[x]
##    all_lines[x] = int(all_lines[x])
##    x += 1

##f = open('GoldScore.txt', 'r')
##leaderboard = [line.replace('\n','') for line in f.readlines()]
##
##
##for i in leaderboard:
##    print(i)

##with open("GoldScore.txt", 'r') as file:
##    sorted_data=sorted(file.readlines(), 
##    key=lambda item: int(item.rsplit('=',1)[-1].strip()))

##myfile = open("GoldScore.txt","r")
##all_lines = myfile.readlines()
##SortedScores = sorted(all_lines, reverse = True)
##
##for line in range(3):
##    print(str(SortedScores[line]))

with open("GoldScore.txt") as f:
    converted_list = []
    content_list = f.readlines()
    for element in content_list:
        converted_list.append(element.strip())
        converted_list = list(map(int, converted_list))
        converted_list = sorted(converted_list, reverse = True)
    print(converted_list)
