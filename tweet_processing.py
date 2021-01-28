import os, json
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from wordcloud import WordCloud

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')
STOPWORDS = set(stopwords.words('english'))


def read_json_from_file(fname):
    # input fname as argument, return list of json documents
    with open(os.path.join(FILES_STATIC, fname), 'r') as f:
        list_of_json = json.loads(f.read())
    return list_of_json


def get_tweet_text(fname):
    # input fname as argument, return a list of tweet-text,

    list_of_json = read_json_from_file(fname)
    list_of_tweets = []
    for json_doc in list_of_json:
        list_of_tweets.append(json_doc['text'])

    return list_of_tweets


def get_tweet_text_by_keyword(fname, keyword):
    # function to return list of tweet-text only if keyword is present

    list_of_tweets = get_tweet_text(fname)
    filtered_tweets = []
    for tweet in list_of_tweets:
        if keyword.lower() in tweet.lower():
            filtered_tweets.append(tweet)
    return filtered_tweets


def get_list_of_token(fname):
    list_of_tweets = get_tweet_text(fname)
    list_of_tokens = [word.lower() for tweet in list_of_tweets
                                    for word in tweet.split(' ')
                                    if word not in STOPWORDS and len(word) > 3 and not word.startswith('http')]
    return list_of_tokens


def generate_wordcloud_by_freq(fname):
    list_of_tweets = get_list_of_token(fname)
    wordcloud = WordCloud(stopwords=STOPWORDS, background_color='white', width=900, height=1000).generate(' '.join(list_of_tweets))
    save_fname = "wordcloud_freq.png"
    wordcloud.to_file(os.path.join(FILES_STATIC, save_fname))

    return save_fname


# TWEET_CONTENTS = read_json_from_file('tweets.json')
# print(search_tweets('tweets.json', "christmas"))
# print(generate_wordcloud_by_freq('tweets.json'))



### Sanity check ###
# print(read_json_from_file('tweets.json')[:5])
# print(get_tweet_text('tweets.json'))
# print(get_tweet_text_by_keyword('tweets.json', keyword='video'))