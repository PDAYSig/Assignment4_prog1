x = int(input())
n = int(input())

mbUsed = 0

for i in range (1, n+1):
    mbUsed += int(input())

mbLeft = x * (n+1) - mbUsed

print(mbLeft)