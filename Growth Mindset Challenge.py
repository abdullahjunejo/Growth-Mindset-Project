import streamlit as st
import random

# Set page config with your name
st.set_page_config(page_title="Growth Mindset Project", page_icon="★", layout="wide")

# Cool gradient background - changed to blue/purple gradient
st.markdown("""
<style>
    [data-testid=stAppViewContainer] {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Title with animation
st.title("🌟 Growth Mindset Challenge 🌟")
st.header("✶ Welcome to your growth journey, Abdullah Junejo!")
st.write("""
Embrace challenges, learn from mistakes, and unlock your full potential. 
This AI-powered app helps you build a growth mindset with reflection, 
challenges, and achievements!
""")

# Interactive quote generator
st.header("💡 Daily Growth Mindset Boost")
quotes = [
    ("\"The only limit to our realization of tomorrow is our doubts of today.\" - Franklin D. Roosevelt"),
    ("\"You don't have to be great to start, but you have to start to be great.\" - Zig Ziglar"),
    ("\"Success is stumbling from failure to failure with no loss of enthusiasm.\" - Winston Churchill"),
    ("\"Your potential is endless. Go do what you were created to do.\" - Unknown"),
    ("\"The expert in anything was once a beginner.\" - Helen Hayes")
]

if st.button("Generate Random Quote ✨"):
    quote = random.choice(quotes)
    st.markdown(f'<p class="big-font">{quote}</p>', unsafe_allow_html=True)
else:
    st.write("Click the button above for motivational boost!")

# Challenge section with difficulty selector
st.header("🔧 Challenge Zone")
user_input = st.text_input("Describe a challenge you're facing:")
difficulty = st.select_slider("Rate the difficulty level:", 
                            options=["Easy", "Medium", "Hard", "Very Hard", "Extreme"])

if user_input:
    encouragement = {
        "Easy": "You've got this! Smooth sailing ahead!",
        "Medium": "A good stretch for your abilities!",
        "Hard": "This will make you stronger!",
        "Very Hard": "The bigger the challenge, the greater the growth!",
        "Extreme": "Legendary challenges create legendary people!"
    }
    st.success(f"**Challenge:** {user_input} ({difficulty})")
    st.balloons()
    st.write(encouragement[difficulty])

# Reflection with mood selector
st.header("🧠 Reflection Corner")
mood = st.radio("How are you feeling about your progress?",
               ("😊 Positive", "😐 Neutral", "😕 Challenged", "😍 Excited"))
reflection = st.text_area("What did you learn today?")

if reflection:
    st.success("### ✨ Reflection Saved!")
    st.image("https://media.giphy.com/media/LpiVeIRgrqVsZJpM5H/giphy.gif", width=200)

# Achievement tracker with progress bar
st.header("🏆 Achievement Tracker")
achievement = st.text_input("Share something you've accomplished recently")
if achievement:
    st.success(f"🎉 Celebrating: {achievement}")
    progress = st.slider("How close are you to your next big goal?", 0, 100, 25)
    st.progress(progress)
    if progress >= 80:
        st.balloons()
        st.write("Almost there! Keep pushing!")

# Daily challenge generator
st.header("🚀 Today's Growth Challenge")
challenges = [
    "Learn something new outside your comfort zone",
    "Help someone else with their challenge",
    "Journal about a recent failure and what it taught you",
    "Practice a skill for 30 minutes",
    "Ask for feedback on your work"
]
daily_challenge = random.choice(challenges)
st.write(f"Your challenge today: **{daily_challenge}**")
if st.button("I completed this challenge!"):
    st.success("Awesome! You're growing every day!")
    st.balloons()

# Personal growth tracker (hidden until used)
with st.expander("📈 Personal Growth Tracker (Click to Expand)"):
    weeks = st.slider("Track your progress over weeks", 1, 52, 4)
    st.write(f"Over {weeks} weeks, you've grown in:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.checkbox("Resilience")
        st.checkbox("Creativity")
    with col2:
        st.checkbox("Knowledge")
        st.checkbox("Confidence")
    with col3:
        st.checkbox("Skills")
        st.checkbox("Positivity")

# Footer with social links
st.write("---")
st.markdown("### Keep growing, Abdullah Junejo!")
st.write("Growth is a journey - enjoy every step!")
st.markdown("""
Connect with me:
[GitHub](https://github.com/abdullahjunejo) | 
[Facebook](https://www.facebook.com/abdullah.junejo.737/) | 
[Instagram](https://www.instagram.com/abdullah_junejo__/)
""")
