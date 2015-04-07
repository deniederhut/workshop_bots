
# coding: utf-8

# # Twitter Bots

# A workshop by Dillon Niederhut and Juan Shishido.
# 
# Interacting with <a href="https://twitter.com/tob_pohskrow" target="_blank">**tob_pohskrow**</a>.

# ## Bots

# The W's: **W**hat, **w**hy, and probably even ho**w**.
# 
# ### What is a bot?
# 
# A bot is a program that runs user defined tasks in an automated way.
# 
# ### Why would you want a bot?
# 
# For fun! For laughs. For productivity.
# 
# ### What can you do with a bot?
# 
# You can test code. You can use it to collect data. On Twitter, you can use a bot to post automated status updates. You can even use a bot can alert you when certain events happen (inside or outside of Twitter).
# 
# At the D-Lab, we pull training/workshop information from our calendar, generate a tweet, and post it to the @DLabAtBerkeley account. We're trying to add more functionality, such as including instructor usernames in the tweets or processing the descriptions and titles to come up with a short, descriptive summary.
# 
# There are lots of people doing interesting things with bots on Twitter. For inspiration, see: http://qz.com/279139/the-17-best-bots-on-twitter/.
# 
# ### How can you do it?
# Read on.

# ## APIs

# **API** is shorthand for **A**pplication **P**rogramming **I**nterface, which is in turn computer-ese for a middleman.
# 
# Think about it this way. You have a bunch of things on your computer that you want other people to be able to look at. Some of them are static documents, some of them call programs in real time, and some of them are programs themselves.
# 
# ### Solution 1
# 
# You publish login credentials on the internet, and let anyone log into your computer
# 
# Problems:
# 
# 1. People will need to know how each document and program works to be able to access their data
# 
# 2. You don't want the world looking at your browser history
# 
# ### Solution 2
# 
# You paste everything into HTML and publish it on the internet
# 
# Problems:
# 
# 1. This can be information overload
# 
# 2. Making things dynamic can be tricky
# 
# ### Solution 3
# 
# You create a set of methods to act as an intermediary between the people you want to help and the things you want them to have access to.
# 
# Why this is the best solution:
# 
# 1. People only access what you want them to have, in the way that you want them to have it
# 
# 2. People use one language to get the things they want
# 
# Why this is still not Panglossian:
# 
# 1. You will have to explain to people how to use your middleman
# 

# ## What is Twitter?

# ### Twitter is visible 
# 
# 1. Currently 8th ranked website worldwide, 7th in the US
# 
# 2. 288 million users per month
# 
# 3. 500 million tweets per day
# 
# ### Twitter is democratic
# 
# 1. 80% of users are on mobile devices
# 
# 2. Support for 33 languages
# 
# 3. American Twitter users are disproprtionately from underrepresented communities
# 
# 4. Fun Fact: the third most-searched for term leading to Twitter, after 'Twitter' and 'CNN' is the name of a porn actress
# 
# ### Twitter is information
# 
# 1. User histories
# 
# 2. User (and tweet) location
# 
# 3. User language
# 
# 4. Tweet popularity
# 
# 5. Tweet spread
# 
# 6. Conversation chains
# 
# ### Twitter is antidemocratic
# 
# 1. Mexico's government has been accused of using Twitter for false flag operations
# 
# 2. GCHQ has a software library purportedly designed to modulate public opinion
# 
# 3. Someone here used a Twitter bot to occupy all of State Bird Provision's table reservations
# 
# ### Twitter is opaque
# 
# 1. Twitter's API does not return all tweets that match your search criteria
# 
# 2. The sampling method is not published, and can change without notice
# 
# 3. Location information is not necessarily provided by GPS
# 
# ### Twitter is spam
# 
# 1. Two years ago, approximately 20 million Twitter accounts were advertising bots
# 
# 2. Appoximately 1/3 of any accounts followers are not humans
# 
# 3. Of the top ten accounts (by followers), eight are celebrities (the other two are YouTube and the current President)

# ## A Tweet

# Simple, right? 140 characters. Done.

# #### Let's find out

# In[ ]:

import json

with open('data/first_tweet.json','r') as f:
    a_tweet = json.loads(f.read())


# #### What you see

# In[ ]:

print a_tweet['text']


# #### What you get

# In[ ]:

from pprint import pprint

pprint(a_tweet)


# You have access to more than just the text.

# ## JSON

# > JSON (JavaScript Object Notation), specified by RFC 7159 (which obsoletes RFC 4627) and by ECMA-404, is a lightweight data interchange format inspired by JavaScript object literal syntax (although it is not a strict subset of JavaScript).

