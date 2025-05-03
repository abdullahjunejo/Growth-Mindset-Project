import streamlit as st
import random

# Set page config with premium styling
st.set_page_config(
    page_title="Growth Mindset Project", 
    page_icon="★", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium CSS styling
st.markdown("""
<style>
    [data-testid=stAppViewContainer] {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f0 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .big-font {
        font-size:30px !important;
        font-weight: 600;
        font-family: 'Georgia', serif;
        color: #2c3e50;
    }
    .header-font {
        font-family: 'Georgia', serif;
        color: #34495e;
    }
    .stButton>button {
        background: linear-gradient(to right, #3498db, #2c3e50);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        border: 1px solid #bdc3c7;
    }
    .stSelectSlider>div {
        color: #2c3e50;
    }
    .stProgress>div>div>div {
        background: linear-gradient(to right, #3498db, #2c3e50);
    }
</style>
""", unsafe_allow_html=True)

# Header with premium look
st.title("🌟 Growth Mindset Mastery")
st.markdown('<h2 class="header-font">✶ Welcome to Your Growth Journey, Abdullah Junejo!</h2>', unsafe_allow_html=True)
st.write("""
<div style="font-size:16px; color:#4a5568;">
Embrace challenges, learn from mistakes, and unlock your full potential. 
This premium app helps you build elite habits with reflection, 
challenges, and achievement tracking.
</div>
""", unsafe_allow_html=True)

# Quote generator with card design
st.markdown('<h2 class="header-font">💎 Daily Mindset Boost</h2>', unsafe_allow_html=True)
quotes = [
    ("\"The only limit to our realization of tomorrow is our doubts of today.\" - Franklin D. Roosevelt"),
    ("\"You don't have to be great to start, but you have to start to be great.\" - Zig Ziglar"),
    ("\"Success is stumbling from failure to failure with no loss of enthusiasm.\" - Winston Churchill"),
    ("\"Your potential is endless. Go do what you were created to do.\" - Unknown"),
    ("\"The expert in anything was once a beginner.\" - Helen Hayes")
]

col1, col2 = st.columns([3,1])
with col2:
    if st.button("Generate Quote ✨", key="quote_button"):
        quote = random.choice(quotes)
        st.session_state.current_quote = quote
with col1:
    if 'current_quote' in st.session_state:
        st.markdown(f"""
        <div style="
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        ">
            <p style="font-size:18px; font-style: italic; color:#2c3e50;">
            {st.session_state.current_quote}
            </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.write("")

# Challenge section with premium cards
st.markdown('<h2 class="header-font">🔥 Challenge Zone</h2>', unsafe_allow_html=True)
with st.container():
    user_input = st.text_input("Describe a challenge you're facing:", placeholder="Type your challenge here...")
    difficulty = st.select_slider("Rate the difficulty level:", 
                                options=["Easy", "Medium", "Hard", "Very Hard", "Extreme"],
                                value="Medium")

    if user_input:
        encouragement = {
            "Easy": "This is your warm-up - build momentum!",
            "Medium": "This will stretch your abilities nicely!",
            "Hard": "Growth happens outside your comfort zone!",
            "Very Hard": "This challenge will transform you!",
            "Extreme": "Legendary challenges forge legendary people!"
        }
        st.markdown(f"""
        <div style="
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            margin: 10px 0;
        ">
            <h4 style="color:#2c3e50;">Your Challenge</h4>
            <p style="font-size:16px;">{user_input}</p>
            <p style="font-weight:600; color:#3498db;">Difficulty: {difficulty}</p>
            <p style="font-style:italic; color:#27ae60;">{encouragement[difficulty]}</p>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()

# Reflection section
st.markdown('<h2 class="header-font">📝 Reflection Journal</h2>', unsafe_allow_html=True)
with st.expander("Daily Reflection (Click to Expand)", expanded=False):
    mood = st.radio("Today's mindset:", ("😊 Positive", "😐 Neutral", "😕 Challenged", "😍 Excited"))
    reflection = st.text_area("Key lessons learned today:", height=150)
    
    if reflection:
        st.success("Reflection saved successfully!")
        st.image("https://media.giphy.com/media/LpiVeIRgrqVsZJpM5H/giphy.gif", width=150)

# Achievement tracker
st.markdown('<h2 class="header-font">🏆 Achievement Tracker</h2>', unsafe_allow_html=True)
achievement = st.text_input("Recent accomplishment:")
if achievement:
    st.markdown(f"""
    <div style="
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        margin: 10px 0;
    ">
        <h4 style="color:#2c3e50;">🎉 Celebrating:</h4>
        <p style="font-size:16px;">{achievement}</p>
    </div>
    """, unsafe_allow_html=True)
    
    progress = st.slider("Progress toward next goal:", 0, 100, 25)
    st.progress(progress)
    if progress >= 80:
        st.balloons()
        st.write("Almost there! Keep pushing!")

# Daily challenge
st.markdown('<h2 class="header-font">🚀 Today\'s Growth Task</h2>', unsafe_allow_html=True)
challenges = [
    "Learn something new outside your comfort zone",
    "Help someone else with their challenge",
    "Journal about a recent failure and what it taught you",
    "Practice a skill for 30 minutes",
    "Ask for constructive feedback on your work"
]
daily_challenge = random.choice(challenges)
st.markdown(f"""
<div style="
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    margin: 10px 0;
">
    <p style="font-weight:600; color:#2c3e50;">{daily_challenge}</p>
</div>
""", unsafe_allow_html=True)

if st.button("Mark as Complete ✓", key="challenge_button"):
    st.success("Excellent work! Growth unlocked!")
    st.balloons()

# Footer with elegant social links
st.write("---")
st.markdown("""
<div style="text-align: center;">
    <h3 style="color:#2c3e50;">Keep Evolving, Abdullah Junejo</h3>
    <p style="color:#7f8c8d;">Excellence is not a destination, but a continuous journey</p>
    <div style="margin-top:20px;">
        <a href="https://github.com/abdullahjunejo" target="_blank" style="margin:0 10px; text-decoration:none; color:#3498db;">GitHub</a>
        <a href="https://www.facebook.com/abdullah.junejo.737/" target="_blank" style="margin:0 10px; text-decoration:none; color:#3498db;">Facebook</a>
        <a href="https://www.instagram.com/abdullah_junejo__/" target="_blank" style="margin:0 10px; text-decoration:none; color:#3498db;">Instagram</a>
    </div>
</div>
""", unsafe_allow_html=True)
