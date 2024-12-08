import streamlit as st

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
        st.write(f"You entered: {user_input}")
    else:
        st.write("Please enter a paragraph to query.")
