import random
import string

def randomString(stringLength=2):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))
#Subroutine to create a random 2 letter uppercase string

f = open("diciplineLog.txt", "w")
for i in range(357):
      f.write(randomString()) #uses subroutine to make random string
      f.write(' ') 
      f.write(str(random.randint(0,9))) #creates random number between 0 and 9
      f.write('\n')
f.close()      
#CREATES RANDOM NUMBERS AND NAMES FOR STUDENTS (EDITS diciplineLog.txt)
