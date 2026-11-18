
import ollama

def ask_ai(question):
    response = ollama.chat(
        model="llama3.2:1b",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI Study Assistant. Explain everything in simple English."
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response["message"]["content"]

