import streamlit as st

st.header("Balinese POS Tagging")
st.write('''Balinese POS Tagging is a project that can classify POS(Part of Speech) tag of a word within a sentence.
            This web app was created to fulfill the project based assignment of Natural Language Processing.''')

st.subheader("Tech Stack")
st.write("The tech stack used in this project are:")
tech1, tech2, tech3, tech4 = st.columns(4)
with tech1:
    st.image("https://github.com/streamlit.png", width=100)
    st.write("[Streamlit](https://streamlit.io/)")
with tech2:
    st.image("https://github.com/scikit-learn.png", width=100)
    st.write("[Scikit Learn](https://scikit-learn.org/stable/)")

st.subheader("Contributors")
person1, person2, person3, person4 = st.columns(4)
with person1:
    st.image("https://github.com/putuwaw.png", width=100)
    st.write("[Putu Widyantara](https://github.com/putuwaw)")
with person2:
    st.image("https://github.com/AksidF.png", width=100)
    st.write("[Diska Fortunawan](https://github.com/AksidF)")
with person3:
    st.image("https://github.com/OdeArdika.png", width=100)
    st.write("[Ode Ardika](https://github.com/OdeArdika)")



st.subheader("Source Code")
st.write(
    "The source code can be found [here](https://github.com/putuwaw/balinese-pos-tagging).")