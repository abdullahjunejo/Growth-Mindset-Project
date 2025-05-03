import streamlit as st
import random

# ✅ 1. DARK BLUE BACKGROUND (NO MORE VISIBILITY ISSUES)
st.set_page_config(
    page_title="GROWTH WARRIOR PRO", 
    page_icon="⚡", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ 2. CHATGPT-APPROVED COLORS (HEADINGS = YELLOW, TEXT = WHITE)
st.markdown("""
<style>
    /* DARK BLUE BACKGROUND */
    [data-testid=stAppViewContainer] {
        background: #0A1128 !important;
    }

    /* HEADINGS = BRIGHT YELLOW (NO MORE WHITE!) */
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important;
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 4px #000000;
    }

    /* BODY TEXT = BOLD WHITE */
    p, .stMarkdown, .stText {
        color: #FFFFFF !important;
        font-weight: bold;
    }

    /* CARDS = GLASS EFFECT */
    .warrior-card {
        background: rgba(10, 25, 47, 0.7);
        border: 2px solid #FF4500;
        border-radius: 15px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: 0 0 10px rgba(255, 69, 0, 0.5);
    }

    /* BUTTONS = GLOWING RED */
    .stButton>button {
        background: linear-gradient(90deg, #FF0000 0%, #FF4500 100%);
        color: white !important;
        font-weight: bold;
        border: none;
        border-radius: 30px;
        box-shadow: 0 0 15px rgba(255, 0, 0, 0.6);
    }
</style>
""", unsafe_allow_html=True)

# ✅ 3. HEADER (NOW SUPER VISIBLE)
st.markdown("""
<div style="text-align: center; padding: 2rem 0; border-bottom: 3px solid #FFD700;">
    <h1 style="font-size: 3.5rem;">⚡ GROWTH WARRIOR PRO</h1>
    <h3 style="color: #FFD700 !important;">Abdullah Junejo - Ready to Dominate?</h3>
</div>
""", unsafe_allow_html=True)

# ✅ 4. QUOTE GENERATOR (YELLOW TEXT)
st.markdown("## 💬 WARRIOR QUOTE")
if st.button("🔥 GENERATE POWER QUOTE"):
    quotes = [
        ("\"No pain, no gain. Simple.\"", "The Rock"),
        ("\"Hard work beats talent.\"", "Kevin Durant"),
        ("\"Suffer now, rule later.\"", "Conor McGregor")
    ]
    quote, author = random.choice(quotes)
    st.markdown(f"""
    <div class="warrior-card">
        <p style="font-size: 1.5rem; color: #FFD700 !important;">{quote}</p>
        <p style="text-align: right; color: #FF6347;">— {author}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ 5. CHALLENGE SECTION (GLOWING BORDERS)
st.markdown("## ⚔️ TODAY'S CHALLENGE")
challenge = st.text_input("What will you conquer today?")
if challenge:
    st.markdown(f"""
    <div class="warrior-card">
        <h4 style="color: #FFD700;">YOUR BATTLE:</h4>
        <p style="font-size: 1.2rem;">{challenge}</p>
    </div>
    """, unsafe_allow_html=True)
    st.balloons()

# ✅ 6. FOOTER (SOCIAL LINKS IN RED)
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 1.5rem; border-top: 3px solid #FF4500;">
    <p style="color: #FFD700; font-weight: bold;">FOLLOW THE WARRIOR:</p>
    <a href="https://github.com/abdullahjunejo" style="color: #FF6347 !important; margin: 0 15px; font-weight: bold; text-decoration: none;">GitHub</a>
    <a href="https://facebook.com/abdullah.junejo.737" style="color: #FF6347 !important; margin: 0 15px; font-weight: bold; text-decoration: none;">Facebook</a>
    <a href="https://instagram.com/abdullah_junejo__" style="color: #FF6347 !important; margin: 0 15px; font-weight: bold; text-decoration: none;">Instagram</a>
</div>
""", unsafe_allow_html=True)
