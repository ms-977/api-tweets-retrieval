#for this project i managed to directly fetch data from given url, rather than
#  downloading the json file on my machine and using it directly from there.
#   
from flask import Flask, jsonify
import re
import requests
app = Flask(__name__)

def retrieve_data(url):
    # Make a GET request to the given URL
    response = requests.get(url)
    
    # Check if the response status code is 200 , which mean we getting a response
    if response.status_code == 200:
        return response.json()  # Parse the response as JSON file
    else:
        # Return None to indicate an unsuccessful requesst
        return None

def find_links(tweet):
    # this will match any https request that we make
    url_type = r'https?://[^\s]+'
    # find any url that inculdes symbols that we justt included above
    return re.findall(url_type, tweet["text"])

@app.route('/tweets', methods=['GET'])# this will get us all tweets found in url
def get_all_tweets():
    github_url = 'https://foyzulhassan.github.io/files/favs.json'#url to fetch data from
    my_data = retrieve_data(github_url)
    
    # Check if we are getting dfata back
    if my_data is not None and isinstance(my_data, list):
        # extract data specified by tweets
        tweets = [
            {"created_at": tweet["created_at"], "id": tweet["id"], "text": tweet["text"]}
            for tweet in my_data
        ]
        return jsonify({"tweets": tweets})
    else:
        return jsonify({"error": "Error fetching data from given rurl."}), 500

@app.route('/tweets/links', methods=['GET'])# this will get us all the links to the twweets
def get_links():
    github_url = 'https://foyzulhassan.github.io/files/favs.json'
    my_data = retrieve_data(github_url)
    
    # Check if the data retrieval was successful
    if my_data is not None and isinstance(my_data, list):
        # Extract links from each tweet's text and group them by tweet IDs
        links = {tweet["id"]: find_links(tweet) for tweet in my_data if find_links(tweet)}
        return jsonify({"links": links})
    else:
        return jsonify({"error": "Error fetching data from GitHub."}), 500

@app.route('/tweet/<tweet_id>', methods=['GET'])#thius will retrieve the id of the tweet
def get_tweet_info(tweet_id):
    github_url = 'https://foyzulhassan.github.io/files/favs.json'
    my_data = retrieve_data(github_url)
    
    # Check if the data retrieval was successful
    if my_data is not None and isinstance(my_data, list):
        # Find the tweet with the specified ID
        tweet = next((t for t in my_data if str(t["id"]) == tweet_id), None)
        if tweet:
            return {
                "created_at": tweet["created_at"],
                "text": tweet["text"],
                "user_screen_name": tweet["user"]["screen_name"]
            }
        else:
            return jsonify({"error": "tweet was not found"}), 404
    else:
        return jsonify({"error": "did not find data ."}), 500

@app.route('/user/<screen_name>', methods=['GET'])#this will reteive screen name of that tweet
def get_user_info(screen_name):
    github_url = 'https://foyzulhassan.github.io/files/favs.json'
    my_data = retrieve_data(github_url)
    
    # Check if the data retrieval was successful
    if my_data is not None and isinstance(my_data, list):
        # Find tweets related to the specified user screen name
        user_tweets = [tweet for tweet in my_data if tweet["user"]["screen_name"].lower() == screen_name.lower()]
        if user_tweets:
            user = user_tweets[0]["user"]
            return {
                "location": user["location"],
                "description": user["description"],
                "followers_count": user["followers_count"],
                "friends_count": user["friends_count"]
            }
        else:
            return jsonify({"error": "user was not found!"}), 404
    else:
        return jsonify({"error": "did not find data!!!."}), 500
    
if __name__ == '__main__':
    app.run(debug=True)