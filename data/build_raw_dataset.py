import tweet_retrieval
import pandas as pd
import numpy as np
import time

TWITTER_API_RATE_LIMIT = 30000

#EMOJIS = "👌,💔,💗,😂,😆,😉,😙,😚,😜,😨,😩,😲,🙀"
EMOJIS = "😂,💕,😭,😍,😊,😘,😔,😩,🙏,👌,😡,🔥"
EMOJI_MAP_FILE = "/Users/anfalsiddiqui/development/cs329s/Project/data/5822100/emoji_map_1791.csv"
RAW_DATA_FILE = "/Users/anfalsiddiqui/development/cs329s/Project/data/5822100/balanced_test_plaintext.txt"
PROCESSED_OUTPUT_FILE = "/Users/anfalsiddiqui/development/cs329s/Project/data/processed/test.csv"

def get_emoji_ids():
    df = pd.read_csv(EMOJI_MAP_FILE)
    ids = []
    for emoji in EMOJIS.split(","):
        ids.append(df[df['Unnamed: 0'] == emoji].index[0])
    return ids

def create_conditions_from_ids(ids, raw_dataset_df):
    conditions = []
    for id in ids:
        conditions.append(raw_dataset_df['annotations'].str.contains(str(id)))
    return conditions

def convert_twitter_api_response_to_processed_rows(twitter_api_resp, df):
    rows = []
    data = twitter_api_resp['data']
    for record in data:
        id, text = record["id"], record["text"]
        annotations = df[df["id"] == id]["annotations"].iloc[0]
        rows.append({"id": id, "text": text, "annotations": annotations})
    return rows

def create_and_save_csv_from_rows(rows):
    df = pd.DataFrame(rows)
    df.to_csv(PROCESSED_OUTPUT_FILE, index=False)


def filter_raw_dataset(raw_dataset_df, df_conditions):
    return raw_dataset_df.loc[np.logical_or.reduce(df_conditions) & ~raw_dataset_df['id'].str.endswith("_q")]


if __name__ == "__main__":
    raw_dataset_df = pd.read_csv(RAW_DATA_FILE, sep="\t")
    df_conditions = create_conditions_from_ids(get_emoji_ids(), raw_dataset_df)
    raw_dataset_filtered_df = filter_raw_dataset(raw_dataset_df, df_conditions)
    processed_rows = []

    iterations = len(raw_dataset_filtered_df) // TWITTER_API_RATE_LIMIT + 1
    for i in range(iterations):
        print(f'Performing iteration {i+1} of {iterations}')
        request_limit_subset = raw_dataset_filtered_df[TWITTER_API_RATE_LIMIT * i:TWITTER_API_RATE_LIMIT * (i + 1)]
        for j in range(len(request_limit_subset) // 100):
            request_subset = request_limit_subset[100*j:100*(j+1)]
            cur_batch_tweet_ids = request_subset["id"].tolist()
            twitter_api_resp = tweet_retrieval.retrieve_tweets(cur_batch_tweet_ids)
            processed_rows += convert_twitter_api_response_to_processed_rows(twitter_api_resp, request_subset)
        time.sleep(900)

    create_and_save_csv_from_rows(processed_rows)









# convert the list of emojis into their IDs
# create a list of conditions based on all these ids
# filter down the dataset
# create a new pandas dataframe that we will save to
# for every 90,000 rows:
#   for every 100 rows:
#       map id to list of emojis in it
#       send request to twitter
#       for every member of data:
#           get tweet, id from data
#           get list of emojis by id
#           add row to dataframe that is [id, tweet, emoji]
    # sleep for 15 minutes