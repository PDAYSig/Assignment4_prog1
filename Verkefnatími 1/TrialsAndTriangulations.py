import math

a = int(input())
b = int(input())
c = int(input())

s = (a + b + c)/2

ans = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(round(ans, 9))