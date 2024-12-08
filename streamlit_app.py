import streamlit as st
import requests

# Set the page title
st.set_page_config(page_title="AI Assistant")

# Add a title to the app
st.title("AI Assistant")

# Create a text area for user input
user_input = st.text_area("Enter your paragraph:", "", height=150)

# Add a button
if st.button("Query"):
    # Handle the button click
    if user_input.strip():
        try:
            # Perform the GET request
            response = requests.get(
                "https://tender-eagle-19.hooks.n8n.cloud/webhook/1c5a3ba4-8b0b-40b5-ad63-6d956845a342",
                params={"query": user_input}
            )
            if response.status_code == 200:
                # Extract and display the 'Answer' field from the JSON response
                answer = response.json().get("Answer", "No answer provided.")
                st.success(answer)
            else:
                st.write("Failed to fetch the answer. Please try again later.")
        except Exception as e:
            st.write(f"An error occurred: {e}")
    else:
        st.write("Please enter a paragraph to query.")
