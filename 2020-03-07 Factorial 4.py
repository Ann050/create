# -------------------------------------------------------------------------------
# Name:        factorial
# Purpose:
#
# Author:      chenw_000
#
# Created:     07/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


user_input = eval(input("Enter a number "))
factorial = factorial(user_input)
print(factorial)
