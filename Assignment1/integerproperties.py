ans = input("")


#Function to check if x is a divisor of num
def isDivisor(num, x):
    if (num % x) == 0:
        return True
    else:
        return False
    
#Function to calculate a digit sum that returns the correct value depending on whether the digit is a 2- or 3-digit number.   
def digitSumCalc(digit): 
    digitAsString = str(digit)

    lastX = 0
    for x in digitAsString:
        x = int(x)
        lastX += x
    if len(digitAsString) == 2:
        return (lastX ** 2)
    elif len(digitAsString) == 3:
        return (lastX ** 3)
        
#The loop for checking if a given number has 10 or more divisors
while ans != "q" and ans != "Q":
    num = int(ans)
    divisorCount = 0

    for x in range(1, num + 1):
        if isDivisor(num, x):
            divisorCount += 1
        
        if divisorCount >= 10:
            print("yes")
            break
    
    if divisorCount < 10:
        print("no")
    
    ans = input("")

'''statement that checks the digit sums of a given number and prints the two digit ones whose digit sum squared is equal
to the number and the three digit ones whose digit sum cubed is equal to the number'''

if ans == "q" or ans == "Q":
    num = int(input())
    for x in range(1, num + 1):
        if (digitSumCalc(x)) == x:
            print(x)

