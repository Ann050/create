#-------------------------------------------------------------------------------
# Name:        定义计算x的n次方的函数
# Purpose:
#
# Author:      chenw_000
#
# Created:     28/05/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

