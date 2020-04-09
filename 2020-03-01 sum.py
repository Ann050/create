# -------------------------------------------------------------------------------
# Name:        plus
# Purpose:
#
# Author:      chenw_000
#
# Created:     01/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

number = eval(input("Enter a non-negative intager to plus "))
product = 0
for i in range(number):
    product = product + (i + 1)
print(product)
