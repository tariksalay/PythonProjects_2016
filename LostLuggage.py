run = True
details = True

while run:

    import random

    r = int(input("How many rounds do you want to run lost luggage ?"))
    while r <= 0:
            print("You must enter a value greater than 0")
            r = int(input("How many rounds do you want to run lost luggage ?"))
    if r > 1000:
            Output = input("Do you want to output the details Y/YES/N/NO ?")
            if Output.lower() == "y" or Output.lower() == "yes":
                 details = True
            elif print("You must enter Y, YES, N or NO"):
                Output = input("Do you want to output the details Y/YES/N/NO ?")
            else:
                 details = False

        
    cnt = 0
    ontime = 0
    maxhops = 0
    while cnt < r:
            hops = 0
            cnt += 1 
            lug = random.choice(["SEA", "LVS", "HNL", "MCI"])
            lug = "MCI"
            if details:
                print("Trial", cnt, lug, end="")
            while lug != "HNL":
                if lug == "MCI":
                    randomx = random.randint(1,10)
                    hops += 1  
                    if randomx in range(1,4):
                        lug = "LVS"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(4,7):
                        lug = "SEA"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(7,10):
                        lug = "HNL"
                        if details:
                            print("->", lug, end="")
                if lug == "LVS":
                    randomx = random.randint(1,10)
                    hops += 1  
                    if randomx in range(1,5):
                        lug = "SEA"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(5,8):
                        lug = "MCI"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(8,10):
                        lug = "HNL"
                        if details:
                            print("->", lug, end="")
                if lug == "SEA":
                    randomx = random.randint(1,10)
                    hops += 1
                    if randomx in range(1,6):
                        lug = "LVS"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(6,7):
                        lug = "MCI"
                        if details:
                            print("->", lug, end="")
                    elif randomx in range(7,10):
                        lug = "HNL"
                        if details:
                            print("->", lug, end="")
            print()

            if hops > maxhops:
                maxhops = hops
            if hops <= 2:
                ontime += 1        
            timepercentage = (ontime/cnt)*100

            
    print("\n")
    print("The baggage was on time", "%", timepercentage, "of the time.", (ontime, cnt))
    print("The max hops that occured was", maxhops)
    print("\n")
    
    replay = input("Do you want to run again? , Y/YES/N/NO")
    if replay.lower() == "y" or replay.lower() == "yes":
            run = True
    else:
            run = False
