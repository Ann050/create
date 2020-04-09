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
    product = 1
    for i in range(number):
        product = product * (i + 1)
    return product


user_input = eval((input("Enter a number ")))
factorial_user_input = factorial(user_input)
print(factorial_user_input)
