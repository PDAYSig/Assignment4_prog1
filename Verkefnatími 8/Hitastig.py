heat = []

days = int(input())

degrees = input()



for x in degrees.split(" "):
    x = int(x)
    heat.append(x)

topHeat = max(heat)
lowHeat = min(heat)

print(topHeat, lowHeat)

