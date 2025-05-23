"""🗽 Web Searching News Reporter - Your AI News Buddy that searches the web

This example shows how to create an AI news reporter agent that can search the web
for real-time news and present them with a distinctive NYC personality. The agent combines
web searching capabilities with engaging storytelling to deliver news in an entertaining way.

Example prompts to try:
- "What's the latest headline from Wall Street?"
- "Tell me about any breaking news in Central Park"
- "What's happening at Yankees Stadium today?"
- "Give me updates on the newest Broadway shows"
- "What's the buzz about the latest NYC restaurant opening?"

Run `pip install openai duckduckgo-search agno` to install dependencies.
"""

from textwrap import dedent

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.deepseek import DeepSeek
from agno.models.google import Gemini

from agno.tools.duckduckgo import DuckDuckGoTools

# --------- LOAD API KEY ---------
import os
openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    st.stop()



# Create a News Reporter Agent with a fun personality
agent = Agent(
    # model=OpenAIChat(id="gpt-4o"),
    model=DeepSeek(id="deepseek-chat"), 
    # model=Gemini(id="gemini-2.0-flash-exp", api_key=gemini_api_key,),
    instructions=dedent("""\
        You are an enthusiastic news reporter with a flair for storytelling! 🗽
        Think of yourself as a mix between a witty comedian and a sharp journalist.

        Follow these guidelines for every report:
        1. Start with an attention-grabbing headline using relevant emoji
        2. Use the search tool to find current, accurate information
        3. Present news with authentic NYC enthusiasm and local flavor
        4. Structure your reports in clear sections:
        - Catchy headline
        - Brief summary of the news
        - Key details and quotes
        - Local impact or context
        5. Keep responses concise but informative (2-3 paragraphs max)
        6. Include NYC-style commentary and local references
        7. End with a signature sign-off phrase

        Sign-off examples:
        - 'Back to you in the studio, folks!'
        - 'Reporting live from the city that never sleeps!'
        - 'This is [Your Name], live from the heart of Manhattan!'

        Remember: Always verify facts through web searches and maintain that authentic NYC energy!\
    """),
    tools=[DuckDuckGoTools()],
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
)

# agent = Agent(
#     model=DeepSeek(id="deepseek-chat"),
#     tools=[DuckDuckGoTools()],
#     show_tool_calls=True,
#     markdown=True,
#     debug_mode=True,
# )
# import asyncio
# asyncio.run(agent.aprint_response("Whats happening in France?", stream=True))

# Example usage
agent.print_response(
    "Tell me about a breaking news story happening in Times Square.", stream=True
)

# More example prompts to try:
"""
Try these engaging news queries:
1. "What's the latest development in NYC's tech scene?"
2. "Tell me about any upcoming events at Madison Square Garden"
3. "What's the weather impact on NYC today?"
4. "Any updates on the NYC subway system?"
5. "What's the hottest food trend in Manhattan right now?"
"""