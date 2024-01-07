import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Mukesh Portfolio", page_icon='Logo.png', layout='wide')


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

lottie_encoding = load_lottie_url("https://lottie.host/2108deec-329f-485f-9b7d-acfdcbd1d2c1/HcJ1VNTNXq.json")
img_contact_form = Image.open("Thumbnail2.jpeg")
img_lottie_animation = Image.open("Thumbnail.png")
with st.container():
    st.subheader("Hi, I am Mukesh :wave:")
    st.title("Mukesh From AVK")
    st.write("I Am Working on to get better at Python, for the Better of Mankind")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What Do I Do?")
        st.write('##')
        st.write("""
        - Study
        - Have Fun with Coding
        - Trying to Get Better Everyday
        """)

    with right_column:
        st_lottie(lottie_encoding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write('##')
    img_column, txt_column = st.columns((1, 2))
    with img_column:
        st.image(img_lottie_animation)
    with txt_column:
        st.subheader("E-Commerce Website")
        st.write("""
        An E-Commerce Website with many categories
        Try now!!!
        """)
        st.markdown("[Visit Now!!!](http://localhost:8501/)")

with st.container():
    st.write('---')
    st.header("Get in Touch with Me!!!")
    st.write('##')

    contact_form = """
    <form action="https://formsubmit.co/mukhee0906@gmail.testuser.com" method="POST">
        <input type ="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="Message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
