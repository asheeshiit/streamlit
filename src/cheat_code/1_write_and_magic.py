import streamlit as  st
import pandas as pd
import numpy as np
import altair as alt


######################################### Write arguments to the app. ############################################
# st.write(*args, unsafe_allow_html=False, **kwargs)
st.write('Hello, *World!* :sunglasses:')
df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.write(df)

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
#  accepts chart objects too!
c = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
# Magic
######################################### Magic. ############################################
'''
 allows you to write almost anything (markdown, data, charts) without having to type an explicit command at all.
'''
######################################### Write arguments to the app. ############################################
######################################### Write arguments to the app. ############################################
######################################### Write arguments to the app. ############################################
######################################### Write arguments to the app. ############################################
