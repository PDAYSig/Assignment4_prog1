p1 = input()
p2 = input()

if (p1 == p2):
    print("Draw")

elif(p1 == "rock"):
    if(p2 == "paper"):
        print("Player 2")
    else:
        print("Player 1")

elif(p1 == "paper"):
    if(p2 == "scissors"):
        print("Player 2")
    #elif(p2 == "rock"):
    else:
        print("Player 1")

elif(p1 == "scissors"):
    if(p2 == "rock"):
        print("Player 2")
    else:
        print("Player 1")
