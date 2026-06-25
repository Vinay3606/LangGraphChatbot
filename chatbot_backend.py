from langgraph.graph import StateGraph,START,END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langchain_ollama import ChatOllama
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from dotenv import load_dotenv

load_dotenv()

llm=ChatOllama(model='qwen2.5:3b')

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage],add_messages]



def chat_node(state:ChatState):

    messages=state['messages']

    response=llm.invoke(messages)

    return {'messages':[response]}



checkpointer=MemorySaver()

graph=StateGraph(ChatState)

graph.add_node('chat_node',chat_node)

graph.add_edge(START,'chat_node')
graph.add_edge('chat_node',END)

chatbot=graph.compile(checkpointer=checkpointer)





