from PIL import Image #To convert jpg files

#I did the extra part's coding as it is explained on the internet. Even if I worked hard on it, still I am not so sure.

def grayscale_look(fname, outname):
    image = Image.open(fname)
    x, y = image.size  #  image.size in (x, y) type
    pixels = image.load()

    for i in range(x):
        for j in range(y):
            r,g,b =  pixels[i,j]
            gray = (r * 0.299) + (g * 0.587) + (b *  0.114)
            gray = int(gray)
            pixels[i,j] = (gray,gray,gray)

    image.save(outname)

def vintage_look(fname, outname):
    image = Image.open(fname)
    x, y = image.size  #  image.size in (x, y) type
    pixels = image.load()

    for i in range(x):
        for j in range(y):
            r,g,b =  pixels[i,j]
            pixels[i,j] = (r,g, int(b/2))

    image.save(outname)

def grayscale(picture):
    outp = [] #blank at first, we are going to append it
    for i in range(3): # 0,1,2 which are the first three line of ppm file (header)
        outp.append(picture[i])

    numpixels = int((len(picture) - 3) / 3) #numbers of pixels ( total - header)
    for val in range(numpixels):
        r = int(picture[ 3 + (3 * val)]) * 0.299 #the first line of group of three
        g = int(picture[ 3 + (3 * val) + 1]) * 0.587 #second line of the group
        b = int(picture[ 3 + (3 * val) + 2]) * 0.114 #every third line of the group
        gray = int(r + g + b)
        outp.append(gray)
        outp.append(gray)
        outp.append(gray)
    return outp

def vintage(picture):
    outp = []
    for i in range(3):
        outp.append(picture[i])

    numpixels = int((len(picture) - 3) / 3)
    for val in range(numpixels):
        r = int(picture[ 3 + (3 * val)])
        g = int(picture[ 3 + (3 * val) + 1])
        b = int((picture[ 3 + (3 * val) + 2]) /2)
        outp.append(r)
        outp.append(g)
        outp.append(b)
    return outp

def menu():
    while True:
        answer = input("Image Filters \n 1.Convert Image to GrayScale \n  2.Convert Image to Vintage \n 3.Convert Jpg to GrayScale \n 4.Convert Jpg to Vintage \n Q. Quit")
        if (answer == "1" ) or (answer == "2") or (answer == "q") or (answer == "Q"):
            return answer
        else:
            print("You must enter 1,2 or Q")


run = True
while run:
    UserInput = menu()
    lines = []
    if UserInput == "1":

        try:
            filename = input("Enter a valid filename to convert. ==>")
            header = open(filename, "r")
            firstline = header.readline().strip("\n") #to get first line
            secondline = header.readline().strip("\n") #to get second line
            thirdline = header.readline().strip("\n") #to get third line. I was also able to use for i in range(3), but I liked his way more.
            if firstline != "P3":#to see if it is ppm file or not
                print("The files first line should be P3")
            elif thirdline != "255":
                print("The color depth must be 255")
            lines = open(filename, "r").readlines()
            gray = grayscale(lines)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            for line in gray:
                f.write(str(line)+"\n")
            f.close()

        except FileNotFoundError:
            print("The file you specified does not exist.  Please enter a valid filename")
            filename = input("Enter a valid filename to convert. ==>")
            header = open(filename, "r")
            firstline = header.readline().strip("\n")
            secondline = header.readline().strip("\n")
            thirdline = header.readline().strip("\n")
            if firstline != "P3":
                print("The files first line should be P3")
            elif thirdline != "255":
                print("The color depth must be 255")
            lines = open(filename, "r").readlines()
            gray = grayscale(lines)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            for line in gray:
                f.write(str(line)+"\n")
            f.close()

        print()
        print("Your file has been saved.")
        print()

    elif UserInput == "2":

        try:
            filename = input("Enter a valid filename to convert. ==>")
            header = open(filename, "r")
            firstline = header.readline().strip("\n")
            secondline = header.readline().strip("\n")
            thirdline = header.readline().strip("\n")
            if firstline != "P3":
                print("The files first line should be P3")
            elif thirdline != "255":
                print("The color depth must be 255")
            lines = open(filename, "r").readlines()
            v = vintage(lines)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            for line in v:
                f.write(str(line)+"\n")
            f.close()

        except FileNotFoundError:
            filename = input("Enter a valid filename to convert. ==>")
            header = open(filename, "r")
            firstline = header.readline().strip("\n")
            secondline = header.readline().strip("\n")
            thirdline = header.readline().strip("\n")
            if firstline != "P3":
                print("The files first line should be P3")
            elif thirdline != "255":
                print("The color depth must be 255")
            lines = open(filename, "r").readlines()
            v = vintage(lines)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            for line in v:
                f.write(str(line)+"\n")
            f.close()

        print()
        print("Your file has been saved.")
        print()

    elif UserInput == "3":

        try:
            filename = input("Enter a valid filename to convert. ==>")
            lines = open(filename, "r").readlines()
            gray = grayscale_look(filename, outfname)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            f.close()

        except FileNotFoundError:
            print("The file you specified does not exist.  Please enter a valid filename")
            filename = input("Enter a valid filename to convert. ==>")
            lines = open(filename, "r").readlines()
            gray = grayscale_look(filename, outfname)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            f.close()

        print()
        print("Your file has been saved.")
        print()


    elif UserInput == "4":

        try:
            filename = input("Enter a valid filename to convert. ==>")
            lines = open(filename, "r").readlines()
            vinpic = vintage_look(filename, outfname)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            f.close()

        except FileNotFoundError:
            print("The file you specified does not exist.  Please enter a valid filename")
            filename = input("Enter a valid filename to convert. ==>")
            lines = open(filename, "r").readlines()
            vinpic = vintage_look(filename, outfname)
            outfname = input("What is the name of the file you want to save to? ==>")
            f = open(outfname,"w")
            f.close()

        print()
        print("Your file has been saved.")
        print()


    elif UserInput.lower() == "q":
        run = False

    else:
        print("You must enter 1, 2 or Q")
        print()
        UserInput = input("Image Filters \n 1.Convert Image to GrayScale \n  2.Convert Image to Vintage \n 3.Convert Jpg to GrayScale \n 4.Convert Jpg to Vintage \n Q. Quit")
