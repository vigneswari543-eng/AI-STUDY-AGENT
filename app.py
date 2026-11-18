
import streamlit as st
from agent import ask_ai

# Page settings
st.set_page_config(
    page_title="AI Study Agent",
    page_icon="🎓",
    layout="centered"
)

# Main heading
st.title("🎓 AI Study Agent")
st.write("Your personal AI-powered study assistant!")

# Sidebar
st.sidebar.title("Study Menu")

feature = st.sidebar.selectbox(
    "Choose a feature",
    [
        "AI Doubt Solver",
        "Subject Explanation",
        "Notes Generator",
        "Quiz Generator",
        "Coding Assistant",
        "Exam Preparation"
    ]
)

# Feature instructions
instructions = {
    "AI Doubt Solver": "Answer this student doubt clearly: ",
    "Subject Explanation": "Explain this subject in very simple English with examples: ",
    "Notes Generator": "Prepare easy and organized study notes about: ",
    "Quiz Generator": "Create 5 multiple-choice questions with answers about: ",
    "Coding Assistant": "Explain and help solve this programming question: ",
    "Exam Preparation": "Prepare an exam-oriented answer for: "
}

# User input
question = st.text_area(
    "Enter your question or topic:",
    placeholder="Example: Explain inheritance in Java"
)

# Ask AI
if st.button("Generate Answer"):
    if question.strip():
        with st.spinner("AI is thinking..."):
            try:
                answer = ask_ai(
                    instructions[feature] + question
                )
                st.subheader("AI Answer")
                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a question first.")
