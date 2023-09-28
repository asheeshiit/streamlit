import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

############################ st.line_chart ##################################
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
############################ st.area_chart ##################################
st.area_chart(chart_data)

############################ st.bar_chart ##################################
st.bar_chart(chart_data)
############################ st.pyplot ##################################
# Display a matplotlib.pyplot figure.
arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)

############################ st.plotly_chart ##################################
# Display an interactive Plotly chart.
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)

############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################