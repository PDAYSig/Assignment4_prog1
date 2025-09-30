movies = []

newOrder = [[], [], []]

movieNum = int(input())
numbers = input()

for x in numbers.split():
    movies.append(int(x))

while len(newOrder[0]) < (movieNum/3) and len(newOrder[2]) < (movieNum/3) and len(newOrder[1]) < (movieNum/3):
    for x in movies:
        if x == min(movies) and len(newOrder[0] < (movieNum/3)):
            newOrder[0].append(x)
            movies.remove(x)
        elif x == max(movies) and len(newOrder[2]) < (movieNum/3): 
            newOrder[2].append(x)
            movies.remove(x)
        

while len(newOrder[2]) < (movieNum/3):
    for x in movies:
        if x == max(movies): 
            newOrder[2].append(x)
            movies.remove(x)


while len(newOrder[1]) < (movieNum/3):
    for x in movies:
        if x == max(movies):
            newOrder[1].append(x)
            movies.remove(x)

for x in sorted(newOrder[1]):
    print(x, end=" ")

for x in sorted(newOrder[0]):
    print(x, end=" ")


for x in sorted(newOrder[2]):
    print(x, end=" ")






        

