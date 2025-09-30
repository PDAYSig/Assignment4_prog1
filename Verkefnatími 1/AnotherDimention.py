import math
#Hönnun (Guðmundur): Reikna flatamál hálfkúlu (half-sphere). Nota formúluna 
#V = 4/3*pi*r**3  . Sem er formula flatarmáls kúlu (sphere). 
# Input væri ein lína: float talan d  sem er þvermál (diameter) af kúlunni (sphere) 
# þar sem d er stærra eða jafnt og 0, minna eða jafnt og 1000. Í mesta lagi tveir aukastafir. 
# Input væri Ein lína: float tala sem er flatarmál af hálfri kúlu (Half-sphere) Outputið verður að hafa
# absolute error eða relative error ef tala nær í 10-9 .
#  Aukastafir í output skipta ekki máli.

d = float(input()) #diameter
r = d/2 #radius (half the diameter)

v = ((4/3)*math.pi*math.pow(r,3))/2 #volume of a sphere divided by 2 for half-sphere

print(round(v, 9)) #print the result

