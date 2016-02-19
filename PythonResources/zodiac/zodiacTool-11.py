
# coding: utf-8

# In[2]:

# Now that tracking is working we can turn on the chart

#Imports
import os.path
import json
# import the plotting library
import matplotlib
get_ipython().magic('matplotlib inline')

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

if os.path.exists('.zodiacCounts.json'):
    #counts = {}
    with open('.zodiacCounts.json','r') as infile:
        counts = json.load(infile)
else:
    counts = {}

#Ask user for input (year)
try:
    birthYear=int(input('What year were you born: '))
    listIndex = (birthYear - 4) % 12
    #print(listIndex)

    #Return character
    print("You are a ", zodiacList[listIndex])

    # INCREMENT CHARACTER VALUE IN DICTIONARY
    # Check if character is in dictionary
    # Add if it isn't
    # Increment if it is
    if zodiacList[listIndex] in counts:
        counts[zodiacList[listIndex]] += 1
    else:
        counts[zodiacList[listIndex]] = 1
    
    # Print the current version of the chart
    import matplotlib.pyplot as plt

    plt.bar(range(len(counts)), counts.values(), align='center')
    plt.xticks(range(len(counts)), list(counts.keys()))

    plt.show()
    
except ValueError:
    print("You did not enter a number")

#Repeat

# Open file if it exists or create it 
# Write Dictionary to JSON
# print(counts)
with open('.zodiacCounts.json', 'w') as outfile:
    json.dump(counts, outfile)


# In[ ]:



