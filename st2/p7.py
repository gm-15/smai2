import streamlit as st

#Sidebar
st.sidebar.markdown("Clicked Page 7")

#Page
st.title("Page 7")

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)