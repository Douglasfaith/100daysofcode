#name = input ("what is your name?")
#print ("Hello")
#print ("name")
#/n new line on the screen

#thiscomment is for helloworld
""" this is faith code
"""


# this code will store the input from the user
from importlib import invalidate_caches
from numbers import Integral
import string

num1 = input("Enter first number:")
num2 = input("Enter second number:")

try:
    print (int(num1) / int(num2))

except ZeroDivisionError:
    print("not allowed to divide by zero")

except ValueError:
    print("only integers allowed")


