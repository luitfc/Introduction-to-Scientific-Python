from __future__ import print_function  # to make sure that the print statement work with both Python 2 and 3.
from datetime import date  # before we use a package, we need to import it first.


def get_year_of_today():  # a function to get the year number of today
    return date.today().year

print("This year is %s." % get_year_of_today())  # call function get_year_of_today and print the result.