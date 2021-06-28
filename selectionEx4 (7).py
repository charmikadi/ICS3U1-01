# Name: Charmi Kadi
# Date: May. 18, 2021
# Class: ICS3U1-01
# Description: Program that outputs the relationship between the area and perimeter of a rectangle.

# User input
dimensions = str(input("Enter the dimensions of the rectangle (length, width): "))
comma = dimensions.find(",")

# Breaking down the length and width 
length = int(dimensions[:comma])
width = int(dimensions[comma+1:])

# Calculating area and perimeter of rectangle
area = length*width
perim = 2*length + 2*width

# if statement
if area > perim:
    print("Area is greater than perimeter of rectangle.")
elif area < perim:
    print("Area is less than perimeter of rectangle.")
else:
    print("Area is equal to the perimeter of rectangle.")