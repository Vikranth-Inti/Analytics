'''Write a Python program to print the calendar of a given month and year.'''

import calendar
mnth=int(input("PLease enter the month : "))
yr=int(input("Please enter the year : "))
cal=calendar.TextCalendar().formatmonth(theyear=yr, themonth=mnth, w=0, l=0)
print(cal)
