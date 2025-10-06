Bytes to Bits

Bytes to Bits is a simple web app that summarizes long text into a single sentence using a Groq-powered language model. The app provides a clean interface to paste or write your text and generate a concise summary instantly.

Features

Summarizes any text into one sentence

Streamlit-based web interface

Powered by LangChain + Groq AI

How to Use

Enter or paste your text in the text area.

Click the Summarize button.

Get the summarized text immediately below.

Tech Stack

Python 3

LangChain (ChatGroq)

Streamlit

Setup Instructions

Clone the repository:

git clone https://github.com/muppidisampathreddy/bytes-to-bits.git


Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Set your Groq API key in environment variables:

export GROQ_API_KEY="YOUR_API_KEY"


Run the app:

streamlit run bytes_to_bits.py
