# Utility functions
#
# Obtained from CS 121 class material

from datetime import datetime as dt
from datetime import date
import sys
import json

def cmp_to_key(mycmp):
    '''
    Convert a cmp= function into a key= function
    From: https://docs.python.org/3/howto/sorting.html
    '''
    
    class K:
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0
    return K


def cmp_count_tuples(t0, t1):
    '''
    Compare pairs using the second value as the primary key and the
    first value as the secondary key.  Order the primary key in
    non-increasing order and the secondary key in non-decreasing
    order.

    Inputs: 
        t0: pair
        t1: pair

    Returns: -1, 0, 1

    Sample uses:
        cmp(("A", 3), ("B", 2)) => -1

        cmp(("A", 2), ("B", 3)) => 1
  
        cmp(("A", 3), ("B", 3)) => -1

        cmp(("A", 3), ("A", 3))
    '''
    (key0, val0) = t0
    (key1, val1) = t1
    if val0 > val1:
        return -1
    elif val0 < val1:
        return 1
    elif key0 < key1:
        return -1
    elif key0 > key1:
        return 1
    return 0

def sort_count_pairs(l):
    '''
    Sort pairs using the second value as the primary sort key and the
    first value as the secondary sort key.

    Inputs: 
       l: list of pairs.

    Returns: list of key/value pairs
    '''
    return sorted(l, key=cmp_to_key(cmp_count_tuples))

def get_json_from_file(filename):
    '''
    Read data from a JSON file.
    '''
    try:
        return json.load(open(filename))
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)

