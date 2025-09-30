msg1 = input()
msg2 = input()
msg3 = input()
msg4 = input()

def findX(msg):
    msgAsList = []


    for i in msg:
        msgAsList.append(i)
        
    x = ord(msgAsList[0]) - ord("H")
    return x



def decipher(msg, x): 
    msgDeciphered = ""

    for i in msg:
        
        newLetter = ord(i) - x
        if(newLetter > 126):
            diff = newLetter - 126
            newLetter = 31 + diff
        elif(newLetter < 32):
            diff = 32 - newLetter
            newLetter = 127 - diff

        msgDeciphered += chr(newLetter)

    print(msgDeciphered)


x = findX(msg1)

decipher(msg1, x)
decipher(msg2, x)
decipher(msg3, x)
decipher(msg4, x)

