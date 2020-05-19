#-------------------------------------------------------------------------------
# Name:        等差数列前100项和
# Purpose:
#
# Author:      chenw_000
#
# Created:     16/05/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Sum = 0
a = 1
b = 0
for i in range(100):
    a = a + 3
    Sum = Sum + a
    b = b + 1
print(a)  #最后一项是多少
print(b)  #检查有多少项
print(Sum)
