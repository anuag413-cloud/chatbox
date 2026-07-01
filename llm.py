from groq import Groq

client=Groq(api_key="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")

def ask_llm(messages):

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    return response.choices[0].message.content