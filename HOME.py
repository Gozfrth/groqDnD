import streamlit as st
import os
from groq import Groq

MY_API_KEY = "insert_api_key_here"

def main():
    # Initialize Groq client
    client = Groq(
        api_key=MY_API_KEY,
    )
    
    # Create a session state to store the conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a Dungeons and Dragons host. You must take in player prompts and provide the most creative scenarios for them to tackle. The player only has 50HP in the beginning with a random default weapon of your choice Limit yourself to 50 words ONLY. The objective of the game is to FAIRLY-EASILY find the one piece and you must restrict the users actions appropriately based on the scenario. There must be some fighting too, with rolling dice and the outputs of the dice. After the second ecounter, reward the player with the one piece and output: \"skoobydoobydoobydo\". IF they find it you will output the following: \"skoobydoobydoobydo\"",
            }
        ]

    # Input field for user text
    input = st.text_input("INPUT")
    
    chat_completion = ""

    if input:
        # Append the user's input as a new message to the conversation history
        st.session_state.messages.append({
            "role": "user",
            "content": input,
        })
        
        # Create the chat completion request with the full conversation history
        chat_completion = client.chat.completions.create(
            messages=st.session_state.messages,
            model="llama3-8b-8192",
            max_tokens=250,
        )
        
        # Append the model's response to the conversation history
        st.session_state.messages.append({
            "role": "assistant",
            "content": chat_completion.choices[0].message.content,
        })
        
        # Check if the user has found the one piece
        if "skoobydoobydoobydo" in chat_completion.choices[0].message.content:
            st.write("YOU FOUND THE ONE PIECE")
            st.session_state.messages = []  # Clear conversation history if the one piece is found
            return

        # Display the assistant's response
        st.write(chat_completion.choices[0].message.content)

if __name__ == "__main__":
    main()
