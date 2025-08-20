import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json


class DisplayStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == "Basic chat bot":
            for event in graph.stream({'messages': [("user", user_message)]}):
                for value in event.values():
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        assistant_message = ""
                        messages = value.get('messages')
                        # If messages is an AIMessage object, get its content
                        if hasattr(messages, "content"):
                            assistant_message = messages.content
                        # If messages is a list, get the last message's content
                        elif isinstance(messages, list) and len(messages) > 0:
                            last_msg = messages[-1]
                            if isinstance(last_msg, tuple) and len(last_msg) > 1:
                                assistant_message = last_msg[1]
                            elif hasattr(last_msg, "content"):
                                assistant_message = last_msg.content
                        if assistant_message:
                            st.write(assistant_message)
                        else:
                            st.warning("No assistant response received.")
        elif usecase == "Chatbot With Web":
            #Prepare state and invoke the graph
            initial_state = {"messages": [user_message]}
            res = graph.invoke(initial_state)
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool call start")
                        st.write(message.content)
                        st.write("Tool call end")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)