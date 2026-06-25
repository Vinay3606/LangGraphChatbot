import streamlit as st
from chatbot_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid #Generate New Thread Id for when userr required



#******************* UTILITY FUNCTION **********

def generate_thread_id():
    thread_id=uuid.uuid4
    return thread_id


#************************* SETUP  ******************************
if 'message_history' not in st.session_state:
    st.session_state['message_history']=[]

if 'thread_id' not in st.session_state:
    st.session_state['thread_id']=generate_thread_id()

#************************** SIDEBAR UI ********************************
st.sidebar.title('LangGraph Chatbot')

st.sidebar.button('New Chat')

st.sidebar.header('My Conversation')

st.sidebar.text(st.session_state['thread_id'])

#***********************  MAIN UI ***********************************


for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content']) 


user_input=st.chat_input('Type Here')

if user_input:

    #first add to message in message history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

        
    CONFIG={'configurable':{'thread_id':st.session_state['thread_id']}}

    #second add a message of assistant in message_history
    response=chatbot.invoke({'messages':[HumanMessage(content=user_input)]},config=CONFIG)
    AI_message=response['messages'][-1].content

    st.session_state['message_history'].append({'role':'Assistant','content':AI_message})
    with st.chat_message('Assistant'):
        st.text(AI_message)
