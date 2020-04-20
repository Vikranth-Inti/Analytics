'''Write a Python program to accept a filename from the user and print the extension of that. '''

fyle=input("Please enter the filename : ")
file=fyle.split('.')
print("Extension of the given file name is : "+file[1])
