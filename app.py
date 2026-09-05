import streamlit as st

st.set_page_config(page_title="Hello World", page_icon="👋")

st.title("👋 Hello, World!")
st.write("This is a simple Streamlit app, ready for deployment.")

name = st.text_input("What's your name?", placeholder="Enter your name here")

if name:
    st.success(f"Hello, {name}! Welcome to Streamlit. 🎉")

st.divider()

count = st.slider("Pick a number", 0, 100, 25)
st.write(f"You picked: **{count}**")

if st.button("Click me!"):
    st.balloons()
