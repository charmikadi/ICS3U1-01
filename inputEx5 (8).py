# Name: Charmi Kadi
# Date: Apr. 30, 2021
# Class: ICS3U1-01
# Description: Program that will output the number of slices each person receives.

# Number of pizza slices 
piece = 32
# User's input for the number of party attendees
guest = int(input ("Please enter the number of guests. "))

# Option 1 is everyone receives the same number of slices ignoring extra piece
opt1 = piece // guest
rema = piece % guest 

# Option 2 with everyone receiving same number of slices
opt2 = piece/guest

# Output that displays the number of slices each guest will receive
print("Number of guests:", guest)
print("Option 1:", opt1, "slices each,", rema, "left over.") 
print("Option 2:", opt2, "slices each.")

