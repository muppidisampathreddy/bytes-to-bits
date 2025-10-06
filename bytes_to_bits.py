import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
import streamlit as st

groq_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_key,  
    model_name="<your_model_name>"
)


command_template="summarize the whole text into a single sentence:{text}"

prompt=PromptTemplate(input_variables=["text"],template=command_template)

chain=prompt | llm

#streamlit ui
st.title("bytes to bits")
st.write("Enter the text to summarize:")
text_input=st.text_area("text input",height=300)

if st.button("summarize"):
    response=chain.invoke({"text":text_input})
    st.write("summary:")
    st.write(response.content)