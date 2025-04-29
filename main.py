import streamlit as st
import random

# 🎮 Set up the title
st.title("🎮 Rock, Paper, Scissors Game")


# 📝 Game options
choices = ["🪨 Rock", "📄 Paper", "✂ Scissors"]
st.write("create by sobiarao")

# 🧑 User selection
user_choice = st.radio("🧑 Choose your move:", choices)

# 🤖 Computer selection
computer_choice = random.choice(choices)

# 🏆 Function to determine winner
def determine_winner(user, computer):
    # 🤝 Check for a tie
    if user == computer:
        return "🤝 It's a tie!"
    # 🎉 Check if the user wins
    if (user == "Rock" and computer == "Scissors") or \
       (user == "Scissors" and computer == "Paper") or \
       (user == "Paper" and computer == "Rock"):
        return "🎉 Congratulations! You win!"
    # 😢 Otherwise, the computer wins
    return "😢 Computer wins!"

# ▶ Play button
if st.button("▶ Play"):
    st.write(f"🧑 You chose: *{user_choice}*")
    st.write(f"🤖 Computer chose: *{computer_choice}*")
    st.subheader(determine_winner(user_choice, computer_choice))

# 🔄 Add a reset button
if st.button("🔄 Reset Game"):
    st.rerun()