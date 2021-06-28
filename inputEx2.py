# Name: Charmi Kadi
# Date: Apr. 30, 2021
# Class: ICS3U1-01
# Description: Program that converts Canadian dollar amount to Euros.

# User's input of Canadian amount
amou = int (input ("Please enter the Canadian amount. "))

# Conversion from Canadian to Euros
euro = amou*0.6718995

# Output that displays the worth of Canadian amount in Euros
print("Your amount of", amou, "Canadian dollars is worth", round(euro,2), "in Euros.")