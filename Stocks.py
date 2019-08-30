########################################################################
##
## CS 101
## Program #6
## Name : Tarik Salay
## Email : tshh2@mail.umkc.edu
## Creation Date : 4/10/2016
## Due Date : 4/10/2016
##
##
## PROBLEM : A program that asks the user tahat stock indexes they  want a history about, the date the stock was purchased, the date the stock was sold and how many  stocks were purchased.
##
## ALGORITHM : None.
##
## ERROR HANDLING: Many errors handling. I could not finish the program because of the other classes's exams and also CS101 exam 2. I am sorry about that, I'm uploading anyway with all I got.
##
##
## OTHER COMMENTS:
##
##
########################################################################

import csv
import datetime

run = True
while run:

    def get_stocklist():
        get_stocklist_file = open("stocklist.csv")
        get_stocklist_csv = csv.reader(get_stocklist_file)
        stocks = {}

    for date in range(purchasedate.strftime("%m/%d/%Y"), selldate.strftime("%m/%d/%Y")):
        for line in stocklist_csv:
            movies[line[0]] = float(line[2])

     return stocks

stocklist_file.close()

csvfilename = indexs()

with open(csvfilename, "r") as csvfile:
        csvfilereader = csv.reader(csvfile)
        dates = []
        sellingprices = []
        purchaseprices = []
        splitratios = []

        for rows in csvfilereader:
            dates = row[0]
            purchaseprice = row[1]
            sellingprice = row[4]
            splitratio = row[7]

            date.append(date)
            purchaseprice.append(purchaseprices)
            sellingprices.append(sellingprice)
            splitratios.append(splitratio)

        csvfile.close()

        def get_stock(stock : dict) -> dict:
            """ Returns a dictionary of stocks """
        stock_file = open("x.csv")
        stock_csv = csv.reader(stock_file)

        stock = {}
        # Iterate over file and append to list
        for line in stock_csv:
            date = line[0]

            if stock_name in stock:
                stock[stock_name].append(stock)
            else:
                stock[stock_name] = []
                stock[stock_name].append(stock)

        stock_file.close()

        #return stock

        def verifydate():
            if purchasedate > selldate:
                print("Invalid input. Purchase date can not be greater than the sell date")
                selldate = input("Enter the date you sold the stock ==>")

            if type(numberofstocks) != int or numberofstocks < 0:
                print("The number  must be an integer and greater than 0.")
                numberofstocks = input("How many stocks were purchased on start date ==>")

        stockname = input("Enter the name of the stock purchased.  Enter quit to exit ==>")
        if stockname == "quit":
            run = False
        else:
            stockname = input("Enter the name of the stock purchased.  Enter quit to exit ==>")

        purchasedate = input("Enter the stock purchase date ==>")(verifydate)
        selldate = input("Enter the date you sold the stock ==>")(verifydate)
        try :
                print("Could not find the stock .  Please enter another")
        except FileNotFoundError:
                selldate = input("Enter the date you sold the stock ==>")(verifydate)
                purchasedate = input("Enter the stock purchase date ==>")
        numberofstocks = input("How many stocks were purchased on start date ==>")(verifydate)


        # Create dictionary of stocks
        stocklist_dict = get_stocklist()

        stock_dict = get_stock(get_stocklist)

        my_date = datetime.datetime.strptime(invalid_date1, "%m/%d/%Y")

        for key, value in stock_dict.items():
            print("{:<15}{:>15.1f}{:>15.1f}{:>15.2f}".format(key, min(value), mid(value), max(value), mydate ))
