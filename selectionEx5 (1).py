# Name: Charmi Kadi
# Date: May. 17, 2021
# Class: ICS3U1-01
# Description: Program that tells the minimum area needed for the base of python's enclosure.

# Constants
REMA = 0.75
MINIMUM = 0.5
FEET = 6
EXPON = 0.5

# User input
length = int(input("Enter how long your python is: "))
             
# if statement 
if length > FEET:
    area = FEET*EXPON + (length - FEET)*REMA
elif length < FEET:
    area = length*EXPON
else:
    area = FEET*EXPON
    
# Print statement
print(str(length) + "' python needs", area, "square feet.")
    