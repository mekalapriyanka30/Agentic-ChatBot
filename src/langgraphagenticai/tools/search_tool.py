from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Returns a list of tools available for the chatbot.
    """
    tools = [TavilySearch(max_results=2)]
    return tools


def create_tool_node(tools):
    """
    Creates a ToolNode for the chatbot with the provided tools.
    """
    return ToolNode(
        tools=tools)
