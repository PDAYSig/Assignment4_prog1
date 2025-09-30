desc = input() # Description

myDict = {}

i = 0 # ´i´ is the index of the first letter in each ´word´

for letter in desc:
    word = ""
    x = i # ´x´ is the index of the last letter in the ´word´
    while x < len(desc):
        word = word + desc[x]
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
        x += 1
    i += 1 


#´myDictSorted´ sorts the dictionary first by descending value, then by keys alphabetically. 
myDictSorted = sorted(myDict.items(), key = lambda item: (-item[1], item[0]))

# turning ´myDictSorted´ back into a dictionary
myDictSorted = dict(myDictSorted)

# Printing the outcome
for item in myDictSorted:
    print(myDictSorted[item], item)




