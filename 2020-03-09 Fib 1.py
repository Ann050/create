# -------------------------------------------------------------------------------
# Name:        fib 1
# Purpose:
#
# Author:      chenw_000
#
# Created:     09/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

def fib(n):
    terms = [0, 1]
    i = 2
    while i <= n:
        terms.append(terms[i - 1] + terms[i - 2])
        i = i + 1
    return terms[n]

