r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

if(r == g and r == b):
    if(r == 0):
        print("svartur")
    elif(r == 255):
        print("hvitur")
    else:
        print("grar")


elif(r > g and r > b):
    print("raudur")

elif(g > r and g > b):
    print("graenn")

elif(b > r and b > g):
    print("blar")

elif(r == g and r > b):
    print("gulur")

elif(r == b and r > g):
    print("fjolubleikur")

elif(b == g and b > r):
    print("blagraenn")

else:
    print("othekkt")