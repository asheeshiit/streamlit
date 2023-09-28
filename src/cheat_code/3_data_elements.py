import streamlit as st
import pandas as pd
import numpy as np

############################ st.dataframe ##################################
df = pd.DataFrame(np.random.randn(50, 20),columns=('col %d' % i for i in range(20)))
st.dataframe(df)  # Same as st.write(df)
st.dataframe(df.style.highlight_max(axis=0))
# customize the dataframe via column_config, hide_index, or column_order
df = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [np.random.randint(0, 1000) for _ in range(3)],
        "views_history": [[np.random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)
# st.dataframe supports the use_container_width parameter to stretch across the full container width:
# Boolean to resize the dataframe, stored as a session state variable
st.checkbox("Use container width", value=False, key="use_container_width")
st.dataframe(df, use_container_width=st.session_state.use_container_width)


############################ st.data_editor ##################################
# to edit dataframes and many other data structures in a table-like UI.
df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")


data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
    }
)
st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands 🎈",
            width="medium",
            required=True,
        )
    },
    hide_index=True,
    num_rows="dynamic",
)
############################ st.column_config ##################################
# for configuring data display and interaction As menthioned above

############################ st.table ##################################
# Display a static table.
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

############################ st.metric ##################################
# Display a metric in big bold font, with an optional indicator of how the metric changed.
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")
############################ st.json ##################################
# Display object or string as a pretty-printed JSON string.
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################