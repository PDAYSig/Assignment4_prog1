playerTurn = 1 #marks which player is playing

wordsUsed = set()

numOfWords = int(input())
word = input()
lastWord = word[0]

for x in range(numOfWords):
    if word[0] == lastWord[-1] and word not in wordsUsed:
        wordsUsed.add(word)
    else:
        print("Player", playerTurn, "lost")
        break
    if playerTurn == 1: #changes whose turn it is from 1 to 2
        playerTurn += 1
    else: #changes whose turn it is from 2 to 1
        playerTurn -= 1
    if len(wordsUsed) < numOfWords:
        lastWord = word
        word = input()

if len(wordsUsed) == numOfWords:
    print("Fair Game")
    