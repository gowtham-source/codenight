import streamlit as st
import base64

file_ = open("pixels-neon.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.write('<center><h1>CodeNight🌙</h1></center>', unsafe_allow_html=True)
st.markdown(
    f'<center><img src="data:image/gif;base64,{data_url}" alt="cat gif"></center><br>',
    unsafe_allow_html=True,
)
st.markdown('<div style="text-align: center;"><h4>"Enhance your coding skills and stay sharp with daily coding challenges! CodeNight provides a platform for students to practice coding and solve real-world programming problems."</h4></div>',
            unsafe_allow_html=True)

st.write('<center><h1>Coming Soon!</h1></center>', unsafe_allow_html=True)
