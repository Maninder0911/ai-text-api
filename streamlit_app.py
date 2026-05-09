import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process"

st.title("AI Job Agent")

#session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#Input box
user_input = st.text_input("Ask something ...")

if st.button("Send") and user_input:
    # Call your API
    response = requests.post(
        API_URL,
        json={
            "session_id": "user1",
            "input": user_input
        }
    )

    result = response.json()

    # Store messages
    st.session_state.messages.append(("You", user_input))
    st.session_state.messages.append(("AI", result["data"]))

# Display chat
for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")