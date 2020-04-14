#-------------------------------------------------------------------------------
# Name:        fib 2
# Purpose:
#
# Author:      chenw_000
#
# Created:     09/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))
