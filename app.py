import streamlit as st
from PIL import Image

# Set page config
st.set_page_config(
    page_title="Zero Hunger DataHacks",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg, #f6f4af 0%, #f0edb1 100%);
}

h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 5rem !important;
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700;
    text-align: center;
    margin: 2rem 0;
    padding: 0 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    letter-spacing: 2px;
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 2rem !important;
    color: #000000;
    text-align: center;
    margin-top: 0;
    margin-bottom: 2rem;
    font-weight: 600;
    padding: 0 1rem;
}

.content-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
}

.highlight-text {
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-size: 1.1rem;
    display: inline-block;
    margin-bottom: 1rem;
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-top: 1rem;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.8rem;
    background: rgba(46, 125, 50, 0.1);
    border-radius: 10px;
}

.feature-icon {
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
    animation: fadeIn 1s ease-out;
}

.stat-box {
    background: white;
    border-radius: 15px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
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

.center-button {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.stButton > button {
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    border: none;
    padding: 1rem 3rem;
    border-radius: 50px;
    font-size: 1.4rem;
    font-weight: 600;
    width: auto;
    min-width: 250px;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(46, 125, 50, 0.4);
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.mega-button {
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 1.8rem;
    padding: 1.5rem 4rem;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    box-shadow: 0 3px 5px 2px rgba(46, 125, 50, .3);
    transition: all 0.3s ease;
    margin: 3rem auto;
    display: block;
    width: 400px;
    position: relative;
    overflow: hidden;
}

.mega-button:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 6px 12px 4px rgba(46, 125, 50, .3);
}

.mega-button::before {
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

.mega-button:hover::before {
    left: 100%;
}

.mission-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 3rem;
    margin: 3rem auto;
    box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
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

.target-card {
    background: rgba(46, 125, 50, 0.1);
    padding: 2rem;
    border-radius: 15px;
    margin-bottom: 1rem;
    border-left: 4px solid #2e7d32;
    transition: all 0.3s ease;
}

.target-card:hover {
    transform: translateX(10px);
    box-shadow: 0 4px 15px rgba(46, 125, 50, 0.2);
}

.developers-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 15px;
    padding: 2.5rem;
    margin-top: 4rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
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

.solutions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
}

.solution-card {
    background: white;
    border-radius: 15px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.solution-card::after {
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

.solution-card:hover {
    transform: translateY(-5px);
}

.solution-card:hover::after {
    transform: scaleX(1);
}

.solution-icon {
    font-size: 3.5rem;
    margin-bottom: 1rem;
    transition: transform 0.3s ease;
}

.solution-card:hover .solution-icon {
    transform: scale(1.1);
}

.solution-title {
    color: #2e7d32;
    font-weight: 600;
    font-size: 1.4rem;
    margin-bottom: 1rem;
}

.solution-description {
    color: #558b2f;
    font-size: 1.1rem;
    line-height: 1.6;
}

.platform-steps {
    list-style: none;
    padding: 0;
    margin: 0;
}

.platform-step {
    color: #33691e;
    font-size: 1.2rem;
    line-height: 1.8;
    margin-bottom: 1.5rem;
    padding-left: 2.5rem;
    position: relative;
}

.platform-step::before {
    content: '→';
    position: absolute;
    left: 0;
    color: #2e7d32;
    font-weight: bold;
    transition: transform 0.3s ease;
}

.platform-step:hover::before {
    transform: translateX(5px);
}
</style>
""", unsafe_allow_html=True)

# Header with emojis in spans for better control
st.markdown('<h1>🌱 UMDAC DATAHACKS 2025 🌱</h1>', unsafe_allow_html=True)
st.markdown("""
<h2 class="subtitle">
    <span style="display: inline-block; transform: translateY(-2px);">🍽️</span> 
    Zero Hunger Challenge 
    <span style="display: inline-block; transform: translateY(-2px);">🌍</span>
</h2>
""", unsafe_allow_html=True)

# Start Analysis Button - Mega version
st.markdown("""
<div style="text-align: center;">
    <button class="mega-button" onclick="this.blur();">
        Start Analysis
    </button>
</div>
""", unsafe_allow_html=True)

# Main content
col1, col2 = st.columns([1, 1])

with col1:
    try:
        image = Image.open("background.png")
        st.image(image, use_container_width=True)
    except Exception as e:
        st.error("⚠️ Error loading image. Please ensure 'background.png' is in the same directory as the app.")

with col2:
    st.markdown("""
    <div class="content-section">
        <div class="highlight-text">SDG Goal 2: Zero Hunger</div>
        <h3 style="color: #2e7d32; font-size: 2rem; margin-bottom: 1rem;">Data-Driven Solutions for a Hunger-Free World</h3>
        <p style="font-size: 1.1rem; color: #333; line-height: 1.6; margin-bottom: 1.5rem;">
            Join us in our mission to combat global hunger through innovative data science and AI solutions. 
            Our platform provides powerful tools to analyze food security, predict crop yields and assess hunger risks 
            across different regions.
        </p>
        <div class="feature-grid">
            <div class="feature-item">
                <span class="feature-icon">📊</span>
                <span>Food Security Analysis</span>
            </div>
            <div class="feature-item">
                <span class="feature-icon">🎯</span>
                <span>Hunger Risk Assessment</span>
            </div>
            <div class="feature-item">
                <span class="feature-icon">🌾</span>
                <span>Crop Yield Prediction</span>
            </div>
            <div class="feature-item">
                <span class="feature-icon">📈</span>
                <span>Market Insights</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Statistics Cards
st.markdown("""
<div class="stats-container">
    <div class="stat-box">
        <div class="stat-number">828M</div>
        <div class="stat-label">People affected by hunger globally in 2021</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">149M</div>
        <div class="stat-label">Children under 5 affected by stunting</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">45M</div>
        <div class="stat-label">Children under 5 suffering from wasting</div>
    </div>
    <div class="stat-box">
        <div class="stat-number">3.1B</div>
        <div class="stat-label">People cannot afford a healthy diet</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Mission Statement moved after statistics
st.markdown("""
<div class="mission-container">
    <h2 style="color: #2e7d32; text-align: center; font-size: 2.5rem; margin-bottom: 1.5rem;">Our Mission</h2>
    <p style="font-size: 1.2rem; color: #333; line-height: 1.8; text-align: center;">
        Aligned with the UN Sustainable Development Goal 2 (Zero Hunger), we are committed to leveraging data science 
        and artificial intelligence to combat global hunger, enhance food security and promote sustainable agriculture. 
        Through predictive analytics and data-driven insights, we aim to support the achievement of SDG targets 2.1, 2.2, 2.3, and 2.c 
        by 2030.
    </p>
</div>
""", unsafe_allow_html=True)

# Data-Driven Solutions Section
st.markdown("""
<div class="mission-container">
    <h2 style="color: #2e7d32; text-align: center; font-size: 2.5rem; margin-bottom: 2rem;">Our Data-Driven Solutions for SDG 2 Targets</h2>
    <div class="solutions-grid">
        <div class="solution-card">
            <div class="solution-icon">📊</div>
            <div class="solution-title">Food Security Index Prediction</div>
            <div class="solution-description">
                Supporting SDG Targets 2.1 & 2.2: Our predictive model helps identify areas at risk of food insecurity, 
                enabling targeted interventions to ensure access to safe and nutritious food while combating malnutrition.
            </div>
        </div>
        <div class="solution-card">
            <div class="solution-icon">🎯</div>
            <div class="solution-title">Hunger Risk Assessment</div>
            <div class="solution-description">
                Addressing SDG Target 2.c: We analyze market dynamics and food commodity accessibility to help stakeholders 
                monitor and stabilize food prices, ensuring timely access to essential nutrition.
            </div>
        </div>
        <div class="solution-card">
            <div class="solution-icon">🌾</div>
            <div class="solution-title">Crop Yield Prediction</div>
            <div class="solution-description">
                Fulfilling SDG Target 2.3: Our advanced analytics help optimize agricultural productivity, 
                particularly benefiting small-scale food producers through data-driven farming insights.
            </div>
        </div>
    </div>
</div>

<div class="mission-container">
    <h2 style="color: #2e7d32; text-align: center; font-size: 2.5rem; margin-bottom: 2rem;">How Our Platform Works</h2>
    <div class="platform-steps">
        <div class="platform-step">
            <strong>1. Food Security Analysis:</strong> Input your region's data to receive FSI predictions and identify potential food security challenges.
        </div>
        <div class="platform-step">
            <strong>2. Risk Assessment:</strong> Explore zone-specific hunger risk scores to understand market dynamics and food accessibility.
        </div>
        <div class="platform-step">
            <strong>3. Agricultural Optimization:</strong> Utilize our crop yield prediction tool to enhance farming productivity and sustainability.
        </div>
        <div class="platform-step">
            <strong>4. Data-Driven Action:</strong> Generate comprehensive reports and recommendations for targeted interventions.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Mission Statement with enhanced design
st.markdown("""
<div class="mission-container">
    <h2 style="color: #2e7d32; text-align: center; font-size: 2.5rem; margin-bottom: 1.5rem;">Our Mission</h2>
    <p style="font-size: 1.2rem; color: #333; line-height: 1.8; text-align: center;">
        Aligned with the UN Sustainable Development Goal 2 (Zero Hunger), we are committed to leveraging data science 
        and artificial intelligence to combat global hunger, enhance food security, and promote sustainable agriculture. 
        Through predictive analytics and data-driven insights, we aim to support the achievement of SDG targets 2.1, 2.2, 2.3, and 2.c 
        by 2030.
    </p>
</div>

<div class="mission-container">
    <h2 style="color: #2e7d32; text-align: center; font-size: 2.5rem; margin-bottom: 1.5rem;">SDG 2 Targets We Address</h2>
    <div class="target-card">
        <h3 style="color: #2e7d32; margin-bottom: 0.5rem;">Target 2.1 & 2.2: End Hunger and Malnutrition</h3>
        <p style="color: #333;">By 2030, end hunger and ensure access by all people to safe, nutritious and sufficient food all year round. End all forms of malnutrition, including achieving the internationally agreed targets on stunting and wasting in children under 5 years of age.</p>
    </div>
    <div class="target-card">
        <h3 style="color: #2e7d32; margin-bottom: 0.5rem;">Target 2.3: Agricultural Productivity</h3>
        <p style="color: #333;">Double the agricultural productivity and incomes of small-scale food producers through secure and equal access to land, resources, and opportunities.</p>
    </div>
    <div class="target-card">
        <h3 style="color: #2e7d32; margin-bottom: 0.5rem;">Target 2.c: Food Market Functionality</h3>
        <p style="color: #333;">Ensure proper functioning of food commodity markets and facilitate timely access to market information to help limit extreme food price volatility.</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Developers section with enhanced design
st.markdown("""
<div class="developers-section">
    <div class="dev-title">Developed by Year 1 Universiti Malaya Data Science Students</div>
    <div class="dev-name">Felicia Sia Xin Rou</div>
    <div class="dev-name">Lau Hiap Meng</div>
    <div class="dev-name">Kenny Ken Wan Jin</div>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = "main"

