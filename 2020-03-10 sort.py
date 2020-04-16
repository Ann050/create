#-------------------------------------------------------------------------------
# Name:        sort
# Purpose:
#
# Author:      chenw_000
#
# Created:     10/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def insersion_sort(list):
    for index in range(1,len(list)):
        value = list[index]
        i = index -1
        while i >= 0:
            if value < list[i]:
                list[i+1] = list[i]
                list[i] = value
                i = i - 1
            else:
                break



