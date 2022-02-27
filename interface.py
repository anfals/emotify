import streamlit as st
import numpy as np
import model
import pandas as pd
import matplotlib.pyplot as plt


def run_streamlit():
    machine = model.ModelCloudRun()
    title = st.title('Emotify')
    st.subheader(
        'Bring your tweets and messages to life with the help of ML generated emojis!')
    text = st.text_area('Emotify machine', value='', max_chars=280,
                        placeholder='Paste your tweet (280 characters max) here')
    if st.button('Click to Emotify!'):
        if text:
            output = machine.predict(text)
            if not output:
                st.write(
                    'We\'re sorry. The Emotify machine is not working right now, or you have put in an improperly formatted input. Please try again.')
            else:
                st.write('Your chosen emoji: ', output['label'])
                st.write('Confidence: ', output['score'])
                st.write(f"[Emojipedia Entry for {output['label']}](https://emojipedia.org/{output['label']}/)")


if __name__ == "__main__":
    run_streamlit()
