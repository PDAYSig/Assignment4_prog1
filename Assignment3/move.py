def moveCharacter(pos:int, movement:str):
    '''This function takes in the current position of the character
    and moves it according to the user input'''
    if movement == 'r':
        pos += 1
    elif movement == 'l':
        pos -= 1
    #If the function goes outside of the idex range we must pull it back
    if pos == 11:
        pos = 10
    elif pos == 0:
        pos = 1

    return pos

def displayAxis(placement:list, pos:int, movement:str):
    '''This function takes in a list and the position of the character and displays the axis'''
    if movement == 'r':
        placement[pos - 2] = 'x' 
        placement[pos - 1] = 'o'
        
    elif movement == 'l':
        placement[pos] = 'x'
        placement[pos - 1] = 'o'
    
    for x in placement:
        print(x, end="")
    print()

def posInAxisRange(pos:int):
    '''This function returns True if the number is in between 0 and 9, otherwise it returns False'''
    return pos <= 10 and pos >= 1

print("Position in [1..10]: ")
pos = int(input()) #the position of the character

while not posInAxisRange(pos):
    print("Position in [1..10]: ")
    pos = int(input())

if posInAxisRange(pos):
    placement = ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
    placement[pos - 1] = 'o'
    for x in placement:
        print(x, end="")
    print()

# displayAxis(placement, pos)
print("l: left\n", "r: right\n", "Move:", sep="")
movement = input() #the direction of movement

while movement == 'r' or movement == 'l':
    pos = moveCharacter(pos, movement)
    displayAxis(placement, pos, movement)
    print("l: left\n", "r: right\n", "Move:", sep= "")
    movement = input()
