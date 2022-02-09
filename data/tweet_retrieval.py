import requests
import os
import json

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAPJCYwEAAAAAcGowBFzpiulxvo76tf15K%2FUkvLU%3DfaIu7F0ZUwlKiZOeGoAVbQjUHHIs8V4AUUqQvAWCXT4cScgq6R"


def create_url(tweet_ids):
    assert len(tweet_ids) <= 100
    tweet_fields = "tweet.fields=lang,author_id"
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    ids = "ids=" + ",".join(tweet_ids)
    # You can adjust ids to include a single Tweets.
    # Or you can add to up to 100 comma-separated IDs
    url = "https://api.twitter.com/2/tweets?{}&{}".format(ids, tweet_fields)
    return url


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2TweetLookupPython"
    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def retrieve_tweets(tweet_ids):
    url = create_url(tweet_ids)
    json_response = connect_to_endpoint(url)
    return json_response

def main():
    # url = create_url([])
    # json_response = connect_to_endpoint(url)
    # print(json.dumps(json_response, indent=4, sort_keys=True))
    retrieve_tweets(["743525594323783680", "742723328864063488", "746328513016303616"])


if __name__ == "__main__":
    main()