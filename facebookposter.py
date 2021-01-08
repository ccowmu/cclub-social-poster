from dotenv import load_dotenv
from message_dictionary import covid_messages
import facebook
import requests
import sys
import os

load_dotenv()
post_list = []

access_token = os.environ.get("facebook_access_token")
page_id = os.environ.get("facebook_page_id")
graph = facebook.GraphAPI(access_token)

# number of items in the covid messages dictionary
keys_values = covid_messages.items()

# iterate through dictionary and put messages into a list
for key in covid_messages:
    post_list.append(covid_messages[key])

# argv[1] will chose the index of the list that contains needed message
index = int(sys.argv[1])


# post message to page's feed
def post_message(message_text):
    graph.put_object(
        page_id, "feed", message=message_text
    )


# choose message to post
def main():
    # comment this command when testing
    post_message(post_list[index])

    # uncomment this command when testing
    # print(post_list[index])


# run main
if __name__ == "__main__":
    main()
