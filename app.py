import streamlit as st
import pandas as pd
from PIL import Image
from model_loader import ModelLoader

# Set page config
st.set_page_config(
    page_title="Zero Hunger DataHacks",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state for navigation and data
if 'page' not in st.session_state:
    st.session_state.page = 'main'
if 'selected_country' not in st.session_state:
    st.session_state.selected_country = None

# Load the dataset once
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('hunger.csv')
        return sorted(df['Area'].unique().tolist())
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return []

# Get unique countries
countries = load_data()

def main_page():
    # 1. UMDAC DATAHACKS 2025
    st.markdown('<h1>🌱 UMDAC DATAHACKS 2025 🌱</h1>', unsafe_allow_html=True)
    
    # 2. Zero Hunger Challenge
    st.markdown("""
    <h2 class="subtitle">
        <span style="display: inline-block; transform: translateY(-2px);">🍽️</span> 
        Zero Hunger Challenge 
        <span style="display: inline-block; transform: translateY(-2px);">🌍</span>
    </h2>
    """, unsafe_allow_html=True)

    # Custom CSS for the enhanced button
    st.markdown("""
    <style>
    div[data-testid="stButton"] > button {
        font-family: 'Poppins', sans-serif !important;
        font-size: 2rem !important;
        font-weight: 600 !important;
        padding: 2rem 4rem !important;
        width: 100% !important;
        border-radius: 100px !important;
        background: linear-gradient(-45deg, #1b5e20, #2e7d32, #388e3c, #43a047) !important;
        background-size: 400% 400% !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                    inset 0 2px 20px rgba(255, 255, 255, 0.2) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        letter-spacing: 4px !important;
        text-transform: uppercase !important;
        position: relative !important;
        overflow: hidden !important;
        cursor: pointer !important;
        animation: gradientBG 8s ease infinite, pulse 2s infinite !important;
    }

    div[data-testid="stButton"] > button:hover {
        transform: translateY(-5px) scale(1.02) !important;
        box-shadow: 0 15px 35px rgba(46, 125, 50, 0.5),
                    inset 0 2px 20px rgba(255, 255, 255, 0.3) !important;
        letter-spacing: 6px !important;
    }

    div[data-testid="stButton"] > button::before {
        content: '🚀' !important;
        position: absolute !important;
        left: 30px !important;
    }

    div[data-testid="stButton"] > button::after {
        content: '→' !important;
        position: absolute !important;
        right: 30px !important;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes pulse {
        0% {
            box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                        inset 0 2px 20px rgba(255, 255, 255, 0.2),
                        0 0 0 0 rgba(46, 125, 50, 0.4);
        }
        70% {
            box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                        inset 0 2px 20px rgba(255, 255, 255, 0.2),
                        0 0 0 20px rgba(46, 125, 50, 0);
        }
        100% {
            box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                        inset 0 2px 20px rgba(255, 255, 255, 0.2),
                        0 0 0 0 rgba(46, 125, 50, 0);
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # 3. Start Analysis Button - Enhanced version
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button('START ANALYSIS', key='start_analysis', use_container_width=True):
            st.session_state.page = 'analysis'
            st.rerun()

    # 4. Scroll Down Indicator
    st.markdown("""
    <div class="scroll-indicator">
        <div class="scroll-text">⌄ scroll down for more information ⌄</div>
    </div>
    """, unsafe_allow_html=True)

    # 5. Background Image and SDG Goal 2 Statistics
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

def analysis_page():
    # Enhanced Styling with Book Animations
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&display=swap');

    /* Reset and base styles */
    .stApp {
        background: linear-gradient(135deg, #f6f4af 0%, #f0edb1 100%);
    }

    /* Main title styles */
    .main-title {
        color: #2e7d32;
        font-size: 4rem;
        font-weight: 700;
        text-align: center;
        margin: 2rem 0 1rem;
        font-family: 'Playfair Display', serif;
        text-shadow: 2px 2px 4px rgba(46, 125, 50, 0.2);
        background: linear-gradient(45deg, #2e7d32, #388e3c);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .main-subtitle {
        color: #1b5e20;
        font-size: 1.8rem;
        text-align: center;
        margin-bottom: 2rem;
        font-family: 'Playfair Display', serif;
        line-height: 1.4;
    }

    /* Country selection styles */
    .country-selection-container {
        background: linear-gradient(to right bottom, #ffffff 0%, #f8f9fa 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0 10px 30px rgba(46, 125, 50, 0.1);
        text-align: center;
        border: 2px solid rgba(46, 125, 50, 0.1);
        transition: all 0.3s ease;
    }

    .country-selection-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(46, 125, 50, 0.15);
    }

    .selection-title {
        color: #2e7d32;
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }

    .selection-subtitle {
        color: #1b5e20;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        line-height: 1.6;
    }

    /* Book styles */
    .book-container {
        perspective: 1000px;
        margin: 2rem auto;
        width: 100%;
        max-width: 1200px;
        display: none;
    }

    .book-container.visible {
        display: block;
        animation: fadeIn 0.6s ease-out;
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Content styles */
    .chapter-title {
        color: #2e7d32;
        font-family: 'Playfair Display', serif;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 25px;
        position: relative;
        padding-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(46, 125, 50, 0.1);
    }

    .quote-box {
        background: linear-gradient(135deg, #f0f9f0 0%, #ffffff 100%);
        border-left: 4px solid #2e7d32;
        padding: 25px;
        margin: 25px 0;
        border-radius: 0 20px 20px 0;
        color: #1b5e20;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 20px;
        line-height: 1.8;
        box-shadow: 5px 5px 20px rgba(46, 125, 50, 0.1);
    }

    .info-box {
        background: linear-gradient(135deg, rgba(46, 125, 50, 0.08) 0%, rgba(46, 125, 50, 0.03) 100%);
        border-radius: 20px;
        padding: 30px;
        margin: 25px 0;
        color: #1b5e20;
    }

    .fact-item {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        padding: 15px;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        transition: all 0.3s ease;
    }

    .fact-item:hover {
        transform: translateX(10px);
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 5px 15px rgba(46, 125, 50, 0.1);
    }

    .fact-icon {
        margin-right: 15px;
        font-size: 24px;
    }

    .section-heading {
        color: #2e7d32;
        font-family: 'Playfair Display', serif;
        font-size: 24px;
        font-weight: 600;
        margin-bottom: 20px;
    }

    .fancy-text {
        font-size: 18px;
        line-height: 1.8;
        color: #333;
        margin-bottom: 20px;
        padding-left: 20px;
        border-left: 3px solid #2e7d32;
    }
    </style>
    """, unsafe_allow_html=True)

    # Back button
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("← Back", use_container_width=True):
            st.session_state.page = 'main'
            st.rerun()

    # Main title and subtitle
    st.markdown('<h1 class="main-title">Begin Your Journey</h1>', unsafe_allow_html=True)
    st.markdown('<div class="main-subtitle">Explore the path to understanding and combating hunger across the globe 🌍</div>', unsafe_allow_html=True)

    # Country Selection First
    st.markdown("""
    <div class="country-selection-container">
        <div class="selection-title">Choose Your Focus Country</div>
        <div class="selection-subtitle">
            Select a country to begin your exploration of its hunger challenges and potential solutions.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Country selection with custom styling
    selected_country = st.selectbox(
        "",  # Empty label since we have the title in HTML
        countries,
        key="country_select",
        index=0
    )

    if selected_country:
        st.markdown(f"""
        <div style="text-align: center; margin: 1rem 0; color: #2e7d32; font-size: 1.2rem;">
            You selected: <strong>{selected_country}</strong>
        </div>
        """, unsafe_allow_html=True)

        # Start Journey Button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            start_journey = st.button("Start Your Journey →", type="primary", use_container_width=True)
            
            if start_journey:
                st.session_state.selected_country = selected_country
                if 'journey_started' not in st.session_state:
                    st.session_state.journey_started = True
                    st.session_state.current_page = 1
                st.rerun()

    # Show the book interface only after country selection
    if 'journey_started' in st.session_state:
        st.markdown(f"""
        <div class="book-container visible">
            <div class="book">
                <div class="page active">
                    <div class="chapter-title">📚 Understanding {selected_country}'s Challenge</div>
                    <div class="fancy-text">
                        Let's explore the unique challenges and opportunities in {selected_country}'s fight against hunger.
                    </div>
                    <div class="quote-box">
                        "Every country faces unique challenges in achieving zero hunger. Understanding these specific 
                        challenges is the first step toward creating effective solutions."
                    </div>
                    <div class="info-box">
                        <div class="section-heading">Key Facts about {selected_country}</div>
                        <div class="fact-item"><span class="fact-icon">📊</span>Population and Demographics</div>
                        <div class="fact-item"><span class="fact-icon">🌾</span>Agricultural Overview</div>
                        <div class="fact-item"><span class="fact-icon">🏦</span>Economic Context</div>
                        <div class="fact-item"><span class="fact-icon">🌡️</span>Environmental Factors</div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Navigation buttons
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Continue to Analysis →", type="primary", use_container_width=True):
                st.session_state.page = 'result'
                st.rerun()

def result_page():
    # Add navigation buttons
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if st.button("← Back to Selection"):
            st.session_state.page = 'analysis'
            st.rerun()

    st.title(f"Analysis Results: {st.session_state.selected_country}")
    
    # Initialize model loader if not in session state
    if 'model_loader' not in st.session_state:
        st.session_state.model_loader = ModelLoader()
        st.session_state.model_loader.load_models()
    
    # Create tabs for different analyses
    tab1, tab2, tab3 = st.tabs([
        "Food Security Index", 
        "Hunger Risk Assessment", 
        "Crop Yield Prediction"
    ])
    
    # Load data for the selected country
    try:
        df = pd.read_csv('hunger.csv')
        country_data = df[df['Area'] == st.session_state.selected_country].iloc[0]
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return
    
    with tab1:
        st.header("Food Security Index Analysis")
        
        # Prepare data for FSI prediction
        fsi_features = ['Production_tonnes_sum', 'Yield_kg_per_ha_mean', 'FSI_Availability']  # Add your actual feature names
        fsi_data = country_data[fsi_features].values.reshape(1, -1)
        
        # Make prediction
        fsi_prediction = st.session_state.model_loader.predict_fsi(fsi_data)
        if fsi_prediction is not None:
            st.success(f"Predicted Food Security Index: {fsi_prediction[0]:.2f}")
            
            # Add interpretation
            st.markdown("""
            ### Interpretation
            The Food Security Index indicates the overall food security level:
            - 0-3: Critical concern
            - 4-6: Moderate concern
            - 7-10: Good standing
            """)
        
    with tab2:
        st.header("Hunger Risk Assessment")
        
        # Prepare data for risk prediction
        risk_features = ['FSI_Access', 'FSI_Utilization']  # Add your actual feature names
        risk_data = country_data[risk_features].values.reshape(1, -1)
        
        # Make prediction
        risk_prediction = st.session_state.model_loader.predict_risk(risk_data)
        if risk_prediction is not None:
            st.warning(f"Predicted Hunger Risk Level: {risk_prediction[0]}")
            
            # Add recommendations
            st.markdown("""
            ### Recommendations
            Based on the risk assessment, consider:
            - Improving food distribution networks
            - Enhancing storage facilities
            - Implementing early warning systems
            """)
        
    with tab3:
        st.header("Crop Yield Prediction")
        
        # Prepare data for yield prediction
        yield_features = ['Temperature Change (°C)', 'FSI_Stability']  # Add your actual feature names
        yield_data = country_data[yield_features].values.reshape(1, -1)
        
        # Make prediction
        yield_prediction = st.session_state.model_loader.predict_yield(yield_data)
        if yield_prediction is not None:
            st.info(f"Predicted Crop Yield: {yield_prediction[0]:.2f} tonnes/ha")
            
            # Add analysis
            st.markdown("""
            ### Analysis
            Factors affecting crop yield:
            - Climate conditions
            - Soil quality
            - Agricultural practices
            - Available technology
            """)

# Main app logic
if st.session_state.page == 'main':
    main_page()
elif st.session_state.page == 'analysis':
    analysis_page()
elif st.session_state.page == 'result':
    result_page()

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Global Styles */
.stApp {
    background: linear-gradient(135deg, #f6f4af 0%, #f0edb1 100%);
    font-family: 'Poppins', sans-serif;
}

/* Title styling without animation */
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
    text-shadow: 4px 4px 8px rgba(0,0,0,0.1);
    letter-spacing: 2px;
}

/* Enhanced Start Analysis Button */
div[data-testid="column"]:nth-of-type(2) .stButton > button {
    font-size: 2rem !important;
    font-weight: 600 !important;
    padding: 2rem 4rem !important;
    margin: 3rem auto !important;
    width: 100% !important;
    border-radius: 100px !important;
    background: linear-gradient(-45deg, #1b5e20, #2e7d32, #388e3c, #43a047) !important;
    background-size: 400% 400% !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                inset 0 2px 20px rgba(255, 255, 255, 0.2) !important;
    transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
    letter-spacing: 4px !important;
    text-transform: uppercase !important;
    position: relative !important;
    overflow: hidden !important;
    animation: gradientBG 8s ease infinite, pulse 2s infinite !important;
}

div[data-testid="column"]:nth-of-type(2) .stButton > button::before {
    content: '🚀' !important;
    position: absolute !important;
    left: 30px !important;
    animation: bounce 2s infinite !important;
}

div[data-testid="column"]:nth-of-type(2) .stButton > button::after {
    content: '→' !important;
    position: absolute !important;
    right: 30px !important;
    animation: slideRight 1.5s infinite !important;
}

div[data-testid="column"]:nth-of-type(2) .stButton > button:hover {
    transform: translateY(-5px) scale(1.02) !important;
    box-shadow: 0 15px 35px rgba(46, 125, 50, 0.5),
                inset 0 2px 20px rgba(255, 255, 255, 0.3) !important;
    letter-spacing: 6px !important;
}

@keyframes gradientBG {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

@keyframes pulse {
    0% {
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                    inset 0 2px 20px rgba(255, 255, 255, 0.2),
                    0 0 0 0 rgba(46, 125, 50, 0.4);
    }
    70% {
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                    inset 0 2px 20px rgba(255, 255, 255, 0.2),
                    0 0 0 20px rgba(46, 125, 50, 0);
    }
    100% {
        box-shadow: 0 8px 25px rgba(46, 125, 50, 0.4),
                    inset 0 2px 20px rgba(255, 255, 255, 0.2),
                    0 0 0 0 rgba(46, 125, 50, 0);
    }
}

@keyframes bounce {
    0%, 100% {
        transform: translateY(0);
    }
    50% {
        transform: translateY(-5px);
    }
}

@keyframes slideRight {
    0%, 100% {
        transform: translateX(0);
        opacity: 1;
    }
    50% {
        transform: translateX(5px);
        opacity: 0.7;
    }
}

/* Subtitle Animation */
@keyframes slideIn {
    0% {
        transform: translateY(20px);
        opacity: 0;
    }
    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 2.2rem !important;
    color: #1b5e20;
    text-align: center;
    margin-top: 0;
    margin-bottom: 2rem;
    font-weight: 600;
    padding: 0 1rem;
    animation: slideIn 1s ease-out;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

/* Content Section Styling */
.content-section {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 0 0 1.5rem 0;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    transform: translateY(0);
    transition: all 0.3s ease;
}

.content-section:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.15);
}

/* Feature Grid Animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.feature-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-top: 2rem;
}

.feature-item {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.2rem;
    background: rgba(46, 125, 50, 0.1);
    border-radius: 15px;
    transition: all 0.3s ease;
    animation: fadeInUp 0.6s ease-out;
    animation-fill-mode: both;
}

.feature-item:hover {
    transform: translateX(10px);
    background: rgba(46, 125, 50, 0.15);
    box-shadow: 0 5px 15px rgba(46, 125, 50, 0.1);
}

.feature-icon {
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    box-shadow: 0 4px 10px rgba(46, 125, 50, 0.2);
    transition: all 0.3s ease;
}

.feature-item:hover .feature-icon {
    transform: scale(1.1) rotate(360deg);
}

/* Stats Container Animation */
@keyframes scaleIn {
    from {
        transform: scale(0.9);
        opacity: 0;
    }
    to {
        transform: scale(1);
        opacity: 1;
    }
}

.stats-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin: 3rem 0;
    animation: scaleIn 0.8s ease-out;
}

.stat-box {
    background: white;
    border-radius: 20px;
    padding: 2.5rem;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(46, 125, 50, 0.1);
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
    transition: transform 0.4s ease;
}

.stat-box:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(46, 125, 50, 0.15);
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
    position: relative;
    display: inline-block;
}

.stat-label {
    font-size: 1.2rem;
    color: #1b5e20;
    line-height: 1.4;
    font-weight: 500;
}

/* Mission Container Styling */
.mission-container {
    background: rgba(255, 255, 255, 0.95);
    border-radius: 25px;
    padding: 3.5rem;
    margin: 4rem auto;
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    border-left: 5px solid #2e7d32;
    position: relative;
    overflow: hidden;
    transition: all 0.4s ease;
}

.mission-container:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
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

/* Solutions Grid Styling */
.solutions-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2.5rem;
    margin: 3rem 0;
}

