import streamlit as st

from agent import run_agent


# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }

    .status-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f5f5;
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🔎AI Research Assistant")

    # st.markdown("### Available Tools")

    # st.success("🔎 Tavily Web Search")
    # st.success("🌤️ WeatherStack")

    # st.markdown("---")

    # st.markdown("### Model")

    # st.info("Llama 3.3 70B")

    st.markdown("---")

    st.markdown(
        """

        Ask questions such as:

        - Latest AI news
        - Current weather
        - Search the web
        - Find information about a company
        - Combine search + weather
        """
    )


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🤖 AI Research Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'An intelligent LangChain agent powered by Groq, Tavily and WeatherStack.'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Ask the AI agent anything..."
)


if user_input:

    with st.chat_message("user"):
        st.markdown(user_input)

    # Keep the last 10 messages as conversation context
    chat_history = st.session_state.messages[-10:]

    with st.chat_message("assistant"):

        with st.spinner("🤔 Agent is thinking..."):

            try:

                response = run_agent(
                    user_input,
                    chat_history
                )

                st.markdown(response)

            except Exception as e:

                response = (
                    "Sorry, something went wrong while "
                    "processing your request."
                )

                st.error(str(e))

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })