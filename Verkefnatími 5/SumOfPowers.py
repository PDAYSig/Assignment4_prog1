k = int(input())
n = int(input())

total = 0
for i in range (1, n+1):
    x = int(input())
    total += k**x

print(total)