.solution-card {
    background: white;
    border-radius: 20px;
    padding: 3rem;
    text-align: center;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    transition: all 0.4s ease;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(46, 125, 50, 0.1);
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
    transition: transform 0.4s ease;
}

.solution-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(46, 125, 50, 0.15);
}

.solution-card:hover::after {
    transform: scaleX(1);
}

.solution-icon {
    font-size: 4rem;
    margin-bottom: 1.5rem;
    transition: transform 0.4s ease;
    display: inline-block;
}

.solution-card:hover .solution-icon {
    transform: scale(1.2) rotate(10deg);
}

.solution-title {
    color: #2e7d32;
    font-weight: 600;
    font-size: 1.6rem;
    margin-bottom: 1.5rem;
}

.solution-description {
    color: #1b5e20;
    font-size: 1.1rem;
    line-height: 1.6;
}

/* Platform Steps Styling */
.platform-steps {
    list-style: none;
    padding: 0;
    margin: 2rem 0;
}

.platform-step {
    color: #1b5e20;
    font-size: 1.2rem;
    line-height: 1.8;
    margin-bottom: 2rem;
    padding-left: 3rem;
    position: relative;
    transition: all 0.3s ease;
}

.platform-step::before {
    content: '→';
    position: absolute;
    left: 0;
    color: #2e7d32;
    font-weight: bold;
    transition: transform 0.3s ease;
}

