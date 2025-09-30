a = int(input())
b = int(input())

while b != 0:
    temp = a % b
    a = b
    b = temp

print(a)
