import streamlit as st
import random
import json

# Load questions and responses from JSON file
def load_finance_qa():
    with open('./__pycache__//config.json') as file:
        return json.load(file)

finance_qa = load_finance_qa()

# Function to generate a random finance-related question
def generate_question():
    return random.choice(list(finance_qa.keys()))

# Function to get the response for a given question
def get_response(question):
    response = finance_qa.get(question, "I'm sorry, I don't have an answer for that question.")
    # Check if response is a URL
    if response.startswith("http"):
        st.write("Redirecting to:", response)
        st.markdown(f'<a href="{response}" target="_blank">Click here to redirect</a>', unsafe_allow_html=True)
    else:
        st.write(f"Response: {response}")

# Streamlit UI
def main():
    st.title("Finance Chatbot")
    st.write("Welcome to the Finance Chatbot! Ask me anything about finance.")

    # Generate a random question button
    if st.button("Generate Random Question"):
        question = generate_question()
        st.write(f"Question: {question}")

    # User input for a specific question
    user_question = st.text_input("Enter your question:")
    if st.button("Get Response"):
        get_response(user_question)

if __name__ == "__main__":
    main()
