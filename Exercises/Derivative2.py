from __future__ import print_function


def f(x):
    return x**4


class Derivative2:
    """
        second-order derivative: f''(x) = ( f(x+h) - 2*f(x) + f(x-h) ) / h**2
    """

    def __init__(self, f, h=1E-6):
        self.f, self.h = f, h

    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x + h) - 2*f(x) + f(x - h)) / h**2


# test it
if __name__ == "__main__":
    x = 1
    df2 = Derivative2(f)  # create an instance to represent f''(x)
    print("The second-order derivative is: ", df2(x))
