from ollama import chat

response = chat(
    model='phi',
    messages=[
        {'role': 'user', 'content': 'Why is the sky blue?'}
    ]
)

print(response.message.content)
