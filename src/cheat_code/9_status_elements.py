import streamlit as st
############################ st.progress ##################################
# Display a progress bar.
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1, text=progress_text)

############################ st.spinner ##################################
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')
############################ st.balloons ##################################
# Draw celebratory balloons.
# watch your app and get ready for a celebration!
st.balloons()

############################ st.error ##################################
# Display error message.
st.error('This is an error', icon="🚨")


############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################