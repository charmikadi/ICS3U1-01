# Name: Charmi Kadi
# Date: June. 12, 2021
# Course Code: ICS3U1-01
# Description: Calculates the product of odd digits in a number from user.

num = int(input("Please enter a number: "))

odd=0
even=0
order = []
product = 1

while(num!=0):
    rem=num%10
    if(rem%2==1):
        odd+=1
        order.append(odd)
    else:
        even+=1
    num//=10

print(order)
for i in order:
    print(i)
#print(order)
print("Number of odd digits = ", odd) 


















