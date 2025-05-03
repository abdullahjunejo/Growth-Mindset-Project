import streamlit as st
import random

# ✅ 1. PAGE SETUP (WARRIOR THEME)
st.set_page_config(
    page_title="GROWTH WARRIOR MODE", 
    page_icon="⚔️", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 2. ULTRA-VISIBLE CSS (HEADINGS = GOLD, TEXT = WHITE)
st.markdown("""
<style>
    /* BACKGROUND */
    [data-testid=stAppViewContainer] {
        background: linear-gradient(135deg, #0F0C29 0%, #1A1A2E 100%);
    }

    /* HEADINGS (NOW GOLD INSTEAD OF WHITE) */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;  /* GOLD COLOR */
        font-family: 'Poppins', sans-serif;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.5);
    }

    /* BODY TEXT (SOFT WHITE) */
    p, .stMarkdown, .stText {
        color: #F5F5F5 !important;
    }

    /* CARDS (GLASS EFFECT) */
    .challenge-card {
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        backdrop-filter: blur(5px);
    }

    /* BUTTONS (GLOWING ORANGE) */
    .stButton>button {
        background: linear-gradient(90deg, #FFA500 0%, #FF6347 100%);
        color: black !important;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        box-shadow: 0 4px 15px rgba(255, 165, 0, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# ✅ 3. HEADER (NOW GOLD & BOLD)
st.markdown("""
<div style="text-align: center; padding: 1rem; border-bottom: 2px solid #FFD700;">
    <h1 style="font-size: 3rem;">⚔️ GROWTH WARRIOR MODE</h1>
    <h3 style="color: #FFD700 !important;">Abdullah Junejo, Ready for Battle?</h3>
</div>
""", unsafe_allow_html=True)

# ✅ 4. QUOTE GENERATOR (GOLD BORDER)
st.markdown("## 💬 WARRIOR'S WISDOM")
quote = st.button("🔥 GENERATE MOTIVATION")
if quote:
    quotes = [
        ("\"The only limit is the one you set yourself.\"", "Sun Tzu"),
        ("\"Pressure makes diamonds.\"", "George S. Patton"),
        ("\"Suffer now and live the rest of your life as a champion.\"", "Muhammad Ali")
    ]
    selected_quote, author = random.choice(quotes)
    st.markdown(f"""
    <div class="challenge-card">
        <p style="font-size: 1.2rem; font-style: italic; color: #F5F5F5;">{selected_quote}</p>
        <p style="text-align: right; color: #FFD700;">— {author}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ 5. CHALLENGE ZONE (GLOWING CARDS)
st.markdown("## ⚡ DAILY CHALLENGE")
challenge = st.text_input("What’s your battle today?")
if challenge:
    st.markdown(f"""
    <div class="challenge-card">
        <h4 style="color: #FFD700;">YOUR MISSION:</h4>
        <p>{challenge}</p>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

# ✅ 6. FOOTER (SOCIAL LINKS IN GOLD)
st.markdown("""
<div style="text-align: center; margin-top: 2rem; padding: 1rem; border-top: 1px solid #FFD700;">
    <p style="color: #FFD700;">CONNECT WITH THE WARRIOR:</p>
    <a href="https://github.com/abdullahjunejo" style="color: #FFD700 !important; margin: 0 10px;">GitHub</a>
    <a href="https://facebook.com/abdullah.junejo.737" style="color: #FFD700 !important; margin: 0 10px;">Facebook</a>
    <a href="https://instagram.com/abdullah_junejo__" style="color: #FFD700 !important; margin: 0 10px;">Instagram</a>
</div>
""", unsafe_allow_html=True)
