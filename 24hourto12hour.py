print("Please enter a 24 hour time:")
hour24 = int(input("hour: "))
minutes24 = int(input("minutes: "))

minutes12 = minutes24   
if(0<=hour24<=11):
    period = "AM"

    if(hour24 == 0):
        hour12 = 12

    else:
        hour12 = hour24

else:
    period="PM"
    if(hour24 == 12):
        hour12 = 12
    else:
        hour12 = hour24 - 12

print(hour24,":", minutes24, " is equal to ", hour12,":", minutes12, period, sep="")