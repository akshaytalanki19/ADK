from google.adk.agents import Agent
from google.adk.tools import google_search
root_agent = Agent(
    name = "frst_agent",
    model = "gemini-2.0-flash",
    instruction =""""
    you are agent that runs based on google search
    """,
    tools = [google_search]
    )