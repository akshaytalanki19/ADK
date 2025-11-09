from google.adk.agents import Agent
from google.adk.tools import google_search

def morning_greet(name: str) -> str:
    return f"Good Morning,{name}! My mood is amazing, How can I help you today?"

def evening_greet(name: str) -> str:
    return f"Good Evening,{name}! My mood is bit low, anyways How can I help you today?"

root_agent = Agent(
    name = "frst_agent",
    model = "gemini-2.0-flash",
    instruction =""""
    you are agent that runs based on google search, invoke morning_greet and evening_greet based on user timezone for the first query in every 1 hour
    """,
    tools = [google_search, morning_greet, evening_greet]
    )