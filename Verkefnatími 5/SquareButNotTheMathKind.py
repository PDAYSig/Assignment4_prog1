sides = int(input())

print("* " * (sides - 1), "*", sep= "")

for x in range (1, sides - 1):
    print("*", end= " ")
    for x in range (1, sides - 1):
        print(" ", end= " ")
    print("*")

if sides != 1:
    print("* " * (sides - 1), "*", sep= "")
