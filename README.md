# Ai_Code_reviewer
AI Code Reviewer is a Streamlit-based web application that leverages Google's Gemini AI to provide feedback on Python code. It helps developers improve their code by analyzing its quality, performance, readability, maintainability, and security.

🚀 Features
AI-Powered Code Review: Uses Gemini AI to analyze and suggest improvements.
Syntax Validation: Checks for syntax errors before review.
Structured Feedback: Provides clear explanations and Python code blocks when needed.
Streamlit UI: Simple and interactive interface for user-friendly experience.
🛠️ Technologies Used
Python
Streamlit
Google Generative AI (Gemini)
Regular Expressions (re)
🔧 Installation & Setup
# Clone the Repository
git clone https://github.com/Saiphani2105/ai-code-reviewer.git
cd ai-code-reviewer

# Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install Dependencies
pip install -r requirements.txt

# Set Up Google Gemini API Key
# Replace `api_key` in the script with your own Gemini API key.

# Run the Application
streamlit run app.py
🏗️ How to Use
Enter or paste your Python code into the text area.
Click the "🚀 Generate Review" button.
View AI-generated feedback in structured text and code blocks.
🌍 Live Demo
Check out the live version of the application here:

AI Code Reviewer Webpage

⚠️ Important Notes
Ensure that your API key is valid and has the necessary permissions.
Avoid sharing your API key publicly.
📜 License
This project is licensed under the MIT License.

🤝 Contributing
Contributions are welcome! Feel free to open issues and pull requests.
