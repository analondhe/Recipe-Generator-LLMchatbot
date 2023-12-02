import streamlit as st
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


st.set_page_config(page_title="Recipe Generator🥑", page_icon="*", layout="wide", )
st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://images.unsplash.com/photo-1612538498456-e861df91d4d0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80");
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)

# set prompt template
prompt_template = """You are a human who is trying to give recipes for different  food  items and you need to come up with steps for how to make that food item.
Come up with a step by step instructions for the food item..
"""

system_message_prompt = SystemMessagePromptTemplate.from_template(prompt_template)

human_template = """List teh recipe for this food item: {title}"""
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages(
    [system_message_prompt, human_message_prompt]
)

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")

#lm_chain = LLMChain(llm=pipe, prompt=chat_prompt)

st.title("Recipe Generator🧑🏼‍🍳🥑")
input_title = st.text_input("Ask anything", placeholder="How to make coffee...",)
button = st.button("Ask")
if input_title:
    response = llm_chain.run(title=input_title)
    st.write(response)