# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:40:04 2017

@author: mgrotowski
"""

# =============================================================================
#                IMPORTING FILES FROM THE WEB
# =============================================================================

# Using urllib module & writing to csv file
from urllib.request import urlretrieve
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv'
urlretrieve(url, 'D:\Python_Anaconda\DataCamp\Data\whitewine.csv')

# Using pandas to do the same job
import pandas as pd
df = pd.read_csv(url, sep=';')
print(df.head())

# Using pandas to import Excel file: reading all sheets to dictionary
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'
xl = pd.read_excel(url, sheetname=None)
print(xl.keys())
print(xl['1700'].head())

# HTTP GET requests using urllib.request
from urllib.request import urlopen, Request
url = 'http://www.wikipedia.org/'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
htmlTxt = html.decode()

print(type(html))
print(type(htmlTxt))
print(html[:200])
print(htmlTxt[:200])

#HTTP GET requests using requests package (acts like a context manager; 
# no need to close the connection)
import requests
url = 'http://www.wikipedia.org/'
r = requests.get(url)
rTxt = r.text

print(type(r))
print(type(rTxt))
print(rTxt[:200])

# Scraping the web with BeautifulSoup
from bs4 import BeautifulSoup
import requests
url = 'https://www.python.org/~guido/'
r = requests.get(url)
htmlDoc = r.text
soup = BeautifulSoup(htmlDoc, 'lxml')

print(type(soup))
print('=========================================================')
print(soup.prettify())
print('=========================================================')
print(soup.get_text())
print('=========================================================')
print(soup.title)
print('=========================================================')
a_tags = soup.find_all('a')
for link in a_tags:
    print(link.get('href'))


# =============================================================================
#                APIs and JSONs
# =============================================================================
# reading json file
import json
jsonPath = 'D:\Python_Anaconda\DataCamp\Data\jsonExample.json'
with open(jsonPath, 'r') as jsonFile:
    jsonData = json.load(jsonFile)

print(type(jsonData))
for key, value in jsonData.items():
    print(key)
    print(value)

# getting json from OMDB API
import requests
r = requests.get('http://www.omdbapi.com/?apikey=ff21610b&t=hackers')
jsonData = r.json()
for key, value in jsonData.items():
    print(key + ':' + value)

# getting json from Wikipedia API using requests package
import requests
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'
r = requests.get(url)
json_data = r.json()
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


# Import package
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"
consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        self.file.write(json.dumps(tweet) + '\n')
        self.num_tweets += 1
        if self.num_tweets < 100:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)


# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)


# Filter Twitter Streams to capture data by the keywords:
stream.filter(track=['clinton', 'trump', 'sanders', 'cruz'])

# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

# Import package
import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text', 'lang'])

# Print head of DataFrame
print(df.head())


import re

def word_in_text(word, tweet):
    word = word.lower()
    text = tweet.lower()
    match = re.search(word, tweet)

    if match:
        return True
    return False


# Initialize list to store tweet counts
[clinton, trump, sanders, cruz] = [0, 0, 0, 0]

# Iterate through df, counting the number of tweets in which
# each candidate is mentioned
for index, row in df.iterrows():
    clinton += word_in_text('clinton', row['text'])
    trump += word_in_text('trump', row['text'])
    sanders += word_in_text('sanders', row['text'])
    cruz += word_in_text('cruz', row['text'])

# Import packages
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(color_codes=True)

# Create a list of labels:cd
cd = ['clinton', 'trump', 'sanders', 'cruz']

# Plot histogram
ax = sns.barplot(cd, [clinton, trump, sanders, cruz])
ax.set(ylabel="count")
plt.show()