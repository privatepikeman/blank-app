import streamlit as st
import requests

# Set the page title
st.set_page_config(page_title="AI Assistant")

# Add a title to the app
st.title("AI Assistant")

# Read the base URL from a local text file
def get_base_url():
    try:
        with open("base_url.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        st.error("Base URL file not found. Please ensure 'base_url.txt' exists in the app directory.")
        return None

base_url = get_base_url()

# Create a text area for user input
user_input = st.text_area("Enter your paragraph:", "", height=150)

# Add a button
if st.button("Query"):
    # Handle the button click
    if user_input.strip():
        if base_url:
            try:
                # Perform the GET request
                response = requests.get(
                    f"{base_url}/webhook/1c5a3ba4-8b0b-40b5-ad63-6d956845a342",
                    params={"query": user_input},
                    headers={"X-TOKEN": "78093019A"}
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
            st.write("Cannot query without a valid base URL.")
    else:
        st.write("Please enter a paragraph to query.")
