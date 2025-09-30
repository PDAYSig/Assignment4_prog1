sec = int(input())

min = sec//60
sec = sec%60

hrs = min//60
min = min%60

print(hrs, ":", min, ":", sec)