# Name: Charmi Kadi
# Date: June. 13, 2021
# Course Code: ICS3U1-01
# Description: Program that displays pattern of asterisks.

rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))

for i in range(rows):
    for j in range(columns):
        print('*', end = '')
    print()