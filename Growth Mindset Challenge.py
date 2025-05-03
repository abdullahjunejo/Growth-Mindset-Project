import streamlit as st
import random

# Set ultra-premium page config
st.set_page_config(
    page_title="GROWTH MINDSET PRO", 
    page_icon="🔥", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Vibrant CSS styling
st.markdown("""
<style>
    [data-testid=stAppViewContainer] {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        color: white;
        font-family: 'Montserrat', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #fca311 !important;
        font-family: 'Poppins', sans-serif;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .quote-card {
        background: rgba(255,255,255,0.1);
        border-left: 4px solid #fca311;
        padding: 1.5rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }
    .stButton>button {
        background: linear-gradient(90deg, #fca311 0%, #e85d04 100%);
        color: #000 !important;
        font-weight: 800;
        border: none;
        border-radius: 30px;
        padding: 12px 28px;
        box-shadow: 0 4px 15px rgba(252, 163, 17, 0.3);
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background: rgba(255,255,255,0.1);
        border: 2px solid #fca311;
        color: white;
        border-radius: 8px;
        padding: 10px;
    }
    .challenge-card {
        background: rgba(22, 33, 62, 0.8);
        border: 1px solid #fca311;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }
    .stProgress>div>div>div {
        background: linear-gradient(90deg, #fca311 0%, #e85d04 100%);
    }
    .social-link {
        color: #fca311 !important;
        font-weight: 600;
        margin: 0 10px;
        text-decoration: none;
    }
    .social-link:hover {
        color: #ffd166 !important;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Header with striking design
st.markdown("""
<div style="text-align: center; padding: 2rem 0; border-bottom: 2px solid #fca311;">
    <h1 style="font-size: 3.5rem; margin-bottom: 0.5rem;">GROWTH MINDSET PRO</h1>
    <h2 style="color: #fff !important; font-size: 1.8rem;">Welcome to Your Evolution, Abdullah Junejo</h2>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(252, 163, 17, 0.1); padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0;">
    <p style="font-size: 1.2rem; color: #fff; text-align: center;">
    <strong>EMBRACE THE GRIND:</strong> Challenges are just opportunities in disguise. 
    This elite system will transform your mindset through daily practice.
    </p>
</div>
""", unsafe_allow_html=True)

# Quote generator with premium design
st.markdown("## DAILY MINDSET FUEL")
col1, col2 = st.columns([3,1])
with col2:
    if st.button("GENERATE QUOTE 🔥", key="quote_button"):
        quotes = [
            ("\"The only limit to our realization of tomorrow is our doubts of today.\"", "Franklin D. Roosevelt"),
            ("\"You don't have to be great to start, but you have to start to be great.\"", "Zig Ziglar"),
            ("\"Success is stumbling from failure to failure with no loss of enthusiasm.\"", "Winston Churchill"),
            ("\"Your potential is endless. Go do what you were created to do.\"", "Unknown"),
            ("\"The expert in anything was once a beginner.\"", "Helen Hayes")
        ]
        quote, author = random.choice(quotes)
        st.session_state.current_quote = (quote, author)

with col1:
    if 'current_quote' in st.session_state:
        quote, author = st.session_state.current_quote
        st.markdown(f"""
        <div class="quote-card">
            <p style="font-size: 1.4rem; font-style: italic; color: #fff;">{quote}</p>
            <p style="text-align: right; font-weight: 600; color: #fca311;">— {author}</p>
        </div>
        """, unsafe_allow_html=True)

# Challenge section with premium design
st.markdown("## CHALLENGE WARRIOR ZONE")
with st.container():
    user_input = st.text_input("DESCRIBE YOUR CURRENT BATTLE:", placeholder="What's testing you today?")
    difficulty = st.select_slider("DIFFICULTY LEVEL:", 
                                options=["WARMUP", "MODERATE", "TOUGH", "BRUTAL", "LEGENDARY"],
                                value="MODERATE")

    if user_input:
        encouragement = {
            "WARMUP": "Good warmup! Now push harder!",
            "MODERATE": "This will stretch you nicely!",
            "TOUGH": "Growth happens outside comfort zones!",
            "BRUTAL": "This will forge you into something greater!",
            "LEGENDARY": "Legendary challenges create legendary warriors!"
        }
        st.markdown(f"""
        <div class="challenge-card">
            <h4 style="color: #fca311;">YOUR CHALLENGE</h4>
            <p style="font-size: 1.1rem; color: #fff;">{user_input}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span style="background: #e85d04; color: white; padding: 4px 12px; border-radius: 20px; font-weight: 600;">{difficulty}</span>
                <p style="font-style: italic; color: #fca311; margin: 0;">{encouragement[difficulty]}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# Reflection section
st.markdown("## WARRIOR'S JOURNAL")
with st.expander("RECORD TODAY'S LESSONS", expanded=False):
    mood = st.radio("TODAY'S MINDSET:", ("🔥 ON FIRE", "💪 STRONG", "🛡️ RESILIENT", "🏆 VICTORIOUS"))
    reflection = st.text_area("KEY INSIGHTS:", height=150, placeholder="What did the battle teach you today?")
    
    if reflection:
        st.success("LESSONS ARCHIVED!")
        st.image("https://media.giphy.com/media/l0HU7JI1nSwE6yjeU/giphy.gif", width=200)

# Achievement tracker
st.markdown("## VICTORY LOG")
achievement = st.text_input("RECORD YOUR WIN:")
if achievement:
    st.markdown(f"""
    <div class="challenge-card" style="border-color: #06d6a0;">
        <h4 style="color: #06d6a0;">🏆 VICTORY</h4>
        <p style="font-size: 1.1rem; color: #fff;">{achievement}</p>
    </div>
    """, unsafe_allow_html=True)
    
    progress = st.slider("PROGRESS TO NEXT LEVEL:", 0, 100, 25)
    st.progress(progress)
    if progress >= 80:
        st.balloons()
        st.markdown("""
        <div style="text-align: center; margin: 1rem 0;">
            <p style="color: #fca311; font-weight: 600; font-size: 1.2rem;">
            ALMOST THERE! PUSH THROUGH!
            </p>
        </div>
        """, unsafe_allow_html=True)

# Daily challenge
st.markdown("## TODAY'S MISSION")
challenges = [
    "Conquer one fear outside your comfort zone",
    "Train a skill for 45 minutes with full intensity",
    "Study the biography of someone who overcame great obstacles",
    "Help another warrior with their challenge",
    "Identify and eliminate one limiting belief"
]
daily_challenge = random.choice(challenges)
st.markdown(f"""
<div class="challenge-card" style="border-color: #118ab2;">
    <h4 style="color: #118ab2;">⚔️ MISSION BRIEFING</h4>
    <p style="font-size: 1.2rem; color: #fff; font-weight: 600;">{daily_challenge}</p>
</div>
""", unsafe_allow_html=True)

if st.button("MISSION COMPLETE ✅", key="challenge_button"):
    st.success("WARRIOR UPGRADED!")
    st.balloons()
    st.image("https://media.giphy.com/media/3o7TKSjRrfIPjeiVyM/giphy.gif", width=200)

# Premium footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem 0; border-top: 2px solid #fca311;">
    <h3 style="color: #fca311 !important;">CONTINUE YOUR JOURNEY</h3>
    <p style="color: #fff;">The warrior's path never ends - only evolves</p>
    <div style="margin: 1.5rem 0;">
        <a href="https://github.com/abdullahjunejo" class="social-link" target="_blank">GITHUB</a>
        <a href="https://www.facebook.com/abdullah.junejo.737/" class="social-link" target="_blank">FACEBOOK</a>
        <a href="https://www.instagram.com/abdullah_junejo__/" class="social-link" target="_blank">INSTAGRAM</a>
    </div>
    <p style="color: rgba(255,255,255,0.6); font-size: 0.8rem;">© 2023 WARRIOR MINDSET SYSTEMS</p>
</div>
""", unsafe_allow_html=True)
