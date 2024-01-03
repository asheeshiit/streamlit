import streamlit as st
from datetime import datetime,date

############################ st.button ##################################
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
############################ st.download_button ##################################
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)
############################ st.checkbox ##################################
agree = st.checkbox('I agree')
if agree:
    st.write('Great!')
############################ st.radio ##################################
genre = st.radio(
    "What\'s your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
############################ st.selectbox ##################################
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
############################ st.multiselect ##################################
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)
############################ st.slider ##################################
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)
############################ st.select_slider ##################################
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
############################ st.text_input ##################################
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
############################ st.number_input ##################################
number = st.number_input('Insert a number')
st.write('The current number is ', number)
############################ st.text_area ##################################
# Display a multi-line text input widget.
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
# st.write('Sentiment:', run_sentiment_analysis(txt))
############################ st._input ##################################
# date input widget.
d = st.date_input(
    "When\'s your birthday",
    date(2019, 7, 6))
st.write('Your birthday is:', d)

############################ st.time_input ##################################
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
############################ st.file_uploader ##################################
# accepts multiple files at a time:
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
############################ st.camera_input ##################################
# widget that returns pictures from the user's webcam.
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)
############################ st.color_picker ##################################
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)
############################ st.markdown ##################################
############################ st.markdown ##################################