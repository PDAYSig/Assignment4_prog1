#Patrik Dagur Sigurðsson
#Verkefnatími 1
#Computer Compute
import math

x1 = float(input()) #Input X coordinate for point 1:
y1 = float(input()) #Input y coordinate for point 1:

x2 = float(input()) #Input X coordinate for point 2:
y2 = float(input()) #Input X coordinate for point 2: 

length = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2)) 

print(round(length, 9))


