# Name: Charmi Kadi
# Date: June. 4, 2021
# Class: ICS3U1-01
# Description: Fruit stand menu with list of ten fruits and prices.

fruits = ["Mango", "Strawberry", "Watermelon", "Raspberry", "Apple", "Pear", "Pineapple", "Blueberry", "Grape", "Banana"]
prices = [5.25, 4.99, 12.50, 4.25, 5.50, 6.99, 10.98, 6.50, 8.25, 7.99]

print("Fresh Fruit Stand")
print("="*18)

print ("""
%s: $%8.2f
%s: $%5.2f
%s: $%5.2f
%s: $%10.2f
%s: $%10.2f
%s: $%10.2f
%s: $%5.2f
%s: $%5.2f
%s: $%5.2f
%s: $%5.2f
"""%
    
(fruits[0],prices[0],fruits[1],prices[1],fruits[2],prices[2],fruits[3],prices[3],fruits[4],prices[4],fruits[5],prices[5],fruits[6],prices[6],fruits[7],prices[7],fruits[8],prices[8],fruits[9],prices[9]))