import sys

stitches = {
    ".":20,
    "o":10,
    "\\":25,
    "/":25,
    "A":35,
    "^":5,
    "v":22
}

num = input()

length, width = num.split()
length = int(length)
width = int(width)

recipe = input()

totalYarn = 0
for line in recipe.split("\n"):
    for i in line:
        if i in stitches:
            addYarn = stitches[i]
            totalYarn += addYarn
            


print(totalYarn)

        

