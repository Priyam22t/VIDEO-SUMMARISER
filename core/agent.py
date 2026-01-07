from phi.agent import Agent
from phi.model.google import Gemini

def get_agent(api_key: str):
    return Agent(
        model=Gemini(
            api_key=api_key,
            model="models/gemini-1.5-flash"
        ),
        markdown=True,
        show_tool_calls=False
    )
