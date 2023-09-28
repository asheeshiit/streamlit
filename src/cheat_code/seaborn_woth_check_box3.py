import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# cmd : streamlit run /home/asheeshm/workspace/streamlit/src/seaborn_woth_check_box3.py

with st.sidebar:
    st.write("Click on the CheckBox Butten")
    st.checkbox("Male", key="male")
    st.checkbox("Female", key="female")



male_age=np.random.normal(loc=50,scale=5,size=1000).astype(int)
female_age=np.random.normal(loc=40,scale=5,size=1000).astype(int)
df=pd.DataFrame({"gender":["male"]*1000+["female"]*1000,"age":list(male_age)+list(female_age)})
df=df.sort_values(by=['age'])
filter_list=[]
if st.session_state.male:
    filter_list.append("male")
if st.session_state.female:
    filter_list.append("female")

df=df[df["gender"].isin(filter_list)]
if not df.empty:
    # fig = plt.figure(figsize=(10, 4))

    g=sns.displot(data=df, x="age", hue="gender")
    # sns.countplot(x="age", data=df,hue="gender")
    # sns.catplot(x="age",hue="gender", kind="count", data=df)
    st.pyplot(g)

    # st.pyplot(fig)
