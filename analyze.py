# Analyze tweets

import json
from basic_algo import find_top_n

def get_top_n_entities(tweets, entity_key, n):
    '''
    Find the N most frequently occuring entities.

    Inputs:
        tweets: a list of tweets
        entity_key: a pair ("hashtags", "text"), 
          ("user_mentions", "screen_name"), etc
        n: integer

    Returns: list of entity, count pairs
    '''
    to_find_list = []
    first_entity, second_entity = entity_key
    # Iterate over list of dictionaries representing tweets
    for i in tweets:
        sublist = i["entities"][first_entity]
        # Iterate over list of dictionaries in sublist, add to list to compute
        for j in sublist:
            value_of_key = j[second_entity]
            to_find_list.append(value_of_key.lower())
    return find_top_n(to_find_list, n)

