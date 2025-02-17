import streamlit as st
import google.generativeai as genai

# Securely fetch API key
if "api_key" not in st.secrets:
    st.error("API Key not found. Please set it in your Hugging Face secrets.")
else:
    key = st.secrets["api_key"]
    genai.configure(api_key=key)

def review_code(user_prompt):
    try:
        system_prompt ="""This system is strictly designed for reviewing code and providing feedback on potential bugs, along with suggestions for fixes. 
    Supported languages include Python, Java, C, C++, C#, JavaScript, HTML & CSS, TypeScript, PHP, Ruby, Go, R, Julia, SQL, Swift, Kotlin, Dart, Rust, and Shell scripting.
    If a user asks unrelated questions, politely remind them to focus on coding-related topics.
    Explanations should be clear and concise, providing corrected code where necessary."""
        
        model = genai.GenerativeModel(
            model_name="models/gemini-2.0-flash-exp",
            system_instruction=system_prompt
        )
        response = model.generate_content(user_prompt)
        return response.text if hasattr(response, "text") else "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("AI-Powered Code Reviewer")
st.write("Optimize, debug, and enhance your code effortlessly.")

code = st.text_area("Enter your code:", placeholder="Paste your code here...")

if st.button("Review Code"):
    if code.strip():
        with st.spinner("Analyzing your code..."):
            review_result = review_code(code)
        st.subheader("Here's my review and suggestion")
        st.text_area("Review Output", review_result, height=300)
    else:
        st.warning("Please enter a valid code snippet.")
