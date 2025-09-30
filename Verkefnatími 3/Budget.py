total = int(input())

a = int(input())
b = int(input())
c = int(input())

abc = a + b + c

num = total - abc

if(num < total):
    print("Budget is sufficient.")
else:
    print("Budget is insufficient.")

