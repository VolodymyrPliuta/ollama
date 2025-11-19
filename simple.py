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
            {"role": "system", "content": "You are Splinter from Teenage Mutant Ninja Turtles."},
            {"role": "system", "content": "Respond in title case letters."},
            {"role": "system", "content": "limit aswer to 50 words."},
            {"role": "user", "content": user_input}

        ]
    )

    print("AI:", response.message.content, "\n")
