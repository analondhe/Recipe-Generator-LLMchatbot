import os
import streamlit as st
import chainlit as cl
from langchain.llms import HuggingFaceHub
#from transformers import pipeline
from langchain.llms import LlamaCpp
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

os.environ['API_KEY'] ="********"


st.set_page_config(page_title="Recipe Generator🥑", page_icon="*", layout="wide", )
st.markdown(f"""
            <style>
            .stApp {{background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

#Model details and parameters
model_id = 'LLM MODEL/FALCON Model'

falcon_llm = HuggingFaceHub(huggingfacehub_api_token=os.environ['API_KEY'],
                            repo_id=model_id,
                            model_kwargs={"temperature":0.8,"max_new_tokens":2000})

# set prompt template
prompt_template = """You are an AI assistant that provides helpful answers to user queries.
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template)

human_template = """List teh recipe for this food item: {title}"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])


llm_chain = LLMChain(llm=falcon_llm, prompt=chat_prompt)

st.title("Recipe Generator🧑🏼‍🍳🥑")
input_title = st.text_input("Ask anything", placeholder="How to make coffee...",)
button = st.button("Ask")
if input_title:
    response = llm_chain.run(title=input_title)
    st.write(response)