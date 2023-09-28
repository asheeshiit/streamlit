import streamlit as st
############################ st.markdown ##################################
# Display string formatted as Markdown.
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")

############################ st.title ##################################
st.title('This is a title')
st.title('A title with _italics_ :blue[colors] and emojis :sunglasses:')
############################ st.header ##################################
st.header('This is a header')
st.header('A header with _italics_ :blue[colors] and emojis :sunglasses:')
############################ st.subheader ##################################
st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
############################ st.caption ##################################
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
############################ st.code ##################################
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
############################ st.text ##################################
st.text('This is some text.')

############################ st.latex ##################################
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
############################ st.divider ##################################
# Display a horizontal rule.
st.write("This is some text.")
st.slider("This is a slider", 0, 100, (25, 75))
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")
st.divider()  # 👈 Another horizontal rule
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
############################ st.markdown ##################################