# Sure. Think of it like Python's `dict` type. Keys and values, collectively referred to as items, are separated by a colon. Multiple items are separated by commas. Keys must be immutable and unique to a particular `dict`. Values can be of any type, including `list` or even another `dict`. Dictionaries are always surrounded by braces, `{}`. 
# 
# In JSON, it's common practice to have nested or hierarchical dictionaries. For example, some Reddit endpoints return JSON objects that are six dictionaries deep.

# So, how can you access data within a Python `dict`? You first need the keys. To get the keys, you must look at the data or use the `.keys()` method, which returns a list of the key names in an arbitrary order.

# In[ ]:

a_tweet.keys()


# How about the values? Use the dictionary name along with the key in square brackets. We used this above to access the tweet's text. If you're interested in knowing when the tweet was created, use the following.

# In[ ]:

a_tweet['created_at']


# Note: This is given in UTC. The offset is shown by the `+0000`.

# The thing about JSON data or Python dictionaries is that they can have a nested structure. What if we want access to the values associated with the `entities` key?

# In[ ]:

a_tweet['entities']


# It's a dictionary. To access any of _those_ values, use the appropriate key.

# In[ ]:

a_tweet['entities']['hashtags']


# Of course, there are no hashtags associated with this tweet, so it's just an empty `list`.

# In[ ]:

type(a_tweet)


# ## Authentication

# Before you proceed, you'll need four pieces of information.
# 
# * consumer_key
# * consumer_secret
# * access_token_key
# * access_token_secret
# 
# While signed in to your Twitter account, go to: https://apps.twitter.com/. Follow the prompts to generate your keys and access tokens. You'll need to have a phone number associated with your account.

# ## Accessing the API

# So, how do we actually access the Twitter API? Well, there are several ways. To search for something, you can use the search URL, which looks like: https://api.twitter.com/1.1/search/tweets.json?q=%40twitterapi. The `q` is the query parameter. You can replace it with anything you want. However, if you follow this link, you'll get an error because your request was not authenticated.
# 
# For more information on the REST APIs, end points, and terms, check out: https://dev.twitter.com/rest/public. For the Streaming APIs: https://dev.twitter.com/streaming/overview.

# Instead, we'll use Jonas Geduldig's `TwitterAPI` module: https://github.com/geduldig/TwitterAPI. The nice thing about modules such as this one--yes, there are others--is that it handles the OAuth. `TwitterAPI` supports both the REST and Streaming APIs.

# ## TwitterAPI

# To authenticate, run the following code.

# In[ ]:

from TwitterAPI import TwitterAPI

consumer_key = '9cQ7SNtWsmTTfta8Gv5y8svWD'
consumer_secret = 'kjJllUPEJefFQ4Dfr6dBXDETiQaVWFXTt0zLSNMy8tY8F8IpqK'
access_token_key = '3129088320-dIfoDZOt5cIKVCFnJpS0krt3oCYPB13rk5ITavI'
access_token_secret = 'H41REM344zgKCvJenCGGsF1JbFSK8I1r1WvFrc8Fs74jg'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


# We've created a Twitter account for this talk. Feel free to use the following keys and access tokens to familiarize yourself with the API. But, be aware that Twitter imposes rate limits, and that these rate limits are different for different kinds of API interactions.
# 
# > Search will be rate limited at 180 queries per 15 minute window for the time being, but we may adjust that over time.
# 
# > \- Twitter

# ### Search

# Notice that the end point is the same as in the URL example, `search/tweets`.

# #### Query

# In[ ]:

r = api.request('search/tweets', {'q':'technology'})
for item in r:
    pprint(item)


# The API supports what it calls query operators, which modify the search behavior. For example, if you want to search for tweets where a particular user is mentioned, include the at-sign, `@`, followed by the username. To search for tweets sent to a particular user, use `to:username`. For tweets from a particular user, `from:username`. For hashtags, use `#hashtag`.
# 
# For a complete set of options: https://dev.twitter.com/rest/public/search.

# To make things clearer, let's use variables.

# In[ ]:

end_point = 'search/tweets'
parameters = {
    'q':'from:Google #GoogleMaps', 
    'count':1
}

r = api.request(end_point, parameters)
for item in r:
    print item['text'] + '\n'


# #### User

# You can also search user timelines. Notice the change in the end point and parameter values.

# In[ ]:

end_point = 'statuses/user_timeline'
parameters = {
    'screen_name':'UCBerkeley', 
    'count':1
}

r = api.request(end_point, parameters)
for item in r:
    print item['text']


# #### Location

# In[ ]:

end_point = 'search/tweets'
parameters = {
    'q':'technology',
    'geocode':'37.871667,-122.272778,5km', # UC Berkeley
    'count':1
}

r = api.request(end_point, parameters)
for item in r:
        print item['text']


# #### Language

# In[ ]:

end_point = 'search/tweets'
parameters = {
    'q':'*',
    'lang':'fr',
    'count':1
}

r = api.request(end_point, parameters)
for item in r:
    print item['text']


# ### Streaming

# In[ ]:

