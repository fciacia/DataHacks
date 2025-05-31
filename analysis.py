import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Zero Hunger DataHacks",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with modern design and animations
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #F6F4AF 0%, #F0EDB1 100%);
}

.main-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 4.5rem !important;
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    text-align: center;
    margin: 2rem 0;
    animation: fadeInDown 1.5s ease-out;
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 2.5rem !important;
    color: #558b2f;
    text-align: center;
    margin-top: 0;
    animation: fadeInUp 1.5s ease-out;
}

.mission-container {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    padding: 2.5rem;
    margin: 3rem auto;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    animation: fadeIn 2s ease-out;
}

.mission-title {
    font-family: 'Poppins', sans-serif;
    font-size: 2.5rem !important;
    background: linear-gradient(45deg, #33691e 30%, #558b2f 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-align: center;
    font-weight: 600;
    margin-bottom: 1.5rem;
}

.mission-text {
    font-size: 1.4rem;
    color: #33691e;
    text-align: center;
    line-height: 1.8;
    font-style: italic;
}

.stats-container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 2rem;
    margin: 3rem 0;
}

.stat-box {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    flex: 1;
    min-width: 250px;
    animation: fadeIn 2s ease-out;
}

.stat-box:hover {
    transform: translateY(-10px);
}

.stat-number {
    font-size: 3rem;
    font-weight: 700;
    color: #2e7d32;
    margin-bottom: 1rem;
}

.stat-label {
    font-size: 1.2rem;
    color: #558b2f;
}

.image-container {
    position: relative;
    margin: 2rem auto;
    border-radius: 20px;
    overflow: hidden;
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
    transition: transform 0.3s ease;
    animation: fadeIn 2s ease-out;
}

.image-container:hover {
    transform: scale(1.02);
}

.stButton>button {
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 1.4rem;
    padding: 1em 3em;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    box-shadow: 0 3px 5px 2px rgba(46, 125, 50, .3);
    transition: all 0.3s ease;
    margin: 3rem auto;
    display: block;
    width: 250px;
}

.stButton>button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 10px 4px rgba(46, 125, 50, .3);
}

.developers {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 15px;
    padding: 2rem;
    margin-top: 4rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    animation: fadeIn 2.5s ease-out;
}

.dev-title {
    color: #1b5e20;
    font-weight: 600;
    font-size: 1.3rem;
    margin-bottom: 1.5rem;
}

.dev-name {
    color: #33691e;
    font-size: 1.1rem;
    margin: 0.7rem 0;
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.goals-container {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 3rem 0;
    flex-wrap: wrap;
}

.goal-card {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: transform 0.3s ease;
    flex: 1;
    min-width: 200px;
    max-width: 300px;
    animation: fadeIn 2s ease-out;
}

.goal-card:hover {
    transform: translateY(-5px);
}

.goal-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.goal-title {
    color: #2e7d32;
    font-weight: 600;
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.goal-description {
    color: #558b2f;
    font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Header
st.markdown('<h1>🌱 UMDAC DATAHACKS 2025 🌱</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Zero Hunger Challenge 🍽️🌍</h2>', unsafe_allow_html=True)

# Main image
st.markdown('<div class="image-container">', unsafe_allow_html=True)
image = Image.open("background.png")
st.image(image, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Mission Statement
st.markdown("""
<div class="mission-container">
    <div class="mission-title">Our Mission</div>
    <div class="mission-text">
        To empower communities worldwide by harnessing data science and artificial intelligence 
        to combat hunger, achieve food security, and promote sustainable agriculture. 
        Together, we can create a world where no one goes to bed hungry.
    </div>
</div>
""", unsafe_allow_html=True)

# Key Statistics
st.markdown("""
<div class="stats-container">
    <div class="stat-box">
        <div class="stat-number">828M</div>
        <div class="stat-label">People affected by hunger globally</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">45%</div>
        <div class="stat-label">Of child deaths linked to malnutrition</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">3.1B</div>
        <div class="stat-label">People cannot afford healthy diet</div>
    </div>
</div>
""", unsafe_allow_html=True)

# SDG Goals
st.markdown("""
<div class="goals-container">
    <div class="goal-card">
        <div class="goal-icon">🎯</div>
        <div class="goal-title">Zero Hunger</div>
        <div class="goal-description">End hunger and ensure access to safe, nutritious food</div>
    </div>
    <div class="goal-card">
        <div class="goal-icon">🌾</div>
        <div class="goal-title">Sustainable Agriculture</div>
        <div class="goal-description">Promote sustainable farming practices and food security</div>
    </div>
    <div class="goal-card">
        <div class="goal-icon">🤝</div>
        <div class="goal-title">Global Partnership</div>
        <div class="goal-description">Foster international cooperation and knowledge sharing</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to Action Button
if st.button("Start Analysis"):
    st.switch_page("pages/country_input.py")

# Developers Section
st.markdown("""
<div class="developers">
    <div class="dev-title">Developed by Year 1 Universiti Malaya Data Science Students</div>
    <div class="dev-name">Felicia Sia Xin Rou</div>
    <div class="dev-name">Lau Hiap Meng</div>
    <div class="dev-name">Kenny Ken Wan Jin</div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "main"