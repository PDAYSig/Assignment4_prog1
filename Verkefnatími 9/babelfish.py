import sys

myDict = {}


for line in sys.stdin:
    if " " in line:
        entry = line.split()
        myDict[entry[1]] = entry[0]

    elif line != "\n":
        
        if line.strip("\n") in myDict:
            print(myDict[line.strip("\n")])
        else:
            print("eh")