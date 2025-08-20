from src.langgraphagenticai.state.state import State 


class BasicChatbotNode:
    """A basic chatbot node for LangGraph Agentic AI."""
    
    def __init__(self, model):
        self.llm = model
        
    def process(self, state:State)-> dict:
        """Process the input state and return a response."""

        return {"messages": self.llm.invoke(state["messages"])}
      