import streamlit as st
import numpy as np
import model
import pandas as pd
import matplotlib.pyplot as plt


class EmotifyMachine:
    def __init__(self):
        self.emojis = ['😂', '💕', '😭', '😍', '😊',
                       '😘', '😔', '😩', '🙏', '👌', '😡', '🔥']

    def choose_random(self):
        return np.random.choice(self.emojis)

    def probability_dist(self):
        return np.random.uniform(low=0.0, high=1.0, size=(len(self.emojis),))


def run_streamlit():
    # em = EmotifyMachine()
    machine = model.HuggingEmotify()
    title = st.title('Emotify')
    subheader = st.subheader(
        'Bring your tweets and messages to life with the help of ML generated emojis!')
    text = st.text_area('Emotify machine', value='', max_chars=280,
                        placeholder='Paste your tweet (280 characters max) here')
    if st.button('Click to Emotify!'):
        output = machine.query({'inputs': text})[0]
        chosen_output = max(output, key=lambda x: x['score'])
        # print(output)
        st.write('Your chosen emoji: ', chosen_output['label'])

        fig, ax = plt.subplots()
        scores = [item['score'] for item in output]
        labels = [item['label'] for item in output]
        y_pos = np.arange(len(labels))

        ax.barh(np.arange(len(labels)),
                scores)
        ax.set_yticks(y_pos, labels=labels)
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_title('Confidence')

        st.pyplot(fig)


if __name__ == "__main__":
    run_streamlit()
