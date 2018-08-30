from __future__ import print_function  # to make sure that the print statement works with both Python 2 and 3.


def diff2(f, x, h=1E-6):
    value = (f(x + h) - 2*f(x) + f(x - h)) / h**2
    return value


def f(x):
    return x**4


# test it
if __name__ == "__main__":
    x = 1
    val = diff2(f, x)
    print("The second-order derivative is: ", val)
