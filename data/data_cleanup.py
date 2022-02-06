import sys
import re
import csv 
import emoji
import pandas as pd

labels = ['😂','💕','😭','😍','😊','😘','😔','😩','🙏','👌','😡','🔥']

def clean_single_text(text:str) -> str:
    clean_text = emoji.get_emoji_regexp().sub(r'', text)
    clean_text = re.sub(r"(?:\@|https?\://)\S+", "", clean_text)
    clean_text = clean_text.strip()
    return clean_text

def label_single_text(text:str) -> list:
    cur_labels = [0 for i in range(len(labels))]
    for i, ch in enumerate(labels):
        if ch in text:
            cur_labels[i] = 1
    return cur_labels

def clean_data(data_csv: str):
    df = pd.read_csv(data_csv)
    df = df[df['text'].notna()]
    df['clean_text'] = df['text'].apply(clean_single_text)
    df['labels'] = df['text'].apply(label_single_text)
    df.to_csv(data_csv[:data_csv.find('.csv')] + "_cleaned.csv")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Please provide data to clean.")
    else:
        data_csv = sys.argv[1]
        print(labels)
        clean_data(data_csv)