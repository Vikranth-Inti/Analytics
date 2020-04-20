'''Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014'''

from datetime import date
Day=int(input("PLease enter day in mumber : "))
Month=int(input("Please enter the month : "))
Year=int(input("Enter year : "))
Date=date(Year,Month,Day)

print("The given date is :  "+str(Date))
