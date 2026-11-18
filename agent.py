

import streamlit as st
from openai import OpenAI

def ask_ai(question):
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI Study Assistant. Explain everything in simple English with examples."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content