.platform-step:hover {
    transform: translateX(10px);
}

.platform-step:hover::before {
    transform: translateX(5px);
}

/* Developers Section Styling */
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

/* Rest of your existing CSS */
.highlight-text {
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-size: 1.1rem;
    display: inline-block;
    margin-top: 0 !important;
    margin-bottom: 1rem;
}

.center-button {
    display: flex;
    justify-content: center;
    margin: 2rem 0;
}

.stButton > button {
    font-family: 'Poppins', sans-serif;
    border-radius: 50px !important;
    border: none;
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
    padding: 1rem 2rem;
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    color: white;
    box-shadow: 0 4px 10px rgba(46, 125, 50, 0.2);
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(46, 125, 50, 0.3);
}

.mega-button {
    background: linear-gradient(45deg, #2e7d32 30%, #558b2f 90%);
    color: white;
    font-family: 'Poppins', sans-serif;
    font-size: 2rem !important;
    font-weight: 700;
    padding: 2rem 4rem;
    border-radius: 50px;
    border: none;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(46, 125, 50, 0.3);
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    margin: 3rem auto;
    display: block;
    width: 100%;
    position: relative;
    overflow: hidden;
    text-transform: uppercase;
    letter-spacing: 3px;
    animation: pulse 2s infinite;
}

.mega-button:hover {
    transform: translateY(-5px) scale(1.02);
    box-shadow: 0 10px 30px rgba(46, 125, 50, 0.4);
    animation: none;
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
        rgba(255, 255, 255, 0.3),
        transparent
    );
    transition: 0.5s;
}

.mega-button:hover::before {
    left: 100%;
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

/* Scroll Down Indicator */
.scroll-indicator {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 1.5rem auto;
    animation: fadeInUp 1s ease-out;
}

.scroll-text {
    color: #2e7d32;
    font-family: 'Poppins', sans-serif;
    font-size: 0.9rem;
    font-weight: 400;
    letter-spacing: 3px;
    text-transform: lowercase;
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: pulseText 2s infinite;
    position: relative;
    padding: 0.3rem 1.5rem;
}

.scroll-text::before,
.scroll-text::after {
    content: '';
    position: absolute;
    bottom: -2px;
    width: 0;
    height: 1px;
    background: linear-gradient(45deg, #2e7d32, #558b2f);
    transition: width 0.3s ease;
}

.scroll-text::before {
    left: 50%;
}

.scroll-text::after {
    right: 50%;
}

.scroll-indicator:hover .scroll-text::before,
.scroll-indicator:hover .scroll-text::after {
    width: 50%;
}

@keyframes pulseText {
    0%, 100% {
        opacity: 0.8;
        transform: translateY(0);
    }
    50% {
        opacity: 1;
        transform: translateY(3px);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)
