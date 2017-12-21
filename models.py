# Build models using Vincent

import vincent as vis
from util import get_json_from_file
from analyze import get_top_n_entities

def make_model(tweets, n, x_title, y_title):
	'''
    Makes bar chart of n most frequently written hashtags.

    Inputs:
        tweets: a list of tweets
        n: integer
        x_title: x axis title
        y_title: y axis title

	Returns: bar chart data
    '''
	top_hashtags = get_top_n_entities(tweets, ("hashtags", "text"), n)
	labels, freq = zip(*top_hashtags)
	data = {'data': freq, 'x': labels}
	bar = vis.Bar(data, iter_idx='x')
	bar.axis_titles(x=x_title, y=y_title)
	return bar

# Edit this section according to whichever handle you're analyzing
trump_tweets = get_json_from_file("data/trump.json")
make_model(trump_tweets, 10, "Top 10 Hashtags", "Frequency").to_json('models/top_hashtags_trump.json')

obama_tweets = get_json_from_file("data/obama.json")
make_model(obama_tweets, 10, "Top 10 Hashtags", "Frequency").to_json('models/top_hashtags_obama.json')