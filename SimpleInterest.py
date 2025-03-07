
#Program for calculating simple interest
Principle=float(input("Enter principle amount"))
if Principle>0:
    Rate=float(input("Enter the Rate of interest"))
    if Rate>0:
        Time=float(input("Enter the time"))
        if Time>0:
            SimpleInterest=(Principle*Rate*Time)/100 #calculating simple interest
            print("Simple Interest is",SimpleInterest)
else:
    print("All entries should be positive")
