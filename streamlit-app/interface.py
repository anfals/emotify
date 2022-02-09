import streamlit as st
import numpy as np


class EmotifyMachine:
    def __init__(self):
        self.emojis = ['😂', '💕', '😭', '😍', '😊',
                       '😘', '😔', '😩', '🙏', '👌', '😡', '🔥']

    def choose_random(self):
        return np.random.choice(self.emojis)

    def probability_dist(self):
        return np.random.uniform(low=0.0, high=1.0, size=(len(self.emojis),))


def run_streamlit():
    em = EmotifyMachine()

    title = st.title('Emotify')
    subheader = st.subheader(
        'Bring your tweets and messages to life with the help of ML generated emojis!')
    text = st.text_area('Emotify machine', value='', max_chars=280,
                        placeholder='Paste your tweet (280 characters max) here')
    if st.button('Click to Emotify!'):
        st.write('Your chosen emoji: ', em.choose_random())
        st.bar_chart(data=em.probability_dist())


if __name__ == "__main__":
    run_streamlit()
