#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import json


#Twitter API credentials
consumer_key = "0FQKWHBk2biSQ48MI60ONDN12"
consumer_secret = "ZCFSopVJkuXPgpRclvcO5pgVoqlVQwvpJt29qZSCygCms92sNK"
access_key = "940503837156057089-DlIIemTz38MjhLLXopFKDGWB5SQbpEM"
access_secret = "bi3EDBWB6v8Bdi2npYJMFQGDOxM17vVISQS16N6RVmoPH"


def get_all_tweets(screen_name, filename):
    
    #Twitter only allows access to a users most recent 3240 tweets with this method
    
    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler("0FQKWHBk2biSQ48MI60ONDN12", "ZCFSopVJkuXPgpRclvcO5pgVoqlVQwvpJt29qZSCygCms92sNK")
    auth.set_access_token("940503837156057089-DlIIemTz38MjhLLXopFKDGWB5SQbpEM", \
        "bi3EDBWB6v8Bdi2npYJMFQGDOxM17vVISQS16N6RVmoPH")
    api = tweepy.API(auth)
    
    #initialize a list to hold all the tweepy Tweets
    alltweets = []    
    
    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    
    #save most recent tweets
    alltweets.extend(new_tweets)
    
    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1
    
    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(alltweets)))
       
    #write tweet objects to JSON
    file = open(filename + '.json', 'w') 
    print("Writing tweet objects to JSON please wait...")
    json.dump([status._json for status in alltweets],file,sort_keys = True,indent = 4)
    
    #close the file
    print("Done")
    file.close()

if __name__ == '__main__':
    #pass in the username of the account you want to download
    get_all_tweets("@BarackObama", "obama")
