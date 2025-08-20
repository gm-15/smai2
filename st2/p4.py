import streamlit as st
from PIL import Image

#Sidebar
st.sidebar.markdown("Clicked Page 4")

#Page
st.title("Page 4")
image = Image.open("img/pic1.jpg")
st.image(image, caption="예제 이미지", use_container_width=True)