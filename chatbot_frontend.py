import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

CONFIG={'configurable':{'thread_id':'1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content']) 


user_input=st.chat_input('Type Here')

if user_input:

    #first add to message in message history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    #second add a message of assistant in message_history
    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    AI_message=response['messages'][-1].content

    st.session_state['message_history'].append({'role':'Assistant','content':AI_message})
    with st.chat_message('Assistant'):
        st.text(AI_message)