end_point = 'statuses/filter'
parameters = {
    'q':'coding',
    'locations': '-180,-90,180,90'
}

r = api.request(end_point, parameters)
tweets = r.get_iterator()
for i in range(15):
    t = tweets.next()
    print t['place']['full_name'] + ', ' + t['place']['country'] + ': ' + t['text'], '\n'


# ### Posting

# The other half of the game is posting.

# In[ ]:

end_point = 'statuses/update'
parameters = {
    'status':'.IPA rettiwT eht tuoba nraeL'
}

r = api.request(end_point, parameters)
print r.status_code


# ## Saving Data

# Now that you know how to search for tweets, how about we save them?

# In[ ]:

for item in r:
    filename = r['id_str'] + '.json'
    with open(filename,'w') as f:
        f.write(item)


# Note: if you are doing a lot of these, it will be faster and easier to use a non-relational database like MongoDB

# ## Scheduling

# The real beauty of bots is that they are designed to work without interaction or oversight. Imagine a situation where you want to write a Twitter bot that replies 'HOORAY!' every time someone posts on Twitter that they were accepted to Cal. One option is to write a python script like this and call it by hand every minute.

# In[ ]:

from TwitterAPI import TwitterAPI
import time

consumer_key = '9cQ7SNtWsmTTfta8Gv5y8svWD'
consumer_secret = 'kjJllUPEJefFQ4Dfr6dBXDETiQaVWFXTt0zLSNMy8tY8F8IpqK'
access_token_key = '3129088320-dIfoDZOt5cIKVCFnJpS0krt3oCYPB13rk5ITavI'
access_token_secret = 'H41REM344zgKCvJenCGGsF1JbFSK8I1r1WvFrc8Fs74jg'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

r = api.request('search/tweets', {'q':'accepted berkeley'})
for item in r.get_iterator():
    username = item['user']['screen_name']
    parameters = {'status':'HOORAY! @' + username}
    r = api.request('statuses/update', parameters)
    time.sleep(5)
    print r.status_code


# But you are a human that needs to eat, sleep, and be social with other humans. Luckily, most `UNIX` based systems have a time-based daemon called `cron` that will run scripts like this *for you*. The way that `cron` works is it reads in files where each line has a time followed by a job (these are called cronjobs). They looks like this:
# 
# ```
# 0 * * * * python twitter_bot.py
# ```
# 
# This is telling `cron` to execute `python twitter_bot.py` at `0` seconds, every minute, every hour, every day, every year, until the end of time.

# In[ ]:

# That thing after crontab is a lowercase L even though it looks like a 1
# This will execute directly through your shell, so use with caution
get_ipython().system(u'crontab -l | { cat; echo "0 * * * * python twitter_bot.py"; } | crontab -')


# If you are using a mac (especially Mavericks or newer), Apple prefers that you use their init library, called `launchd`. `launchd` is a bit more complicated, and requires that you create an xml document that will be read by Apple's init service:
# 
# ```
# <?xml version="1.0" encoding="UTF-8"?>
# <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
# <plist version="1.0">
# <dict>
#     <key>Label</key>
#     <string>twitter.bot</string>
#     <key>ProgramArguments</key>
#     <array>
#         <string>python</string>
#         <string>twitter_bot.py</string>
#     </array>
#     <key>StartCalendarInterval</key>
#     <dict>
#         <key>Minute</key>
#         <integer>00</integer>
#     </dict>
# </dict>
# </plist>
# ```
# 
# We won't be messing with `launchd` for this workshop.

# ## Now it is time for you to make your own twitter bot!
# 
# To get you started, here is a template in python. You should modify the search parameters and post parameters to get the bot to act the way you want.

# In[ ]:

from TwitterAPI import TwitterAPI
import time

consumer_key = '9cQ7SNtWsmTTfta8Gv5y8svWD'
consumer_secret = 'kjJllUPEJefFQ4Dfr6dBXDETiQaVWFXTt0zLSNMy8tY8F8IpqK'
access_token_key = '3129088320-dIfoDZOt5cIKVCFnJpS0krt3oCYPB13rk5ITavI'
access_token_secret = 'H41REM344zgKCvJenCGGsF1JbFSK8I1r1WvFrc8Fs74jg'

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

request_parameters = {} #Enter your search parameters here

def main():
    while True: #You may want to set a condition here
        r = api.request('search/tweets', request_parameters)
        if r.status_code == 200:
            for item in r.get_iterator():
                if True: #You may want to set a condition here
                    post_parameters = {} #Enter your post parameters here
                    p = api.request('statuses/update', post_parameters)
                    time.sleep(15)
        if r.status_code == 420: #If Twitter is throttling you
            break
        if r.status_code == 429: #If you are exceeding the rate limit
            time.sleep(60)
        
if __name__ == 'main':
    main()


# In[ ]:



