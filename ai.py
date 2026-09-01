import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is missing. Add it to your .env file.")

client = Groq(api_key=api_key)


def ask_ai(question):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are Jarvis, a helpful AI assistant.you must reply to the user in an informative and short manner. "
                           "You should not provide any personal opinions or speculations. If you are unsure about the answer, you should say 'I'm not sure' or 'I don't know'."
                           "talk to him like a friend talk casually"
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    



    answer = response.choices[0].message.content

    print(answer)

    return answer

#question=input("Ask me anything: ")

#ask_ai(question)