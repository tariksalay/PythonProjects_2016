def untranspose(message):
    wordlen = len(message)
    wordmid = wordlen / 2
    if wordlen % 2 == 1:
        wordmid += 1
    middle = int(wordmid)
    odd = message[:middle]
    even = message[middle:]
    wordfin = ""
    for i in range(wordlen):
        if (i + 1) % 2 == 1:
            wordfin += odd[int(i/2)]
        else:
            wordfin += even[int(i/2)]
    return wordfin  # Replace with code to untranspose the line.

def transpose(originalword):
    wordlen = len(originalword)
    odd = ""
    even = ""
    for i in range(wordlen):
        if (i + 1) % 2 == 1:
            odd += originalword[i]
        else:
            even += originalword[i]
    return  odd+even  #Replace code with valid code to transpose the line

def menu():
    while True:
        answer = input("Transposition Options \n 1. Encipher File \n  2.Decipher File \n Q. Quit")
        if (answer == "1" ) or (answer == "2") or (answer.lower() == "q"):
            return answer
        else:
            print("You must enter 1,2 or Q")


run = True
while run:
    UserInput = menu()

    if UserInput == "1":
        lines = ""
        try:
            filename = input("Enter the name of the file to Encipher ==>")
            # read all lines into lines as a list
            lines = open(filename, "r").readlines()

        except FileNotFoundError:
            print("Could not find the file specified.  Try another filename")
            filename = input("Enter the name of the file to Encipher ==>")
            lines = open(filename, "r").readlines()

        except IOError:
            print("General Error")

        if lines != "":

            # get the output file name
            outFileName = input("Enter the name of the file to write to ==>")
            outFile = open(outFileName, "w")

            # for each line, strip and transpose
            for line in lines:

                transposed = transpose(line.strip("\n"))
                transposed += "\n"
                # write the transposed line to new file
                outFile.write(transposed)
                print (line, transposed)

                #close output file after finishing.
                outFile.close()


    elif UserInput == "2":
        lines = ""
        try:
            filename = input("Enter the name of the file to Decode ==>")
            lines = open(filename, "r").readlines()

        except FileNotFoundError:
            print("Could not find the file specified.  Try another filename.")
            filename = input("Enter the name of the file to Decode ==>")
            lines = open(filename, "r").readlines()

        except IOError:
            print("General error")

        # read all lines into lines as a list
        if lines != "":
            # get the output file name
            outFileName = input("Enter the name of the file to write to ==>")
            outFile = open(outFileName, "w")

            # for each line, strip and transpose
            for line in lines:
                untransposed = untranspose(line.strip("\n"))
                untransposed += "\n"
                # write the transposed line to new file
            outFile.write(untransposed)

            #close output file after finishing.
            outFile.close()


    elif UserInput.lower() == "q":
        run = False

    else:
        print("You must enter 1, 2 or Q")
        print()
        UserInput = int(input("Transposition Options \n 1. Encipher File \n 2.Decipher File \n Q. Quit"))
