import streamlit as st
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


# col1, col2 = st.columns(2)
#
# with col1:
#     st.checkbox("Disable radio widget", key="disabled")
#     st.checkbox("Orient radio options horizontally", key="horizontal")
#
# with col2:
#     st.write(st.session_state.disabled)
#     st.write(st.session_state.horizontal)
st.write("Click on the CheckBox Butten")
st.checkbox("Male", key="male")
st.checkbox("Female", key="female")
male_age=np.random.normal(loc=50,scale=10,size=1000).astype(int)
female_age=np.random.normal(loc=40,scale=10,size=1000).astype(int)
df=pd.DataFrame({"gender":["male"]*1000+["female"]*1000,"age":list(male_age)+list(female_age)})
# if st.session_state.male:
#     df=df[df["gender"]=="male"]
# if st.session_state.female:
#     df=df[df["gender"]=="female"]

fig = plt.figure(figsize=(10, 4))

sns.displot(df, x="age", hue="gender")
st.pyplot(fig)
plt.show()
