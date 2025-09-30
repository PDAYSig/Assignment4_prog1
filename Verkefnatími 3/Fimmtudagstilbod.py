year = int(input())
price = 1000

yrSince = year - 2020

if (yrSince > 0):
    price = yrSince * 100 + 1000

print(price)
