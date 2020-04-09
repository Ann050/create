# -------------------------------------------------------------------------------
# Name:        Factorial2
# Purpose:
#
# Author:      chenw_000
#
# Created:     06/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------
Number = eval(input("Enter a number "))
Factorial = 1
i = 1
while i < Number:
    Factorial = Factorial * (i + 1)
    i = i + 1
    print(Factorial)
