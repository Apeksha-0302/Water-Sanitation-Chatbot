import streamlit as st
import google.generativeai as genai

# Add your Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

st.title("💧 AI Water Conservation Assistant")

user_input = st.text_area(
    "Ask a question about water conservation and sanitation:"
)

if st.button("Get Advice"):
    if user_input:
        prompt = f"""
        You are a Water Conservation Assistant.

        Answer the user's question about:
        - Water Conservation
        - Clean Water
        - Sanitation
        - Rainwater Harvesting
        - Water Pollution

        User Question:
        {user_input}
        """

        response = model.generate_content(prompt)

        st.subheader("AI Response")
        st.write(response.text)
