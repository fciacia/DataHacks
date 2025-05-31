# import streamlit as st
# from PIL import Image

# # Set page config with wide layout
# st.set_page_config(page_title="Zero Hunger", layout="wide")

# # Title and subtitle
# st.title("UMDAC DATAHACKS 2025")
# st.subheader("Zero Hunger Challenge")

# # Load and display the visual image
# image = Image.open("background.png")  # Replace with your image path
# st.image(image, use_container_width=True)

# # Intro message
# st.markdown("""
# Welcome to the Zero Hunger DataHacks app!  
# Enter the name of a country on the next page to view hunger predictions and insights.
# """)
# st.markdown("""
# ---
# ### Our Mission:  
# *To empower communities worldwide by harnessing data to end hunger and achieve food security for all.*
# """)

# # Button to proceed to next page (we'll implement next page soon)
# if st.button("Start"):
#     st.session_state.page = "country_input"
#     st.experimental_rerun()  # Refresh app to load next page (once implemented)

# import streamlit as st

# # Set page config
# st.set_page_config(page_title="Byte Me", layout="wide")

# # Replace with your chosen color from the image, e.g. "#a8d5a3"
# background_color = "#F6F4AF"

# # Inject CSS
# page_bg_style = f'''
# <style>
#     .stApp {{
#         background-color: {background_color};
#     }}
# </style>
# '''

# st.markdown(page_bg_style, unsafe_allow_html=True)

# # Your existing app content below
# st.title("UMDAC DATAHACKS 2025")
# st.subheader("Zero Hunger")

# # Load and display your image as usual
# from PIL import Image
# image = Image.open("background.png")  # update with your image path
# st.image(image, use_container_width=True)

# st.markdown("""
# Welcome to the Zero Hunger DataHacks App!  
# Enter the name of a country on the next page to view hunger predictions and insights.
# """)

# st.markdown("""
# ---
# ### Our Mission:  
# *To empower communities worldwide by harnessing data to end hunger and achieve food security for all.*
# """)

# st.markdown("""
# ---
# #### Developed by Universiti Malaya Year 1 Data Science Students:
# Felicia Sia Xin Rou<br>
#             Lau Hiap Meng<br>
#              Kenny Ken Wan Jin
# """, unsafe_allow_html=True)


# if st.button("Start"):
#     st.session_state.page = "country_input"
#     st.experimental_rerun()

import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(page_title="Zero Hunger DataHacks", layout="wide")

# Custom CSS for fonts, colors, button
st.markdown("""
<style>        
.stApp {
    background-color: #F6F4AF;  
}
h1 {
    font-size: 4rem !important;
    color: #2e7d32;
    font-weight: bold;
    text-align: center;
    margin: 0;  
}
h3 {
    font-size: 3rem !important;
    color: #558b2f;
    text-align: center;
    margin-top: 0;
}
.mission-title {
    font-family: 'Georgia', serif;
    font-size: 2.5rem !important;
    color: #33691e;
    text-align: center;
    font-weight: bold;
    margin-top: 1.5em;
    margin-bottom: 0.3em;
}
p.mission {
    font-size: 1.3rem;
    color: #33691e;
    text-align: center;
    font-style: italic;
    margin-top: 0.5em;
    margin-bottom: 2em;
}
.stButton>button {
    background-color: #4caf50;
    color: white;
    font-size: 1.2rem;
    padding: 0.8em 2em;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    display: block;
    margin: 0 auto;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #388e3c;
}
.developers {
    text-align: center;
    margin-top: 3em;
    color: #1b5e20;
    font-weight: bold;
}
.block-container img {
    max-width: 100% !important;
    height: auto !important;
    margin-left: auto;
    margin-right: auto;
    display: block;
}
</style>
""", unsafe_allow_html=True)

# Page content in centered columns
cols = st.columns([1, 5, 1])  # narrow padding columns on sides

with cols[1]:
    st.markdown("""
    <h1>🌱 UMDAC DATAHACKS 2025 🌱</h1>
    """, unsafe_allow_html=True)
    st.subheader("Zero Hunger Challenge 🍽️🌍")
    image = Image.open("background.png")  
    st.image(image, use_container_width=True)
    st.markdown('<p class="mission-title">Our Mission</p>', unsafe_allow_html=True)
    st.markdown('<p class="mission">To empower communities worldwide by harnessing data to end hunger and achieve food security for all.</p>', unsafe_allow_html=True)

    if st.button("Start"):
        st.session_state.page = "country_input"
        st.experimental_rerun()

    st.markdown("""
    <div class="developers">
    Developed by Year 1 Universiti Malaya Data Science Students:<br>
    Felicia Sia Xin Rou<br>
    Lau Hiap Meng<br>
    Kenny Ken Wan Jin
    </div>
    """, unsafe_allow_html=True)
