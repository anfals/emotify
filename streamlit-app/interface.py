import streamlit as st
import numpy as np


class EmotifyMachine:
    def __init__(self):
        self.emojis = ['😂', '💕', '😭', '😍', '😊',
                       '😘', '😔', '😩', '🙏', '👌', '😡', '🔥']

    def choose_random(self):
        return np.random.choice(self.emojis)


em = EmotifyMachine()

title = st.title('Emotify')
subheader = st.subheader(
    'Bring your tweets and messages to life with the help of ML generated emojis!')
text = st.text_area('Emotify machine', value='', max_chars=280,
                    placeholder='Paste your tweet (280 characters max) here')
if st.button('Click to Emotify!'):
    st.write('Your chosen emoji: ', em.choose_random())
