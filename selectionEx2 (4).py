# Name: Charmi Kadi
# Date: May. 18, 2021
# Class: ICS3U1-01
# Description: Program that reads in a file name from the user and tells them what kind of file it is

# User input
file = str(input("Enter the file name: "))

# String slicing
period = file.find(".")
extension = str(file[period+1:])

# if statement
if extension == "png":
   print( file, "is a png file.") 
elif extension == "jpeg":
   print( file, "is a jpeg file.") 
elif extension == "doc":
   print( file, "is a Word Document.") 
elif extension == "gif":
   print( file, "is a GIF image file.") 
elif extension == "pdf":
   print( file, "is a Portable Document Format file.") 
   
