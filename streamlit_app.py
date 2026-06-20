import streamlit as st
import google.generativeai as genai

# Page settings
st.set_page_config(
    page_title="AI Water Conservation Assistant",
    page_icon="💧",
    layout="centered"
)

# Load Gemini API key from secrets.toml
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

# Use supported Gemini model
model = genai.GenerativeModel("gemini-3.5-flash")

# App UI
st.title("💧 AI Water Conservation Assistant")

st.write(
    "Ask questions about water conservation, sanitation, rainwater harvesting, "
    "water pollution, and sustainable water use."
)

with st.expander("Example Questions"):
    st.write("• How can I save water at home?")
    st.write("• What is rainwater harvesting?")
    st.write("• Why is clean water important?")
    st.write("• How can schools conserve water?")
    st.write("• What causes water pollution?")

user_input = st.text_area(
    "Enter your question:",
    placeholder="Example: How can I save water in daily life?"
)

if st.button("Get Advice"):
    if user_input.strip() == "":
        st.warning("Please enter a question first.")
    else:
        prompt = f"""
        You are an AI Water Conservation Assistant for SDG 6: Clean Water and Sanitation.

        Your task is to answer only questions related to:
        - Water conservation
        - Clean water
        - Sanitation
        - Rainwater harvesting
        - Water pollution
        - Sustainable water usage
        - Water saving tips for homes, schools, and communities

        Rules:
        1. Give simple, clear, student-friendly answers.
        2. Keep the answer informative but easy to understand.
        3. If the question is unrelated to water or sanitation, politely say:
           "I can only help with water conservation and sanitation related questions."

        User question:
        {user_input}
        """

        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
