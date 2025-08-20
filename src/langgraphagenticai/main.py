import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayStreamlit

def load_langgraph_agenticai_app():
    """Load the LangGraph Agentic AI application UI using Streamlit."""

##load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Enter your message:")


    if user_message:
        try:
            ## configure the LLMs
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model=obj_llm_config.get_llm_model()

            if not model:
                st.error("Failed to initialize the LLM model.")
                return
            
            # Process the user message with the LLM
            usecase = user_input.get('selected_usecase')

            if not usecase:
                st.error("No use case selected.")
                return

            ##Graph Builder


            graph_builder = GraphBuilder(model)

            try:
                graph= graph_builder.setup_graph(usecase)
                print(user_message)
                DisplayStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Failed to set up the graph: {e}")
                return
            
        except Exception as e:
            st.error(f"Graph setup failed: {e}")
            return