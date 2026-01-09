"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
def bake_time_remaining(time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(number_of_layers):
    """Calculate time needed for layer preparation

    :param number_of_layers: int - the number of layers in the lasagna

    This function takes the numbers of layers in the lasagna and counts how much time requires to prepare them.
    """
    return number_of_layers * 2



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    :param number_of_layers: int - the number of layers in the lasagna
    :param elapled_bake_time: int - elspsed cooking time in minutes

    This function takes two ints represented above and calculates total time spent cooking the lasagna
    """
    return number_of_layers * 2 + elapsed_bake_time
    

