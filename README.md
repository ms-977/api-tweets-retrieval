# api-tweets-retrieval

This Flask application provides a set of RESTful APIs to interact with Twitter Favorites data. The application fetches data from a JSON file hosted on GitHub, allowing users to retrieve information about tweets, links in tweets, tweet details, and user profiles.

1. Install Flask and Requests:

    ```bash
    pip install Flask requests
    ```

2. Run the Flask application:

    ```bash
    python your_app_name.py
    ```

Replace `your_app_name.py` with the name of your Python file containing the Flask application.

## Endpoints

### Get All Tweets

- **Endpoint:** `/tweets`
- **Method:** `GET`
- **Description:** Retrieve all tweets with their creation time, ID, and text.

### Get All Links from Tweets

- **Endpoint:** `/tweets/links`
- **Method:** `GET`
- **Description:** Extract all external links found in the tweet texts, grouped by tweet IDs.

### Get Tweet Details by ID

- **Endpoint:** `/tweet/<tweet_id>` "incude acutal tweet id within <here>
- **Method:** `GET`
- **Description:** Retrieve details of a specific tweet by its ID, including creation time, text, and user screen name.

### Get User Profile by Screen Name

- **Endpoint:** `/user/<screen_name>` "incude acutal screen name within <here>
- **Method:** `GET`
- **Description:** Retrieve detailed profile information of a specific Twitter user by screen name.
