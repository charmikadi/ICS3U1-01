# Name: Charmi Kadi
# Date: June. 12, 2021
# Course Code: ICS3U1-01
# Description: Finds sum of all numbers between user's input for 2 numbers. 

# 2 numbers from user input
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

count = 0 
for i in range(number1, number2+1):
    count+= i
print(count)