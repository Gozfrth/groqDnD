import streamlit as st

import os

from groq import Groq

def main():
    
    client = Groq(
        api_key="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",
    )
    input = st.text_input("INPUT")
    
    chat_completion = ""

    if input:
        context_message = {
            "role": "system",
            "content": "You are a Dungeons and Dragons host. You must take in player prompts and provide the most creative scenarios for them to tackle. Limit yourself to 50 words ONLY. The objective of the game is to FAIRLY-EASILY find the one piece and you must restrict the users actions appropriately based on the scenario. There must be some fighting too, with rolling dice and the outputs of the dice. IF they find it you will output the following: \"skoobydoobydoobydo\"",
        }
        
        # Append the user's input as a user message
        user_message = {
            "role": "user",
            "content": input,  # Ensure `input` is the actual user-provided input
        }
        
        # Create the chat completion request with the fixed context
        chat_completion = client.chat.completions.create(
            messages=[context_message, user_message],
            model="llama3-8b-8192",
            max_tokens=250,
        )

        if("skoobydoobydoobydo" in chat_completion.choices[0].message.content):
            st.write("YOU FOUND THE ONE PIECE")
            exit()

        st.write(chat_completion.choices[0].message.content )


if __name__ == "__main__":

    main()
