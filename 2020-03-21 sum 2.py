#-------------------------------------------------------------------------------
# Name:        sum
# Purpose:
#
# Author:      chenw_000
#
# Created:     21/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def sum(n):
    #sum = 0
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
