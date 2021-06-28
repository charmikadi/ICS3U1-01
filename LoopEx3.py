# Name: Charmi Kadi
# Date: June. 12, 2021
# Course Code: ICS3U1-01
# Description: Calculates the average age of the user's family members.

count = 0
check = 0
while True: 
    age = int(input("Enter the age of family member: "))
    if age >= 1: 
        count+=age
        check +=1
        average = count / check        
    elif age == -1:
        break

print("The average age of your family members is", average)

