#Testing the previous step showed the ability of users to break the program (Why we didn't allow user input immediately).  Here we add in error trapping to catch this.

#Open the zodiac file

zodiacText = open('zodiacDescriptions.txt')
#for line in zodiacText:
#    print(line)

#Load into a list
zodiacList = []
for line in zodiacText:
    zodiacList.append(line)

print(zodiacList)

#Ask user for input (year)
try:
    birthYear=int(input('What year were you born: '))
    listIndex = (birthYear - 4) % 12
    print listIndex
    
    #Return character
    print("You are a ", zodiacList[listIndex])
    
except ValueError:
    print("You did not enter a number")

#Repeat

zodiacText.close()

#Below is a description of the task

"""
While taking a class on the culture of China, you have learned about the Chinese zodiac in which people fall into 1 of 12 categories, depending on the year of their birth. The categories, numbered 0 to 11, correspond to the following animals:

(0) monkey
(1) rooster
(2) dog
(3) pig
(4) rat
(5) ox
(6) tiger
(7) rabbit
(8) dragon
(9) snake
(10) horse
(11) goat

Those who believe in this zodiac think that the year of a person's birth influences both their personality and fortune in life.

Your task is to build a program that will ask a user for their birth year and tell them their zodiac sign.  If the user does not enter a number that can be interpreted as a year then an error message must be shown and the user given another chance.  If the user types "quit" then the program halts.

For extra credit: save each year that is input to a file and print a chart showing how many of each type or animal have been returned.

To find your zodiac sign, divide the year of your birth by 12. The remainder then determines your sign. For example: The remainder when we divide 1985 by 12, is 5; therefore, a person born in 1985 is an ox according to the Chinese zodiac.
"""