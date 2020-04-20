'''Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days '''

import datetime

d1=int(input("Please enter the day of first date : "))
m1=int(input("Please enter the month of first date : "))
y1=int(input("Please enter the year of first date : "))
date1=datetime.date(y1,m1,d1)

d2=int(input("Please enter the day of second date : "))
m2=int(input("Please enter the month of second date : "))
y2=int(input("Please enter the year of second date : "))
date2=datetime.date(y2,m2,d2)

print(date2-date1)
