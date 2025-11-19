from ollama import chat

model = "phi"

print("Jus a chat. Type 'exit' to quit.\n")

while True:
    user_input = input("Me: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = chat(
        model=model,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("AI:", response.message.content, "\n")
