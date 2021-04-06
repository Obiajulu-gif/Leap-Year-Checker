#ask for the Users Year
year = int(input ("Which Year do you want to check?\n"))

#this Line of Code Divides and store the modules of the input
year4 = (year % 4)
year100 = (year % 100)
year400 = (year % 400)


#firstly, we check if it is divisble by 4
#inside it, we also check if it is divisble by 100
#inside it, we check if it is divisble by 400
#note it must be divisble by 4 and 400 else it is not a leap year
#note, it also keep going down if the condition is true
if year4 == 0:
    if year100 == 0:
        if year400 == 0:
            print ("Leap Year")
        else:
            print ("Not a Leap Year")
    
    else:
        print ("Leap Year")
    
else:
    print ("Not a Leap Year ")

#what i understand is that the odd condition should be at the middle of the code

