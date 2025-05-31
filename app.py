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
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 2.5rem !important;
    color: #558b2f;
    text-align: center;
    margin-top: 0;
    animation: fadeInUp 1.5s ease-out;
    text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
}

.hero-section {
    position: relative;
    margin: 2rem 0;
    animation: fadeIn 2s ease-out;
}

.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.1));
    border-radius: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
    opacity: 0;
    transition: opacity 0.3s ease;
}

.hero-section:hover .hero-overlay {
    opacity: 1;
}

.mission-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 3rem;
    margin: 3rem auto;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    animation: fadeIn 2s ease-out;
    border-left: 5px solid #2e7d32;
    position: relative;
    overflow: hidden;
}

.mission-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, transparent 0%, rgba(255,255,255,0.1) 50%, transparent 100%);
    transform: translateX(-100%);
    transition: transform 0.6s ease;
}

.mission-container:hover::before {
    transform: translateX(100%);
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
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.stat-box {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    animation: fadeIn 2s ease-out;
    position: relative;
    overflow: hidden;
}

.stat-box::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #2e7d32, #558b2f);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.stat-box:hover {
    transform: translateY(-10px);
}

.stat-box:hover::before {
    transform: scaleX(1);
}

.stat-number {
    font-size: 3.5rem;
    font-weight: 700;
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
    line-height: 1;
}

.stat-label {
    font-size: 1.2rem;
    color: #558b2f;
    line-height: 1.4;
}

.goals-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.goal-card {
    background: white;
    border-radius: 15px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    animation: fadeIn 2s ease-out;
    position: relative;
    overflow: hidden;
}

.goal-card::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #2e7d32, #558b2f);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.goal-card:hover {
    transform: translateY(-5px);
}

.goal-card:hover::after {
    transform: scaleX(1);
}

.goal-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    transition: transform 0.3s ease;
}

.goal-card:hover .goal-icon {
    transform: scale(1.1);
}

.goal-title {
    color: #2e7d32;
    font-weight: 600;
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.goal-description {
    color: #558b2f;
    font-size: 1.1rem;
    line-height: 1.6;
}

.cta-button {
    position: relative;
    overflow: hidden;
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 1.4rem;
    padding: 1.2em 3em;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    box-shadow: 0 3px 5px 2px rgba(46, 125, 50, .3);
    transition: all 0.3s ease;
    margin: 4rem auto;
    display: block;
    width: 280px;
}

.cta-button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 6px 12px 4px rgba(46, 125, 50, .3);
}

.cta-button::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        120deg,
        transparent,
        rgba(255, 255, 255, 0.2),
        transparent
    );
    transition: 0.5s;
}

.cta-button:hover::before {
    left: 100%;
}

.developers {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2.5rem;
    margin-top: 4rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    animation: fadeIn 2.5s ease-out;
    border: 1px solid rgba(46, 125, 50, 0.1);
}

.dev-title {
    color: #1b5e20;
    font-weight: 600;
    font-size: 1.4rem;
    margin-bottom: 2rem;
    position: relative;
    display: inline-block;
}

.dev-title::after {
    content: '';
    position: absolute;
    bottom: -8px;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, transparent, #2e7d32, transparent);
}

.dev-name {
    color: #33691e;
    font-size: 1.2rem;
    margin: 1rem 0;
    transition: transform 0.3s ease;
}

.dev-name:hover {
    transform: translateX(10px);
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-50px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(50px);
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

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.05);
    }
    100% {
        transform: scale(1);
    }
}

.scroll-prompt {
    text-align: center;
    margin: 2rem 0;
    color: #2e7d32;
    font-size: 1.2rem;
    animation: bounce 2s infinite;
}

@keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
        transform: translateY(0);
    }
    40% {
        transform: translateY(-10px);
    }
    60% {
        transform: translateY(-5px);
    }
}
</style>
""", unsafe_allow_html=True)

# Main content
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# Header
st.markdown('<h1>🌱 UMDAC DATAHACKS 2025 🌱</h1>', unsafe_allow_html=True)
st.markdown('<h2 class="subtitle">Zero Hunger Challenge 🍽️🌍</h2>', unsafe_allow_html=True)

# Hero Section
st.markdown('<div class="hero-section">', unsafe_allow_html=True)
image = Image.open("background.png")
st.image(image, use_container_width=True)
st.markdown("""
<div class="hero-overlay">
    <div style="text-align: center; color: white; font-size: 2rem; font-weight: bold;">
        Together We Can End Hunger
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Scroll Prompt
st.markdown('<div class="scroll-prompt">↓ Scroll to explore our mission ↓</div>', unsafe_allow_html=True)

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
<div class="goals-grid">
    <div class="goal-card">
        <div class="goal-icon">🎯</div>
        <div class="goal-title">Zero Hunger</div>
        <div class="goal-description">End hunger and ensure access to safe, nutritious food for all people, all year round</div>
    </div>
    <div class="goal-card">
        <div class="goal-icon">🌾</div>
        <div class="goal-title">Sustainable Agriculture</div>
        <div class="goal-description">Promote sustainable farming practices and resilient agricultural methods</div>
    </div>
    <div class="goal-card">
        <div class="goal-icon">🤝</div>
        <div class="goal-title">Global Partnership</div>
        <div class="goal-description">Foster international cooperation and knowledge sharing for food security</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Call to Action Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center;">
        <button class="cta-button" id="start-button">
            Start Analysis
        </button>
    </div>
    
    <script>
        document.getElementById('start-button').onclick = function() {
            window.location.href = '/pages/country_input';
        }
    </script>
    """, unsafe_allow_html=True)

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