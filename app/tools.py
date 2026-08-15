import os
import requests

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults


load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
WEATHERSTACK_API_KEY = os.getenv("WEATHERSTACK_API_KEY")


# -----------------------------
# Tavily Search Tool
# -----------------------------

search_tool = TavilySearchResults(
    api_key=TAVILY_API_KEY,
    max_results=2
)


# -----------------------------
# Weather Tool
# -----------------------------

@tool
def get_weather_data(city: str) -> str:
    """
    Fetch current weather information for a city.
    """

    if not WEATHERSTACK_API_KEY:
        return "WeatherStack API key is not configured."

    url = (
        "https://api.weatherstack.com/current?"
        f"access_key={WEATHERSTACK_API_KEY}"
        f"&query={city}"
    )

    try:

        response = requests.get(
            url,
            timeout=20
        )

        response.raise_for_status()

        data = response.json()

    except requests.RequestException as e:

        return f"Weather request failed: {e}"

    if "current" not in data:

        return (
            f"Could not fetch weather data for {city}. "
            f"Reason: {data.get('error', 'Unknown error')}"
        )

    return (
        f"City: {city}\n"
        f"Temperature: {data['current']['temperature']}°C\n"
        f"Weather: {data['current']['weather_descriptions'][0]}\n"
        f"Humidity: {data['current']['humidity']}%"
    )


# -----------------------------
# All Agent Tools
# -----------------------------

tools = [
    search_tool,
    get_weather_data
]