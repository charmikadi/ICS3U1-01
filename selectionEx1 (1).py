# Name: Charmi Kadi
# Date: May. 18, 2021
# Class: ICS3U1-01
# Description: Program that gets the base price of a meal and outputs the total.

#  Constants 
HIGHTAX = 0.13
LOWTAX = 0.08
LIMIT = 4

# Input from the user
price = float(input("Enter price of the meal: ")) 

# Custom tax based on price of meal
if price > LIMIT :
    tax = HIGHTAX
    
else:
    tax = LOWTAX

# Calculate the total price
meal = (tax+1)*price 

# Output that displays receipt 
print("McD's Receipt")
print("-------------")
print("Meal      $%5.2f" % price)
print("          ------")
print("Tax (13"+"%"+")", "$%5.2f" % (price*tax))
print("          ------")
print("Total     $%5.2f" % meal)
