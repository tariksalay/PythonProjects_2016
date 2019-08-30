########################################################################
##
## CS 101
## Program #1
## Name : Tarik Salay
## Email : tshh2@mail.umkc.edu
## Creation Date : 1/29/2016
## Due Date : 1/31/2016
##
##
## PROBLEM : This program is created to show you that how long is your drone going to fly, with the drone's information that given.
##
## ALGORITHM : 
##      1. By asking several question, I will get input for the variables to use them upcoming steps.
##      2. Then I will convert that variable units like time(hour to min and min to sec.) or ampere to miliamperes
##      3. Making calculations to get flight time and to see how many amps that drone is going to use.
##      4. Defining new variables to use them in the codes in the results step, inside the other codes.
##      5. Letting the user know that calculation finished.
##      6. Lastly, the program will give the results to the user after calculations with print string.
##      
##
## ERROR HANDLING: None.
##      
##
## OTHER COMMENTS: It is my first semester in the university, so I am sorry if I did some mistakes in the using English, Mr.Bingham.
##      
##
########################################################################

##Explain what input you will get from the user, how the input will be
##transformed or results produced, and what sort of output the user can expect.
##Also include a quick discussion of any error handling. 

#First Part : Asking questions to get input, all of this part have int at the beginning to get integer part in the case of user put the number with remainder. To get integer part of the number. And also this is part to define.
mAh = int(input("What is the mAh value on your battery ?")) #To define mAh variable and get input.
NumberOfMotors = int(input("How many motors does Drone have ?"))#To define NumberOfMotors variable and get input.
PerMotor = int(input("What is the Amps amount that drawn per motor? "))#To define PerMotor variable and get input from the question.

#Calculation Part : First of all,what program need to do is converting units. Amps = mAh/100, Sec = Min*60, Min = Hour*60 etc. And then calculate the flight times with the formula that you gave which is Amps = Motors * Amps drawn per motor and the fligh time is Ah divided by total amps.
AmountOfAmps = NumberOfMotors*PerMotor #To calculate amount of Amps we need multiplication of number of motors and amps that drawn per motor
FlightTimeInMin = (mAh/1000)/AmountOfAmps*60 #To get Amps we need to divide mAh by 1000. Then we will divide it the amps amount to find flight time in hour, because of we need to find it in minutes, what program is going to do is multiply it with 60.
FlightTimeInSec = (FlightTimeInMin*60) #To get flight time in sec, we need to multiply it with 60 again. We will use this part in the next codes.
Min = int(FlightTimeInMin) #To get integer part of the result, I wrote this code.
Sec = int(FlightTimeInSec)%60 #Now, we are using the InSec code here. I used "%" to see what is the remainder from this calculation and I will use it in the last part to show that how many seconds it has. Remained part of the number. That part was the hardest one for me until I think of using '%'.

#Last Part : All the last part is with "print" string because we are going to tell the results to the user.
print("Calculation has ended!") #To let user know.
print("\n") #To show the program sightly and regular.
print("Results") #To inform the user.
print("Your drone is going to use", AmountOfAmps, "Amps"): #I need to use "" two times at the beginning and finish because of the AmountOfAmps variable and I seperated it with commas to make code run without error.
print("The total flight time is", FlightTimeInMin, "minutes")# I need to seperate the variable named FlightTimeInMin between commas to get no error in print string.
print("Which is", Min, "minutes and", Sec, "seconds")#Here I need to do it three times because I had two different variables.
