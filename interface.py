import streamlit as st
import numpy as np
import model
import pandas as pd
import altair as alt


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
                sorted_response = sorted(
                    output, key=lambda v: v['score'], reverse=True)
                st.write('Your chosen emoji: ', sorted_response[0]['label'])
                st.write('Confidence: ', sorted_response[0]['score'])
                st.write(
                    f"[Emojipedia Entry for {sorted_response[0]['label']}](https://emojipedia.org/{sorted_response[0]['label']}/)")

                alt_chart = alt.Chart(pd.DataFrame(sorted_response)).mark_bar().encode(
                    x='label:O',
                    y="score:Q",
                    color=alt.condition(
                        alt.datum.label == sorted_response[0]['label'],
                        alt.value('orange'),
                        alt.value('steelblue')
                    )
                )
                st.altair_chart(alt_chart, use_container_width=True)


if __name__ == "__main__":
    run_streamlit()
