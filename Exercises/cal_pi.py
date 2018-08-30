
from __future__ import print_function  # to make sure that the print statement works with both Python 2 and 3.
from math import sqrt

"""
 Calculate pi using Madhava formula 
"""


# function to calculate pi
def cal_pi(k):
    value = 0

    for i in range(k):
        value += sqrt(12) * (-1/3)**i / (2*i+1)

    return value


# test it
if __name__ == "__main__":
    pi = cal_pi(200)
    print("The value of pi is: ", pi)

