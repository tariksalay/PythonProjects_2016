########################################################################
##
## CS 101
## Program #8
## Name : Tarik Salay
## Email : tshh2@mail.umkc.edu
## Creation Date : 4/8/2016
## Due Date : 5/8/2016
##
##
## PROBLEM : Simple simulation of tourist that using the tram to go from one lot to  another. 
##
## ALGORITHM : Already sent.
##      
## ERROR HANDLING: None.
##      
##
## OTHER COMMENTS: None.
##      
##
########################################################################

import random
import sys

def randstart(num_lots):
    if num_lots == 1: # To let user know lot number have to more than one
        print("This simulation requires more than one lot")
        return None, None
    if num_lots == 2: # In case if user put 2 for number of lots
        start = random.randint(0,2)
        if start == 0:
            dest = 1
        else:
            dest = 0
        return start, dest
    start = random.randint(0, num_lots-1) # To get random start point
    dest = random.randint(0, num_lots-1) # To get random destination
    if start == dest: # If start point is same with the destination, then get new ones.
        x, dest = randstart(num_lots-1)
    return start, dest

class ParkingLot:
    def __init__(self, lot_number):
        self.lot_number = lot_number
        self.wait_list = [] # To make tourist's list who are waiting

    def __str__(self): 
        return "L{}({})".format(self.lot_number, len(self.wait_list)) # To show at which lot and waiter tourist's number

    def __repr__(self):
        return "This is  parking lot {}".format(self.lot_number) # To show at which parking lot it is

    def register_tourist(self, tourist): # To register tourists to our waiter list
        self.wait_list.append(tourist)
        
    def report(self):
        arrived = 0
        waiting = 0
        for t in self.wait_list:
            if t.arrived  == True:
                arrived  += 1
            else:
                waiting  += 1

    def get_on_tram(self, tram): 
        templist = []
        for tourist in self.wait_list:
            if tourist.arrived == False: # To discard tourist that already have been reached their destinations.
                trd = tourist.direction()
                if tram.direction  == trd:
                    tram.get_on(tourist)
                    #self.wait_list.remove(tourist) #If tourist already got on tram, we need to remove him from our waiter list.
                else:
                    templist.append(tourist)
        self.wait_list = templist
        self.report()

class Park:
    def __init__(self, lots = 2 , tourist_num = 0):
        if lots < 2:
            print("This simulation requires more than one lot") # To let user know
            sys.exit()
        self.lots_total = lots
        self.lots = {}

        for i in range(lots):
            self.lots[i] = ParkingLot(i) # To generate parking lots by the loop

        self.tourists = [] 
        for i in range(tourist_num):
            start, dest = randstart(self.lots_total)
            t = Tourist(start, dest)
            self.tourists.append(t) # To fill our tourist list
            self.lots[start].register_tourist(t)
            
        self.tram = Tram(0, self.lots)

    def print_state(self):
        temp = ""
        for i in range(self.lots_total):
            temp += "{:<7} ==".format(str(self.lots[i])) # To make tram move
        print(temp[:-3])
        print((" " * ((self.tram.current_lot * 10) + 2) + "|")) # To show tram's position
        print((" " * ((self.tram.current_lot * 10) + 2) + str(self.tram))) # To show tram's position
        print()

        self.lots[self.tram.current_lot].report()

    def step(self):
        self.tram.move()
        
    def simulate(self):
        exiting = False
        while exiting is False:
            ans = input("Enter Q to quit")
            if ans.lower() == "q": # In case of user put q or Q
                sys.exit()
            else:
                self.print_state()
                self.step()
            

    def __str__(self):
        return "Park with {} lots and {} tourists".format(self.lots_total, len(self.tourists)) # To inform user
        
    def report(self):
        for lot_num, plot in self.lots.items(): # To inform user
            print(str(plot))


class Tram:
    def __init__(self, current_lot, lots):
        self.lots = lots
        self.current_lot = current_lot
        self.direction = 1 # Go forward
        if self.current_lot == 0:
            self.direction = 1 # Keep going
        elif self.current_lot == len(self.lots):
            self.direction = -1 # Go backward

        self.tourists = []

    def __str__(self):
        if self.direction == 1:
            return "T({})>".format(len(self.tourists)) # If direction is 1 it means, tram is going forward
        else: # Else, tram is going backward, I could basically write  elif self.direction == -1: , both are same
            return "<T({})".format(len(self.tourists))

        
    def get_on(self, tourist): # To get tourist on the tram, append them to list
        self.tourists.append(tourist)

    def get_off(self): # To drop off at the current lot, tourist who are arrived their destination
        for tourist in self.tourists:
            if tourist.destination == self.current_lot: 
                tourist.set_arrived() # To set tourist which are arrived as arrived
                self.lots[self.current_lot].register_tourist(tourist) 
                print(tourist.arrived)
                self.tourists.remove(tourist) # If arrived, remove it from list to make them don't get on again to tram
        
    def move(self):
        old_count = len(self.tourists)
        self.lots[self.current_lot].get_on_tram(self)
        get_on_count = len(self.tourists) - old_count # To see how many tourist picked up
        self.get_off()
        get_off_count = (old_count + get_on_count) - len(self.tourists) # To calculate how many tourist dropped off
        print("Tram dropped off {} Passengers at Lot {}".format(get_off_count, self.current_lot))
        print("Tram picked up {} Passengers at Lot {}".format(get_on_count, self.current_lot))
        if self.current_lot == len(self.lots) - 1 : # If the tram at the last lot(index -1)
            self.direction = -1 # It will go backward
            self.current_lot = len(self.lots) - 2 # It the tram at the last lot, go to the previous one before the last one.
        elif self.current_lot == 0: # If the tram at the first lot ( index 0 )
            self.direction = 1 # It will go forward
            self.current_lot = 1 # Next destination will be index 1 which is the next lot
        else:
            self.current_lot += self.direction # Goes to next stop, using direction.

        

class Tourist:
    def __init__(self, start_lot, dest_lot):
        self.start = start_lot
        self.destination = dest_lot
        self.arrived = False

    def __str__(self):
        return "Tourist travelling from Lot {} to Lot {} ".format(self.start, self.destination) # To inform user

    def direction(self):
        if self.start < self.destination: # To see which direction tourist wants to go (Next stations or the previous ones)
            return 1 # If start point is before than destination, go forward
        else:
            return -1 # If tourist wants go back (destination number is bigger than start point), go backward

    def set_arrived(self):
        self.arrived = True

numOfLots=0 # At first, it is going to change after input
numOfTourist=0 # It will change too after getting input from user
proper = False

while not proper: # If it is not a proper input

    try:
        numOfLots = int(input("Enter the number of lots in the simulations ==> ")) 

        if numOfLots > 11 or numOfLots < 2 : # To warn user
            print(" Number of lots must be greater or equal to 2, and less than or equal to 11 ") # To warn user
            proper = False
        else:
            numOfTourist = int(input("Enter the number of tourists waiting on trams. ==>"))
            if numOfTourist < 0 or numOfTourist > 20: # To warn user
                print(" Number of tourists must be greater or equal to 0, and less than or equal to 20 ") # To warn user
                proper = False
            else:
                proper = True

    except ValueError: # In case of user put float number
        print("Both of the number of lots and tourists must be an integer")
        proper = False

p = Park(numOfLots,numOfTourist) # To make program run
p.simulate() # To make program run
