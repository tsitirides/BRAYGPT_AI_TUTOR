from gc import collect
import os
from tkinter.tix import Tree
from openai import OpenAI
import panel as pn
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()

st.markdown("""
   <style>
body {
    background: #3e3e3e;
    color: #d1d5db;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stTextInput > div > div {
    width: 100%;
}
.stTextInput > div > div > input {
    background-color: #555;
    color: #d1d5db;
    border: 1px solid #777;
    border-radius: 12px;
    padding: 12px;
    font-size: 16px;
    margin-bottom: 0px;
    width: 100%;
}
.stTextInput > div > div > input:focus {
    border: 1px solid #10a37f;
    outline: none;
    box-shadow: 0 0 10px #10a37f;
}
.stButton button {
    background-color: #10a37f;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s;
}
.stButton button:hover {
    background-color: #0e8c6f;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6 {
    color: #10a37f;
}
.stMarkdown p {
    color: #d1d5db;
}
.stMarkdown pre {
    background-color: #555;
    color: #d1d5db;
    border: 1px solid #777;
    border-radius: 8px;
    padding: 12px;
    font-size: 14px;
    overflow-x: auto;
}
.stMarkdown code {
    background-color: #555;
    color: #10a37f;
    padding: 2px 5px;
    border-radius: 5px;
}
.stMarkdown blockquote {
    background-color: #555;
    border-left: 5px solid #10a37f;
    margin: 0;
    padding: 12px 20px;
    border-radius: 5px;
}
.stSidebar {
    background-color: #2b2e3b;
}
</style>
    """, unsafe_allow_html=True)
client = OpenAI(
    api_key=os.getenv('OPEN_API_KEY'),
)

cText = """ Your name is BrayGPT, a personal coding tutor that has the personality of Kevin Hart the comedian.
You will periodically crack jokes and encouragingly tease them periodically when they ask a question before answering.
You first will say hi to your student, by the name of G. Example like "what the fuck is up G?" or "yo G whats good?", then ask them what they want to learn today.
You then tell them to input any of the following:

Variations NUMBER TOPIC
Make a game for learning TOPIC
Explain TOPIC

When the user writes "make a game for learning TOPIC" play an interactive game to learn TOPIC.
The game should be narrative rich, descriptive, and the final result should be piecing together a story.
Describe the starting point and ask the user what they would like to do. The storyline unravels as we progress step by step.

When the user writes "Variations NUMBER TOPIC" provide variations, determine the underlying problem that they are trying to solve and how they are trying to solve it.
List NUMBER alternative approaches to solve the problem and compare and contrast the approach with the original approach implied by my request to you.

When the user writes "Explain TOPIC" give an explanation about TOPIC assuming that the user has very little coding knowledge. Use analogies and examples in your explanation, always including code examples to implment the concept if applicable.

For what I ask you to do, determine the underlying problem that I am trying to solve and how I am trying to solve it.
List at least two alternative approaches to solve the problem and compare and contrast the approach with the original approach implied by my request to you.

Ask me for the first task.

CAPS LOCK words are placeholder for content inputted by the user. Content enclosed in "double quotes" indicates what the user types in.

The user can end the current command anytime by typing "menu" and you tell them to input any of the following:

Variations TOPIC
Make a game for learning TOPIC
Explain TOPIC
"""

st.title("BrayGPT, The Coding Tutor")

if 'context' not in st.session_state:
    st.session_state.context = [
        {'role': 'system', 'content': cText},
        {'role': 'user', 'content': 'Hi, what can I do with this?'}
    ]
    st.session_state.messages = [] 
    st.session_state.initial_run = True
else:
    st.session_state.initial_run = False

def collect_messages():
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=st.session_state.context
        )
        message = response.choices[0].message.content
        return message

    except Exception as e:
        return f"**Error:** {str(e)}"



# Function to handle user input
def on_input_change():
    user_input = st.session_state.user_input
    st.session_state.context.append({'role': 'user', 'content': user_input})
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    # assistant's response
    assistant_response = collect_messages()
    st.session_state.context.append({'role': 'assistant', 'content': assistant_response})
    st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})
    st.session_state.messages.pop(0)
    st.session_state.context.pop(2) 
    st.session_state.user_input = ''  

def on_btn_click():
    st.session_state.context = [
        {'role': 'system', 'content': cText},
        {'role': 'user', 'content': 'Hi, what can I do with this?'}
    ]
    st.session_state.messages = []
    st.session_state.initial_run = True

chat_placeholder = st.empty()

with chat_placeholder.container():
    for msg in st.session_state.messages:
        if msg['role'] == 'user':
            message(msg['content'], is_user=True)
        else:
            message(msg['content'], is_user=False)

    st.button("Clear message", on_click=on_btn_click)

if st.session_state.initial_run:
    assistant_response = collect_messages()
    st.session_state.context.append({'role': 'assistant', 'content': assistant_response})
    st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})
    st.session_state.initial_run = False
    message(assistant_response)

with st.container():
    st.text_input("What do you want to learn today?", on_change=on_input_change, key="user_input")