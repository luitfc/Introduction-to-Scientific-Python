from __future__ import print_function  # to make sure that the print statement works with both Python 2 and 3.

"""
    Class to represents a line (y = ax + b) that passes two points.
"""


class Line:
    def __init__(self, p1, p2):
        self.p1, self.p2 = p1, p2
        x1, y1 = p1
        x2, y2 = p2
        if x2 != x1:
            self.a = (y2 - y1) / float(x2 - x1)
            self.b = y1 - self.a * x1
        else:
            raise Exception('Vertical line x = %s' % x1)

    def y(self, x):
        a, b = self.a, self.b
        return a * x + b

    # or use __call__ method to make the class callable
    def __call__(self, x):
        a, b = self.a, self.b
        return a * x + b


# test it
if __name__ == "__main__":
    line = Line((0, 0), (10, 10))
    x = 5
    print("The value of y at x=%s is %s: " % (x, line.y(x)))  # use y method
    print("The value of y at x=%s is %s: " % (x, line(x)))  # use __call__ method
