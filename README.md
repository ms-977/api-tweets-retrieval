# api-tweets-retrieval

This Flask application provides a set of RESTful APIs to interact with Twitter Favorites data. The application fetches data from a JSON file hosted on GitHub, allowing users to retrieve information about tweets, links in tweets, tweet details, and user profiles.

Prerequisites
Python 3.x
Flask
Requests
Installation
Clone the repository:

bash
Copy code
git clone [repository_url]
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Flask application:

bash
Copy code
python app.py
Access the APIs using the following routes:

Get all tweets:

Endpoint: /tweets
Method: GET
Get all links in tweets:

Endpoint: /tweets/links
Method: GET
Get tweet details by ID:

Endpoint: /tweet/<tweet_id>
Method: GET
Get user profile by screen name:

Endpoint: /user/<screen_name>
Method: GET
Sample Requests
Get all tweets:

bash
Copy code
curl http://localhost:5000/tweets
Get all links in tweets:

bash
Copy code
curl http://localhost:5000/tweets/links
Get tweet details by ID:

bash
Copy code
curl http://localhost:5000/tweet/123456
Get user profile by screen name:

bash
Copy code
curl http://localhost:5000/user/username
