from dotenv import load_dotenv
from message_dictionary import covid_messages
import tweepy
import sys
import os

load_dotenv()
post_list = []

CONSUMER_KEY = os.environ.get("twitter_consumer_key")
CONSUMER_SECRET = os.environ.get("twitter_consumer_secret")
ACCESS_KEY = os.environ.get("twitter_access_key")
ACCESS_SECRET = os.environ.get("twitter_access_secret")

# authenticate tweepy can tweet for you
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# number of items in the covid messages dictionary
keys_values = covid_messages.items()

# iterate through dictionary and put messages into a list
for key in covid_messages:
    post_list.append(covid_messages[key])

# argv[1] will chose the index of the list that contains needed message
index = int(sys.argv[1])


# function to post tweet
def post_tweet(tweet):
    api.update_status(tweet)


# function to choose tweet to post
def main():
    # comment this command when testing
    post_tweet(post_list[index])

    # uncomment this command when testing
    # print(post_list[index])


# run main
if __name__ == "__main__":
    main()
