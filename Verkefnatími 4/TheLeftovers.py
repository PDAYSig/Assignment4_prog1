numberOfPlyrs = int(input())

while numberOfPlyrs < 2:
    numberOfPlyrs = int(input())

total = 0
for x in range(1, numberOfPlyrs + 1):
    total += int(input())

winner = total % numberOfPlyrs

print("The sum of all contributions is ", total, "\nWhen ", total, " is divided by ", numberOfPlyrs,
      ", the remainder is ", winner, "\nPlayer ", winner, " is the winner!", sep="")