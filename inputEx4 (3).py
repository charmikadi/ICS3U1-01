# Name: Charmi Kadi
# Date: Apr. 30, 2021
# Class: ICS3U1-01
# Description: Program that computes the distance between 2 points.  

# Input for coordinates of first point
x1val = int(input("Please enter the x-coordinate of first point. " ))
y1val = int(input("Please enter the y-coordinate of first point. " ))

# Input for coordinates of second point
x2val = int(input("Please enter the x-coordinate of second point. " ))
y2val = int(input("Please enter the y-coordinate of second point. " ))

# Using formula to calculate distance
dist = (((x2val-x1val)**2 + (y2val - y1val)**2)**0.5)

# Output that displays the distance between user's 2 points
print("The distance between given 2 points is", round(dist,2), "units.") 