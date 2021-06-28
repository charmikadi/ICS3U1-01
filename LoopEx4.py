# Name: Charmi Kadi
# Date: June. 12, 2021
# Course Code: ICS3U1-01
# Description: Calculates the sum of digits in a number from user.



number = int(input("Please enter a number: "))

total = 0

while number > 0:
    digit = number % 10
    total +=  digit
    number = number //10

print("The sum of digits is", total)


























#number = int(input("Enter the number: "))

#for i number:
    #print(i)