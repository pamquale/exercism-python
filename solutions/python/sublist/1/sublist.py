"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if not list_one and not list_two:
        return EQUAL
    if not list_one:
        return SUBLIST
    if not list_two:
        return SUPERLIST
    if len(list_one) == len(list_two):
        if list_one == list_two:
            return EQUAL
        return UNEQUAL
    if len(list_one) > len(list_two):
        for number in range(0, len(list_one) - 1):
            check_list = list_one[number:number + len(list_two)]
            if list_two == check_list:
                return SUPERLIST
        return UNEQUAL
    if len(list_one) < len(list_two):
        for number in range(0, len(list_two) - 1):
            check_list = list_two[number:number + len(list_one)]
            if list_one == check_list:
                return SUBLIST
        return UNEQUAL

        
