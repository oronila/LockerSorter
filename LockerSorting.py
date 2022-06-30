                  #######################################
                  #CREATED BY: MICHEAL WONG AND NOOR ALI#
                  #               5/24/19               #
                  #         4th Period Langston         #
                  #######################################
datanumber = []
dataname = []
lockers = []

#TO CHANGE THE AMOUNT OF LOCKER SECTIONS, CHANGE ONLY THE NUMBER BELOW

amountOfLockerSections = 17 #<------ The amount of lockers sections

#IT'S ABOVE THIS LINE

nextLockerSet = 0
amountOfLockersPerSection = 24 #<-------- The amount of lockers per sections
average = 0
allNums = []
total = 0
for i in range(amountOfLockerSections):
      lockers.append([]) # Creates amount lockers per section into array
with open(r"diciplineLog.txt", "r+") as f:
   data = f.readlines() # read the text file.
   for line in data:
      allNums += line.strip().split(" ") # get a list containing all the numbers in the file.
#print(allNums)
for k in range(0,len(allNums),2):
   print(allNums[k], end = ' ') #prints names of student
   print(allNums[k+1])# prints score of student
for k in range(1,len(allNums),2):
   datanumber.append(int(allNums[k])) # Appends datanumber array for students score
for k in range(0,len(allNums),2):
   dataname.append(allNums[k]) # Appends students name into dataname array
# DATANUMBER AND DATANAME ARRAY ARE MATCHED WITH ARRAY INDEX AND PULLED FROM FILE diciplineLog.txt

   
#print(lockers)
#print(datanumber)
#print(dataname)

for i in range(len(datanumber)):
   print(nextLockerSet)
   lockers[nextLockerSet].append(dataname[i])
   lockers[nextLockerSet].append(datanumber[i])
   if (len(lockers[nextLockerSet]) == amountOfLockersPerSection*2):
      nextLockerSet += 1
   elif (datanumber[i] >= 6):
      nextLockerSet += 1 #IF POSSIBLE ANNOTATE THIS PART OF THE CODE
   if nextLockerSet <= amountOfLockerSections - 2 and len(lockers[nextLockerSet]) > len(lockers[nextLockerSet + 1]):
      nextLockerSet += 1
   elif len(lockers[amountOfLockerSections - 1]) > len(lockers[0]):
      nextLockerSet = 0
   if nextLockerSet > amountOfLockerSections - 1:
      nextLockerSet = 0
#SORTS EACH SECTION BASED ON THE LOWEST POSSIBLE SCORE
      
for i in range(len(lockers)):
   print()
   print(lockers[i])#Prints each locker section with order of students
print()


###for i in range(len(lockers)):
###   for k in range(1,len(lockers[i]),2):
###      average += lockers[i][k]
###   print (average/amountOfLockersPerSection)
###   average = 0
# FINDS AVERAGE SCORE FOR LOCKER SECTIONS


f = open("sortedLockers.txt", "w")
f.truncate(0)# Clears file with orignal numbers
f.close()
file = open("sortedLockers.txt", "w")
for i in range(len(lockers)):
   for k in range(0,len(lockers[i]),2):
      file.write(lockers[i][k])#Takes names of students then places them in text file matrix
      file.write(", ")
   file.write("\n\n")
file.close()
#CREATES FILE WITH LOCKERS SORTED WITH STUDENTS
print("Made by Michael Wong and Noor Ali")
