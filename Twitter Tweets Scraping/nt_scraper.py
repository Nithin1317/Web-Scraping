import pandas as pd
from ntscraper import Nitter

scrape = Nitter()

# get_tweets("user_name/hashtag_name/term_name",mode="user/hashtag/term",number= no.of tweets we want)
# get_profile_info("username")

def get_tweets(username,modes,n):
    final_tweets=[]
    tweets = scrape.get_tweets(username,mode=modes,number=n)
    for tweet in tweets['tweets']:
        data = [tweet['link'],tweet['text'],tweet['date'],tweet['stats']['likes'],tweet['stats']['comments']]
        final_tweets.append(data)

    data = pd.DataFrame(final_tweets,columns=['link','tweet','date','No_of_Likes','No_of_comments'])
    return data

data = get_tweets('ImRo45','user',5)

data.to_csv('tweets.csv')