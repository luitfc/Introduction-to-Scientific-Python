from __future__ import print_function  # to make sure that the print statement work with both Python 2 and 3.
from datetime import date  # before we use a package, we need to import it first.


class test:
    AA = 101
    def __init__(self):
        self.__a = 100
        self.AA = 2000


aa = test()
print(aa.AA)
bb = test()
print(bb.AA)
bb.AA = 202

print(aa.AA)
print(bb.AA)