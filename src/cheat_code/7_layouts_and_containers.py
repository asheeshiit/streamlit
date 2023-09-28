
############################ st.sidebar ##################################
# can you add interactivity to your app with widgets
# Each element that's passed to st.sidebar is pinned to the left, allowing users to focus on the content in your app.
import streamlit as st

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
############################ st.columns ##################################
# Insert containers laid out as side-by-side columns.
# Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

import numpy as np

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("A wide column with a chart")
col1.line_chart(data)

col2.subheader("A narrow column with the data")
col2.write(data)
############################ st.tabs ##################################
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
data = np.random.randn(10, 1)

tab1.subheader("A tab with a chart")
tab1.line_chart(data)

tab2.subheader("A tab with the data")
tab2.write(data)
############################ st.expander ##################################
import streamlit as st

st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

with st.expander("See explanation"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
############################ st.container ##################################
# Inserts an invisible container into your app that can be used to hold multiple elements.
############################ st.empty ##################################
# Inserts a container into your app that can be used to hold a single element.
# This allows you to, for example, remove elements at any point, or replace several elements at once (using a child multi-element container).
# Overwriting elements in-place using "with" notation:
import time

with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")

# Replacing several elements, then clearing them:
placeholder = st.empty()

# Replace the placeholder with some text:
placeholder.text("Hello")

# Replace the text with a chart:
placeholder.line_chart({"data": [1, 5, 2, 6]})

# Replace the chart with several elements:
with placeholder.container():
    st.write("This is one element")
    st.write("This is another")

# Clear all those elements:
placeholder.empty()
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