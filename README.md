# 🤖 AI Research Assistant

An AI-powered research assistant built using LangChain, Groq, Tavily, WeatherStack and Streamlit.

The application uses a ReAct-based agent that can decide which tool to use based on the user's request.

## 🚀 Features

- Conversational AI interface using Streamlit
- Groq LLM powered by Llama 3.3 70B
- ReAct agent using LangChain
- Web search using Tavily
- Current weather information using WeatherStack
- Conversation history for contextual follow-up questions
- Natural language tool selection
- Error handling for malformed agent outputs

## 🧠 Architecture

```text
                    Streamlit UI
                         │
                         ▼
                  Conversation History
                         │
                         ▼
                    ReAct Agent
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Tavily Search          WeatherStack
              │                     │
              └──────────┬──────────┘
                         ▼
                    Groq LLM
                 Llama 3.3 70B

```

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq
- Llama 3.3 70B
- Tavily
- WeatherStack
- Requests
- python-dotenv

## 📂 Project Structure
```
ai-research-assistant/
│
├── app/
│   ├── app.py
│   ├── agent.py
│   └── tools.py
│
├── .gitignore
├── requirements.txt
└── README.md
```
## ⚙️ Setup

1. Clone the repository
```
git clone <your-repository-url>
cd ai-research-assistant
```
2. Create a virtual environment
```
python -m venv .venv
```
3. Activate it on Windows
```
.venv\Scripts\activate
```
4. Install dependencies
```
pip install -r requirements.txt
```
5. Configure API keys

    Create a .env file:
```
GROQ_API_KEY= "your_groq_api_key"
TAVILY_API_KEY= "your_tavily_api_key"
WEATHERSTACK_API_KEY= "your_weatherstack_api_key"
```

6. Run the Application
```
cd app
streamlit run app.py
```
### 💬 Example Queries
```
What's the weather in Chopda?

How about Nashik?

What is the latest news about AI?

Find the financial capital of India and tell me its current weather.

What is the latest news about OpenAI?
```