logNum = int(input())

inside = set()


for x in range(logNum):
    movement, name = input().split()
    if movement == "entry": 
        if name not in inside:
            inside.add(name)
            print(name, "entered")
        else:
            print(print(name, "entered (ANOMALY)"))
    
    elif movement == "exit":
        if name in inside:
            inside.remove(name)
            print(name, "exited")
        else:
            print(name, "exited (ANOMALY)")


    