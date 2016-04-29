
# coding: utf-8

# In[ ]:

#Testing the previous step showed the ability of users to break the program (Why we didn't allow user input immediately).  Here we add in error trapping to catch this.
#In this version we also begin adding the ability to read from a file that has counts of zodiac characters so far, print a bar graph of all the characters seen by the program so far after someone is told their character, and then write the new data to a file.

#Open the zodiac file

zodiacText = open('zodiacDescriptions.txt')
#for line in zodiacText:
#    print(line)

#Load into a list
zodiacList = []
for line in zodiacText:
    zodiacList.append(line)

print(zodiacList)

zodiacText.close()

# check if a file with the right name exists
# if it does then open the file with the counts of zodiac characters (read-only) and initialize a dictionary with its JSON contents
# close the file
# if it doesn't then initialize the dictionary from scratch. No need to specify members.  We'll add them as they come up.


#Ask user for input (year)
try:
    birthYear=int(input('What year were you born: '))
    listIndex = (birthYear - 4) % 12
    print(listIndex)

    #Return character
    print("You are a ", zodiacList[listIndex])

    # INCREMENT CHARACTER VALUE IN DICTIONARY
    # Check if character is in dictionary
    # Add if it isn't
    # Increment if it is
    
except ValueError:
    print("You did not enter a number")

#Repeat

# Open file if it exists or create it 
# Write Dictionary to JSON


# In[ ]:



