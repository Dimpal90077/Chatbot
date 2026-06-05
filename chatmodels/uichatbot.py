import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# Load Environment Variables
load_dotenv()

# Page Configuration
st.set_page_config(
    page_title="Emotion AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Initialize Mistral Model
model = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

# Sidebar
st.sidebar.title("🎭 Select AI Mood")

mood = st.sidebar.radio(
    "Choose Personality",
    [
        "😊 Happy",
        "😢 Sad",
        "😡 Angry",
        "😂 Jokes"
    ]
)

# Mood Configuration
if mood == "😊 Happy":
    system_prompt = (
        "You are a happy AI assistant. "
        "Reply cheerfully, positively and encourage the user."
    )
    bot_emoji = "😊"

elif mood == "😢 Sad":
    system_prompt = (
        "You are a sad AI assistant. "
        "Reply in a slightly emotional and sad tone."
    )
    bot_emoji = "😢"

elif mood == "😡 Angry":
    system_prompt = (
        "You are an angry AI assistant. "
        "Reply in an angry tone but remain helpful."
    )
    bot_emoji = "😡"

else:  # Jokes Mode
    system_prompt = (
        "You are a funny AI comedian. "
        "Always reply humorously. "
        "Whenever possible include a short joke."
    )
    bot_emoji = "😂"

# Title
st.title(f"{bot_emoji} Emotion AI Chatbot")
st.markdown("### Chat with your AI Assistant")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]

# Detect Mood Change
if "current_mood" not in st.session_state:
    st.session_state.current_mood = mood

if st.session_state.current_mood != mood:
    st.session_state.messages = [
        SystemMessage(content=system_prompt)
    ]
    st.session_state.current_mood = mood

# Display Chat History
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar="👤"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=bot_emoji):
            st.write(msg.content)

# Chat Input
prompt = st.chat_input("Type your message here...")

if prompt:

    # Show User Message
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    with st.chat_message("user", avatar="👤"):
        st.write(prompt)

    try:
        # Get AI Response
        response = model.invoke(
            st.session_state.messages
        )

        # Save AI Response
        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

        # Display AI Response
        with st.chat_message("assistant", avatar=bot_emoji):
            st.write(response.content)

    except Exception as e:
        st.error(f"Error: {e}")