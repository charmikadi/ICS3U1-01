# Name: Charmi Kadi
# Date: May. 18, 2021
# Class: ICS3U1-01
# Description: Program that tells the user how much postage will cost.

# User input
location = str(input("Enter the mailing location: "))

# If statement
if location == "Canada":
    postage = 0.52
elif location == "USA" or location == "United States":
    postage = 0.93
else:
    postage = 1.55
    
# Print statement that displays postage price
print("Please pay the postage rate of $%.2f." % postage)