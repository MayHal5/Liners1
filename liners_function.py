"""
    A module that contains functions
    Author: Maysan Halaby
    Date: 11/03/2024
"""


def str_len(lst: list):
    """
    Goes through each string in the list and calculates its length
    :param lst: list of strings
    :return: list with length of each string in the list
    """
    return [len(i) for i in lst]


def mul_table(num: int) -> list:
    """
    which receives a number and multiplies it by the number itself
    number of times
    :param num: A number multiplied
    :return:list of the multiplied numbers
    """
    return [num * i for i in range(1, 1 + num)]
