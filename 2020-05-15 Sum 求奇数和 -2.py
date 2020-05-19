#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chenw_000
#
# Created:     15/05/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Sum1 = 0
Num1 = 3
while Num1 < 1000:
    if (Num1 % 2) == 1:
        Sum1 = Sum1 + Num1
    Num1 = Num1 + 1
print(Sum1 + 1)

