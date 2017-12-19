# Basic Algorithms for analyzing tweets

from util import sort_count_pairs

def find_top_n(items, n):
    '''
    Find the N most frequently occuring items.

    Inputs:
        items: a list of items
        n: integer 

    Returns: sorted list of N tuples

    '''
    item_count = {}
    for item in items:
        item_count[item] = item_count.get(item, 0) + 1
    sorted_list = sort_count_pairs(item_count.items())
    return sorted_list[0:n]
