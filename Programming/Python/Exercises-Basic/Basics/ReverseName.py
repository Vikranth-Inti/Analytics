'''Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.'''

name=input("Please give your full name : ")
ListName=name.split(' ')
outputString=ListName[1]+' '+ListName[0]
print(outputString)
