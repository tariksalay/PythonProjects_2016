import random
import string

hints = True
run = True 

while run:

    print("Welcome to the game of Slice!")

    RoundAmount = int(input("How many rounds do you want to play? 1-20"))
    while RoundAmount < 1 or RoundAmount > 20: 
        print("You must enter a number between 1 and 20")
        print()
        RoundAmount = input("How many rounds do you want to play? 1-20")

    difficulty = int(input("How easy of a string? 1. Easy, 2. Medium, 3. Hard"))
    while difficulty < 1 or difficulty > 3:
        print("You must choose 1, 2, or 3.")
        difficulty = int(input("How easy of a string? 1. Easy, 2. Medium, 3.Hard"))
    print()

    hint = input("Do you want hint indexes? (Y/YES/N/NO) ==>").upper()
    if hint == "Y" or hint == "YES":
                hints = True
    elif hint == "N" or hint == "NO":
                hints = False
    else:
                print("You must enter Y, YES, N or NO.")
                print()
                hint = input("Do you want hint indexes? (Y/YES/N/NO) ==>").upper()

    correct = 0

    for round in range (RoundAmount):

        print()

        if difficulty == 1:
            cnt=1
            length = 5
            word = random.choice(string.ascii_letters)
            while cnt < length:
                word += random.choice(string.ascii_letters)
                cnt += 1

            halflenword = int(len(word)/2)
            lenofword = len(word)
            startslice = random.randint(0, halflenword)
            endslice = random.randint(halflenword+1, lenofword-1)
            stepsize = 1

            if stepsize == 1:
                stepsize = ":"

            slice = "[{},{},{}]".format(startslice,endslice,stepsize)

            if hints:
                print("{:>26}\n{:>26}".format("01234","-54321"))

            wordquestion = input("What is the slice of "+ word+ slice)

            if wordquestion == word[startslice:endslice]:
                print("Correct, the word was", word[startslice:endslice])
                print()
                correct += 1
            else:
                print("Wrong, the word was", word[startslice:endslice])
                print()

        elif difficulty == 2:

            cnt = 1
            length = 7
            word = random.choice(string.ascii_letters)
            while cnt < length:
                word += random.choice(string.ascii_letters)
                cnt += 1

            halflenword = int(len(word)/2)
            lenofword = len(word)
            startslice = random.randint(0, halflenword)
            endslice = random.randint(halflenword+1, lenofword-1)
            stepsize = 1

            if stepsize == 1:
                stepsize = ":"

            slice = "[{},{},{}]".format(startslice,endslice,stepsize)

            if hints:
                print("{:>28}\n{:>28}".format("0123456","-7654321"))

            wordquestion = input("What is the slice of "+ word+ slice)

            if wordquestion == word[startslice:endslice]:
                print("Correct, the word was", word[startslice:endslice])
                print()
                correct += 1
            else:
                print("Wrong, the word was", word[startslice:endslice])
                print()

        elif difficulty == 3:

            cnt = 1
            length = 10
            word = random.choice(string.ascii_letters)
            while cnt < length:
                word += random.choice(string.ascii_letters)
                cnt += 1

            halflenword = int(len(word)/2)
            lenofword = len(word)

            startposs = random.randint(0,20)
            if startposs in range(0,5):
                startslice = random.randint(-(halflenword), halflenword)
            else:
                startslice = random.randint(0, halflenword)

            endposs = random.randint(0,20)
            if endposs in range(0,5):
                endslice = random.randint(-(halflenword+1), -(lenofword-1))
            else:
                endslice = random.randint(halflenword+1, lenofword-1)

            reverseposs = random.randint(0,20)
            if reverseposs in range(0,5):
                reverseslice = -1
            elif reverseposs in range (0,4):
                reverseslice = random.randint(-2,2)
            else:
                reverseslice = 1

            slice = "[{},{},:{}]".format(startslice,endslice,reverseslice)

            if hints:
                print("{:>31}\n{:>31}".format("0123456789","-0987654321"))

            wordquestion = input("What is the slice of "+ word+ slice)

            if wordquestion == word[startslice:endslice:reverseslice]:
                print("Correct, the word was", word[startslice:endslice:reverseslice])
                print()
                correct += 1
            else:
                print("Wrong, the word was", word[startslice:endslice:reverseslice])
                print()

    print()
    percentage = (correct/RoundAmount)*100
    print("You got",correct,"of",RoundAmount,"which is %",percentage)

    while True:
            print()
            replay = input("Do you want to run again? (Y/YES/N/NO) ==> ").upper()
            if replay == "Y" or replay == "YES":
                print()
                break
            elif replay == "N" or replay == "NO":
                run = False
                break
            else:
                print("You must enter Y, YES, N or NO.")
                print()

    print("Thanks for playing!")
    print()
