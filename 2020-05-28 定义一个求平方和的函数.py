#-------------------------------------------------------------------------------
# Name:        定义一个求平方和的函数
# Purpose:
#
# Author:      chenw_000
#
# Created:     28/05/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def square_of_sum(l):
    sum = 0
    for x in l:
        sum = sum + x * x
    return sum
print(square_of_sum([2,3,4]))
