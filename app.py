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

import streamlit as st

# Set page config
st.set_page_config(page_title="Byte Me", layout="wide")

# Replace with your chosen color from the image, e.g. "#a8d5a3"
background_color = "#F6F4AF"

# Inject CSS
page_bg_style = f'''
<style>
    .stApp {{
        background-color: {background_color};
    }}
</style>
'''

st.markdown(page_bg_style, unsafe_allow_html=True)

# Your existing app content below
st.title("UMDAC DATAHACKS 2025")
st.subheader("Zero Hunger")

# Load and display your image as usual
from PIL import Image
image = Image.open("background.png")  # update with your image path
st.image(image, use_container_width=True)

st.markdown("""
Welcome to the Zero Hunger DataHacks App!  
Enter the name of a country on the next page to view hunger predictions and insights.
""")

st.markdown("""
---
### Our Mission:  
*To empower communities worldwide by harnessing data to end hunger and achieve food security for all.*
""")

st.markdown("""
---
#### Developed by Universiti Malaya Year 1 Data Science Students:
Felicia Sia Xin Rou<br>
            Lau Hiap Meng<br>
             Kenny Ken Wan Jin
""", unsafe_allow_html=True)


if st.button("Start"):
    st.session_state.page = "country_input"
    st.experimental_rerun()
