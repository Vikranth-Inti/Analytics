''' Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
'''

import subprocess

fun=str(input("please enter a Python function that you wish to know its documentation : "))
p = subprocess.Popen("pydoc  "+fun, stdout=subprocess.PIPE, shell=True)
print(p.stdout.read())
