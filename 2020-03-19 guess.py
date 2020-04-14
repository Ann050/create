#-------------------------------------------------------------------------------
# Name:        guess 2
# Purpose:
#
# Author:      chenw_000
#
# Created:     19/03/2020
# Copyright:   (c) chenw_000 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
guess = eval(input("Enter: " " "))
secret = "123"
i = 1
while i<3:
    if guess != secret:
        print("no")
        i = i +1
        print(secret)