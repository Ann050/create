#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chenw_000
#
# Created:     28/02/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
print(3+2)
print(5-1)
number = eval(input("Enter a non-negative integer to take the factorial of: "))
product = 1
for i in range(number):
 product = product * (i+1)
print(product)
