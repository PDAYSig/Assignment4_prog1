import math

n = int(input())
counter = 2
isPrime = True


if n != 1:
    while counter <= math.sqrt(n):
        if n%counter == 0:
            isPrime = False
            break

        counter+=1

    if isPrime:
        print("prime")

    else:
        print("not prime")

else:
    print("not prime")